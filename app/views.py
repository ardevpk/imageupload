from django.shortcuts import render, redirect
from .models import upload
from django.contrib import messages

# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    header = request.META
    ip = get_client_ip(request)
    context = {
        'user': header['USERNAME'],
        'ip': ip,
    }
    return render(request, 'index.html', context)


def detail(request):
    header = request.META
    ip = get_client_ip(request)
    if request.method == 'POST':
        image = request.FILES['image'] if 'image' in request.FILES else None
        if upload.objects.filter(user=ip).__len__() < 10:
            uploader = upload.objects.create(user=ip, image=image)
            uploader.save()
        else:
            messages.add_message(request, messages.ERROR, 'You Exceed Your Image Upload Limit 10')
    context = {
        'user': header['USERNAME'],
        'ip': ip,
        'data': upload.objects.filter(user=ip),
    }
    return render(request, 'detail.html', context)


def delete(request, id):
    todelete = upload.objects.get(id=id)
    todelete.delete()
    return redirect('/detail/')