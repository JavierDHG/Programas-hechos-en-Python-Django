from django.urls import path
from .views import render_posts,post_detail

#Para referenciar mas facilmente todas las urls
app_name = 'blog'

urlpatterns=[
    path('',render_posts,name='posts'),
    path('<int:post_id>', post_detail,name='post_detail')
]
