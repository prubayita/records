from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('bank_overview/', views.bank_overview, name='bank_overview'),
    path('mt_overview/', views.mt_overview, name='mt_overview'),
    path('bank_record/', views.bank_record, name='bank_record'),
    path('mt_record/', views.mt_record, name='mt_record'),
    path('users/', views.user_list, name='user_list'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/approve/<int:user_id>/', views.approve_staff, name='approve_staff'),
]