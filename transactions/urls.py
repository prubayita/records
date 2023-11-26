from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('overview/', views.overview, name='overview'),
    # path('record/', views.record, name='record'),
]