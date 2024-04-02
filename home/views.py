import uuid
from urllib.parse import urlencode

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from playdjango import settings


def index(request):
    return render(request, 'home/index.html')


def result(request, filename):
    result_filename = settings.MEDIA_URL + 'uploads/images/' + filename

    return render(request, 'home/result.html', {'result_filename': result_filename})



def upload(request):
    if request.method != 'POST' or 'user_image' not in request.FILES:
        return HttpResponse('你沒有上傳圖片檔喔！', status=400)

    file = request.FILES['user_image']

    # uuid 是一個固定格式的長的隨機字串
    # 用 uuid 當檔名是為了避免有人上傳同樣名字的檔案
    filename = uuid.uuid4().hex + '.jpeg'

    # 這裡可以用 「/」 串接資料夾路徑，把完整路徑建立好
    full_filename = settings.MEDIA_ROOT / 'uploads' / 'images' / filename

    # 下面這三行用才把檔案存到 /media/uploads/images 底下
    with open(full_filename, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return redirect(reverse('result', kwargs={'filename': filename}))
