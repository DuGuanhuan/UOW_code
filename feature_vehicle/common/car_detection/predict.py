import os
import json

import torch
from PIL import Image
from torchvision import transforms


# from get_info import predict as bsb   # 单独运行这个文件 要用这个
from .get_info import predict as bsb      # 网页运行要用这个
# from model import resnet50           # 单独运行这个文件 要用这个
from .model import resnet50         # 网页运行要用这个



workdir = os.path.dirname(os.path.abspath(__file__))

def main(img_path,tok):
    # 如果有NVIDA显卡,转到GPU训练，否则用CPU
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # 将多个transforms的操作整合在一起
    data_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    # 确定图片存在，否则反馈错误
    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path)
    # imshow()：对图像进行处理并显示其格式，show()则是将imshow()处理后的函数显示出来
    #plt.imshow(img)
    # [C, H, W]，转换图像格式
    img = data_transform(img)
    # [N, C, H, W]，增加一个维度N
    img = torch.unsqueeze(img, dim=0)
    col , xh = bsb(img_path,tok)
    # 获取结果类型
    json_path = os.path.join(workdir,'class_indices.json')
    # 确定路径存在，否则反馈错误
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
    # 读取内容
    with open(json_path, "r") as f:
        class_indict = json.load(f)

    # 模型实例化，将模型转到device，结果类型有5种
    model = resnet50(num_classes=12).to(device)

    # 载入模型权重
    weights_path = os.path.join(workdir,'models',"resNet50.pth")
    # 确定模型存在，否则反馈错误
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    # 加载训练好的模型参数
    model.load_state_dict(torch.load(weights_path, map_location=device))

    # 进入验证阶段
    model.eval()
    with torch.no_grad():
        # 预测类别
        # squeeze()：维度压缩，返回一个tensor（张量），其中input中大小为1的所有维都已删除
        output = torch.squeeze(model(img.to(device))).cpu()
        # softmax：归一化指数函数，将预测结果输入进行非负性和归一化处理，最后将某一维度值处理为0-1之内的分类概率
        predict = torch.softmax(output, dim=0)
        # argmax(input)：返回指定维度最大值的序号
        # .numpy()：把tensor转换成numpy的格式
        predict_cla = torch.argmax(predict).numpy()

    # 输出的预测值与真实值
    print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
                                                 predict[predict_cla].numpy())
    print(print_res)

    return class_indict[str(predict_cla)],col,xh


if __name__ == '__main__':
    tok = '24.a8286d8f2fbb4ef9ca1a2cf585b2b26d.2592000.1722937194.282335-91808609'

    # img_path = '001.png'
    img_path = './1.jpg'
    result = main(img_path,tok)
    print(result)
