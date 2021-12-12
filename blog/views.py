from django.shortcuts import render
from . import models

def get_posts(request):
    post = models.Post.objects.all()
    return render(request, 'post_list_html', {'post': post})