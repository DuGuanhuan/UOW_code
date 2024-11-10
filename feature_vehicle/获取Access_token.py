
import requests
import json


def main():

    api_key = 'Z4K0kcoE34YrIay7YkykwC0O'
    secret_key = 'YptYw6PQKsR4SCie5xZpZqH2BpOIcBAm'


    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

if __name__ == '__main__':
    main()


# 2024.7.7更新
# access_token：要获取的Access Token；
# 24.a8286d8f2fbb4ef9ca1a2cf585b2b26d.2592000.1722937194.282335-91808609
# expires_in：Access Token的有效期(秒为单位，有效期30天)；





