import uuid

from django.http import HttpResponse
from django.shortcuts import render

from playdjango import settings


def index(request):
    if request.method == 'POST':
        return upload(request)

    return render(request, 'home/index.html')


def upload(request):
    if 'user_image' not in request.FILES:
        return HttpResponse('你沒有上傳圖片檔喔！', status=400)

    file = request.FILES['user_image']

    # uuid 是一個固定格式的長的隨機字串
    # 用 uuid 當檔名是為了避免有人上傳同樣名字的檔案
    filename = uuid.uuid4().hex + '.jpeg'

    # 這裡可以用 「/」 串接資料夾路徑，把完整路徑建立好
    full_filename = settings.MEDIA_ROOT / 'uploads' / 'images' / filename

    with open(full_filename, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    result_filename = settings.MEDIA_URL + 'uploads/images/' + filename

    return render(request, 'home/index.html', context={'result_filename': result_filename})
