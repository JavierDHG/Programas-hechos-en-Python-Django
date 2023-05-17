from django.shortcuts import render, get_object_or_404
from .models import Post

# Retorna retorna todas las publicaciones
def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html',{'posts':posts})

# Retorna en detalle las publicaciones (Eje=/blog/1 hasta infinito)
def post_detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id) #pk=primary key
    return render(request, 'post_detail.html',{'post':post})