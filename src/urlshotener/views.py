from django.shortcuts import render,redirect,get_object_or_404
from .models import Url,generate_url


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
def redir(request,short_url):
    if request.method == 'GET':
        url = get_object_or_404(Url,short_url=short_url)
        print(url)
        return redirect(url.long_url)
#views.py
# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response, get_object_or_404
# >from django.template import RequestContext
# from forms import UrlForm
# from models import ShortUrl, Hit
#  <def make_short_url(url):
#     short_url = ShortUrl.objects.get_or_create(target=url)[0]
# >    short_url.save()
# >    return 'http://example.com/%s' % (short_url.key)
#def index(request):
#    if request.method == 'POST':
#        form = UrlForm(request.POST)
#        if form.is_valid():
#          url = form.cleaned_data.get('url')
#            url = make_short_url(url)
#             return render_to_response('shortener.html', {'url':url})
#     else:
#       form = UrlForm(label_suffix='')
#    return render_to_response('shortener.html', {'form': form, 'url': ''})
#  def redirect(request, key):
#   target = get_object_or_404(ShortUrl, key=key)
#     try:
#         hit = Hit()
#         hit.target = target
#         hit.referer = request.META.get("HTTP_REFERER", "")
#         hit.ip = request.META.get("REMOTE_ADDR", "")
#       hit.user_agent = request.META.get("HTTP_USER_AGENT", "")
#         hit.save()
#     except IntegrityError:<
#        pass
#    return HttpResponseRedirect(target.target) <br/>