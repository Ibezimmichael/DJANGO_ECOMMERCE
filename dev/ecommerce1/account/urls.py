from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register', views.register, name='register'),
    path('email-verification/<str:uidb64>/<str:token>', views.email_verification, name='email-verification'),
    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),
    path('email-verification-success', views.email_verification_success, name='email-verification-success'),
    path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('profile-management',views.profile_mangement, name='profile-management'),
    path('delete',views.delete_account, name='delete'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='account/password/password-reset.html'), name='reset_password'),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='account/password/password-reset-sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/password/password-reset-form.html'), name='password_reset_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='account/password/password-reset-complete.html'), name='password_reset_complete'),

    # shipping
    path('manage-shipping', views.manage_shipping, name='manage-shipping'),

    path('track-orders', views.track_orders, name='track-orders'),


]