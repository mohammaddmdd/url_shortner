from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import signup, login_view

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('generate', views.generate, name='generate'),
    path('<str:pk>', views.follow, name='follow')
]