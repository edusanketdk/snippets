from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import blog

class blogList(generic.ListView):
    queryset = blog.objects.order_by('created_on')
    template_name = 'home.html'

class blogDetail(generic.DetailView):
    model = blog
    template_name = 'blog.html'

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def editor(request):
    return render(request, "editor.html")
