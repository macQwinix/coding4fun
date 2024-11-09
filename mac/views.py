from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from mac.models import Post

# Create your views here.
def home(request: HttpRequest):
    x = str(request.session)
    print("x: {}".format(x))
    x = x.replace('<','&lt;')
    x = x.replace('>','&gt;')
    # return HttpResponse('Hello world, from Mac! <code>{}</code>'.format(x))
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def about(request: HttpRequest):
    return render(request, 'about.html')