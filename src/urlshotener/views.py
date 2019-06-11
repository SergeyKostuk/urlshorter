from django.shortcuts import render, redirect, get_object_or_404
from .models import Url


# Create your views here.

def make_makeshorter(url):
    new_url = Url.objects.get_or_create(short_url=url)[0]

    new_url.save()
    return f'{new_url.short_url}'


def home(request):
    if request.method == 'GET':
        urls = Url.objects.all()

        context = {'urls': urls}

        return render(request, 'home.html', context)
    elif request.method == "POST":

        Url.objects.create(
            long_url=request.POST.get('url'),

        )
        return redirect('home')


def redir(request, short_url):
    if request.method == 'GET':
        url = get_object_or_404(Url, short_url=short_url)
        url.count += 1
        url.save()
        print(url)
        return redirect(url.long_url)
