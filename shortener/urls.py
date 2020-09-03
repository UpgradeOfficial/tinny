from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

    


urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('',
     views.home,
      name='home'),
      
      path('<unique_id>/',
      views.url_redirect,
      name='url_redirect'),
      
    path('accounts/login/',
     views.login_view,
      name='login'),
      
    path('accounts/logout/',
     views.logout_view,
      name='logout'),
      
    path('register/',
     views.register,
      name='register'),
      
    path('search',
    views.search,
    name='search'),
    
    path('search_id',
    views.search_id,
    name='search_id'),
    
    path('dashboard/',
     views.dashboard,
      name='dashboard')
    
]

