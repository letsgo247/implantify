from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.utils.text import get_valid_filename


from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.inception_resnet_v2 import preprocess_input

import numpy as np




# Create your views here.



def cover(request):
    context={'a':1}
    return render(request, 'identifier/cover.html', context)






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