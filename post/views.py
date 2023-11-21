from django.shortcuts import render
from .models import Post

def post(request):
    return render(request=request, template_name='post.html', context={})
