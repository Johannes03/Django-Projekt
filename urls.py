from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from website import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='website/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='website/logout.html'), name='logout'),
    path('', include('website.urls')),
]
