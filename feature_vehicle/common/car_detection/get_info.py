# encoding:utf-8
import requests
import base64


def get_token():

    api_key = 'Z4K0kcoE34YrIay7YkykwC0O'
    secret_key = 'YptYw6PQKsR4SCie5xZpZqH2BpOIcBAm'
    #  原始
    # api_key = 'DanmDFGDCpaCxkRAZdBLT9dN'
    # secret_key = '9FuFMHUSjWLemj5hUrkfrvwvlu4MuefY'

    host = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    # host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}'

    response = requests.get(host)
    if response:
        access_token = response.json()['access_token']
        return access_token
        # 24.101b2608c4125e9c115e8957ba8b406b.2592000.1672474165.282335-28766577


def predict(image_path,access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
    # 二进制方式打开图片文件
    f = open(image_path, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img, "top_num": 5}
    print(access_token)
    #access_token = '24.101b2608c4125e9c115e8957ba8b406b.2592000.1672474165.282335-28766577'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers).json()
    print(response)
    if response:
        color_result = response['color_result']
        pinpai = response['result'][0]['name']
        return color_result, pinpai
    else:
        return '黑色','大众'


if __name__ == '__main__':
    access_token = '24.a8286d8f2fbb4ef9ca1a2cf585b2b26d.2592000.1722937194.282335-91808609'

    img_path = './008.png'
    predict(img_path,access_token)



    # predict()