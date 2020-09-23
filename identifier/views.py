from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.utils.text import get_valid_filename

import numpy as np

from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.inception_resnet_v2 import preprocess_input
from yolov5 import detect

import os





# Create your views here.



def cover(request):
    context={'a':1}
    return render(request, 'identifier/cover.html', context)



def detection_cover(request):
    context={'a':1}
    return render(request, 'identifier/detection_cover.html', context)


from urllib import parse


def detection_result(request):
    print('request.FILES=', request.FILES)
    fileObj = request.FILES['filePath']
    print('fileObj=', fileObj)
    fs = FileSystemStorage()
    filename_encoded = parse.quote(fileObj.name)    # 한글 에러나서 ?로 인코딩 해주는 함수
    print('fileObj.name =', filename_encoded)
    filePathName = fs.save(get_valid_filename(filename_encoded), fileObj)
    image_path = './media/'+filePathName
    output_path = './media/output/'+filePathName
    print('image_path=', image_path)

    os.system('pwd')

    class OptClass:
        def __init__(self):
            self.weights = './yolov5/runs/exp8_i2_PA+pano_yolov5x_results/weights/best_i2_PA+pano_yolov5x_results.pt'
            self.source = image_path
            self.output = './media/output'
            self.img_size = 640
            self.conf_thres = 0.4
            self.iou_thres = 0.5
            self.device = ''
            self.view_img = None
            self.save_txt = True
            self.classes = None
            self.agnostic_nms = None
            self.augment = None
            self.update = None

    opt = OptClass()

    detect.detect(opt)

    context={'file_name':fileObj.name, 'output_path':output_path}
    return render(request, 'identifier/detection_result.html', context)




img_height, img_width = 150, 150
# with open('models/classes.txt','r') as f:
#     labelInfo = f.read()
labels = ['GS3', 'SS', 'TS mini', 'TS3', 'TS4']

model = load_model('models/InceptionResNetV2_epoch_1000.h5')


def predictImage(request):
    # print('request.POST.dict()=',request.POST.dict())
    fileObj=request.FILES['filePath']
    print('fileObj:',fileObj)
    fs=FileSystemStorage()
    filePathName=fs.save(get_valid_filename(fileObj.name),fileObj)
    print('filePathName:',filePathName)
    # filePathName = fs.url(filePathName)
    # print(filePathName)
    image_path = './media/'+filePathName

    resized_image = load_img(image_path, target_size=(img_height, img_width))
    image_array = img_to_array(resized_image)
    image_array = image_array.reshape((1, img_height, img_width, 3))
    preprocessed_image_array = preprocess_input(image_array)

    prediction = model.predict(preprocessed_image_array)[0]
    idx = np.argmax(prediction)
    predictedLabel = labels[idx]
    predictReliability = round(prediction[idx]*100, 2)

    print(predictedLabel, predictReliability)

    context={'file_name':fileObj.name, 'image_path':image_path, 'predictedLabel':predictedLabel, 'predictReliability':predictReliability}

    return render(request, 'identifier/predict.html', context)