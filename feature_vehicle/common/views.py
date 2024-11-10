import datetime
import os
import time

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from user.models import User
from .models import *
from .car_detection import predict as main
workdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .car_detection.get_info import get_token
def login(req):
    """
    跳转登录
    :param req:
    :return:
    """
    return render(req, 'login.html')


def register(req):
    """
    跳转注册
    :param req:
    :return:
    """
    return render(req, 'register.html')


def index(req):
    """
    跳转首页
    :param req:
    :return:
    """
    username = req.session['username']
    total_user = User.objects.count()
    date = datetime.datetime.today()
    month = date.month
    year = date.year
    total_pic = Pic.objects.count()
    total_car = Car.objects.count()
    current_time = datetime.datetime.now()
    # create_time = Info.objects.filter(id=1).first().create_time
    gqsj = current_time + datetime.timedelta(days=30)
    # if current_time > create_time:
    #     t = get_token()
    #     Info.objects.filter(id=1).update(
    #         token=t,
    #         create_time=gqsj
    #     )
    return render(req, 'index.html', locals())


def login_out(req):
    """
    注销登录
    :param req:
    :return:
    """
    del req.session['username']
    return HttpResponseRedirect('/')


def personal(req):
    username = req.session['username']
    role_id = req.session['role']
    user = User.objects.filter(name=username).first()
    return render(req, 'personal.html', locals())



def scdq(request):
    username = request.session['username']
    results = Car.objects.all()
    return render(request,'scdq.html',locals())

def detection(request):
    username = request.session['username']
    image_list = Pic.objects.all()
    return render(request, 'pic.html', locals())

# 保存缓存文件
def save_file(file):
    if file is not None:
        file_name = os.path.join(workdir, 'static', 'uploadImg', file.name)
        with open(file_name, 'wb')as f:
            # chunks()每次读取数据默认 我64k
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
        return file_name
    else:
        return None
def predict(request):
    image = request.FILES.get('image')
    file_name = save_file(image)
    tt = Info.objects.filter(id=1).first().token
    file_path = os.path.join(workdir, 'static', 'uploadImg', image.name)
    try:
        car_type,col,xh = main.main(file_path,tt)
        #car_type,col,xh = '小轿车','黑色','宝马'
        Pic.objects.create(name=image.name,
                           path=file_path,
                           xh=xh,
                           color=col,
                           type=car_type)
        return JsonResponse({"color":col,'xh':xh,'type':car_type,'error':0})
    except Exception as e:
        print(e)
        return JsonResponse({"error":403})


def get_result(request,pic_id):
    result = Pic.objects.filter(id=pic_id).first()
    car_type = result.type
    color = result.color
    xh = result.xh
    return JsonResponse({'car_type': car_type,'xh':xh,'color':color})


def get_pic(request):
    """
    获取用户列表信息 | 模糊查询
    :param request:
    :return:
    """
    keyword = request.GET.get('name')
    page = request.GET.get("page", '')
    limit = request.GET.get("limit", '')
    role_id = request.GET.get('position', '')
    response_data = {}
    response_data['code'] = 0
    response_data['msg'] = ''
    data = []
    if keyword is None:
        results_obj = Pic.objects.all()
    else:
        results_obj = Pic.objects.filter(name__contains=keyword).all()

    paginator = Paginator(results_obj, limit)
    results = paginator.page(page)

    if results:
        for result in results:
            record = {
                "id": result.id,
                "name": result.name,
                "path": result.path,
                "type": result.type,
                "xh": result.xh,
                "color": result.color,
                'create_time': result.create_time.strftime('%Y-%m-%d %H:%m:%S'),
            }
            data.append(record)
        response_data['count'] = len(results_obj)
        response_data['data'] = data

    return JsonResponse(response_data)


def pics(request):
    username = request.session['username']
    role = int(request.session['role'])
    user_id = request.session['user_id']
    return render(request, 'pics.html', locals())


def del_pic(request):
    """
    删除图片
    """
    pic_id = request.POST.get('id')
    result = Pic.objects.filter(id=pic_id).first()
    try:
        if not result:
            response_data = {'error': '删除失败！', 'message': '找不到id为%s' % pic_id}
            return JsonResponse(response_data, status=403)

        result.delete()
        response_data = {'message': '删除成功！'}
        return JsonResponse(response_data, status=201)
    except Exception as e:
        response_data = {'message': '删除失败！'}
        return JsonResponse(response_data, status=403)

def qcbk(request):
    username = request.session['username']
    results = CarKnowledge.objects.all()
    return render(request,'qcbk.html',locals())


def add_message(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    CarKnowledge.objects.create(
        title=title,
        desc=text
    )
    return JsonResponse({'msg':'ok'})