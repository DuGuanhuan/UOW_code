import datetime
import os

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from user.models import User
from .models import *
from .predict import image_detection
workdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    total_user = len(User.objects.all())
    total_info = Pic.objects.count()
    date = datetime.datetime.today()
    month = date.month
    year = date.year
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


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)  # 有文件上传要传如两个字段
        if form.is_valid():
            m = User.objects.get(pk=request.session['user_id'])
            m.image = form.cleaned_data['image']  # 直接在这里使用 字段名获取即可
            m.save()
            return HttpResponse('image upload success')
        return HttpResponseForbidden('allowed only via POST')



def get_data(request):
    """
    获取列表信息 | 模糊查询
    :param request:
    :return:
    """
    keyword = request.GET.get('name')
    page = request.GET.get("page", '')
    limit = request.GET.get("limit", '')
    role_id = request.GET.get('position','')
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
        for user in results:
            record = {
                "id": user.id,
                "name": user.name,
                "eye_status": user.eye_status,
                "yawn": user.yawn,
                "status": user.status,
                'create_time': user.create_time.strftime('%Y-%m-%d %H:%m:%S'),

            }
            data.append(record)
        response_data['count'] =len(results_obj)
        response_data['data'] = data

    return JsonResponse(response_data)


def data(request):
    """
    跳转页面
    """
    username = request.session['username']
    role = int(request.session['role'])
    user_id= request.session['user_id']
    return render(request, 'pics.html', locals())
def analysis(request):
    """
    跳转页面
    """

    username = request.session.get('username', 'admin')
    role = int(request.session.get('role', 3))
    user_id = request.session.get('user_id', 1)
    results = Pic.objects.values('eye_status').annotate(myCount=Count('eye_status'))  # 返回查询集合
    country = []
    count = []
    for i in results:
        country.append(i['eye_status'])
        count.append(i['myCount'])
    result1 = Pic.objects.values('yawn').annotate(myCount=Count('yawn'))  # 返回查询集合
    values = []
    for i in result1:
        if i['yawn']:
            name = '打哈欠'
        else:
            name = '不打哈欠'
        values.append({'name':name,'value':i['myCount']})
    print(values)
    return render(request, 'analysis.html', locals())
def detection(request):
    """
    跳转页面
    """
    username = request.session['username']
    role = int(request.session['role'])
    user_id= request.session['user_id']
    return render(request, 'detection.html', locals())
def pics(request):
    """
    跳转页面
    """
    username = request.session['username']
    role = int(request.session['role'])
    user_id= request.session['user_id']
    return render(request, 'pics.html', locals())
def edit_data(request):
    """
    修改信息
    """
    response_data = {}
    user_id = request.POST.get('id')
    username = request.POST.get('username')
    phone = request.POST.get('phone')
    User.objects.filter(id=user_id).update(
        name=username,
        phone=phone)
    response_data['msg'] = 'success'
    return JsonResponse(response_data, status=201)


def del_data(request):
    """
    删除信息
    """
    user_id = request.POST.get('id')
    result = User.objects.filter(id=user_id).first()
    try:
        if not result:
            response_data = {'error': '删除失败！', 'message': '找不到id为%s' % user_id}
            return JsonResponse(response_data, status=403)
        result.delete()
        response_data = {'message': '删除成功！'}
        return JsonResponse(response_data, status=201)
    except Exception as e:
        response_data = {'message': '删除失败！'}
        return JsonResponse(response_data, status=403)

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
    file_path = os.path.join(workdir, 'static', 'uploadImg', image.name)
    if not os.path.exists(os.path.join(workdir, 'static', 'result')):
        os.mkdir(os.path.join(workdir, 'static', 'result'))
    result_path = os.path.join(workdir, 'static', 'result', image.name)
    try:
        eye_status,yawn = image_detection(file_path,result_path)
        if eye_status == '闭眼' or yawn:
            status = True
        else:
            status = False
        Pic.objects.create(
            name=image.name,
            eye_status=eye_status,
            yawn=yawn,
            status=status)
        return JsonResponse({"eye_status": eye_status, 'yawn': yawn, 'error': 0,'status':status})
    except Exception as e:
        print(e)
        return JsonResponse({"error": 403})
