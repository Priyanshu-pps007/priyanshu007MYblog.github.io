from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.loginuser,name='loginuser'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('blog',views.blog,name='blog'),
    path('logout_view',views.logout_view,name='logout_view'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)