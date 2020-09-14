from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    context={'a':1}
    return render(request, 'identifier/index.html', context)

def cover(request):
    context={'a':1}
    return render(request, 'identifier/cover.html', context)


def predictImage(request):
    # print('request=',request)
    # print('request.POST=',request.POST)
    print('request.POST.dict()=',request.POST.dict())
    # print('request.FILES=',request.FILES)
    # print("request.FILES['filePath']=",request.FILES['filePath'])
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    # print(fileObj.name)
    filePathName=fs.save(fileObj.name,fileObj)
    print('filaPathName=', filePathName)
    # filePathName=fs.url(filePathName)
    # print('filaPathName2=', filePathName)

    context={'filePathName':filePathName}
    return render(request, 'identifier/cover.html', context)