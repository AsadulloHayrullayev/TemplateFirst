from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('',views.hello_view, name = 'hello'),
    path('about/', views.hello_view, name='about'),
    path('classes/', views.hello_view, name='classes'),
    path('blog/', views.hello_view, name='blog'),
    path('',views.copy_blog_fun,name="copy_blog"),
]



