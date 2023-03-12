from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cms/', include('cms.urls')),
    path('', include('home.urls')),
    path('store/', include('retailstores.urls', namespace='retailstore')),
    path('register/', user_views.register, name='register'),

    path('users/login/', auth_views.LoginView.as_view(template_name='users/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # path('password-reset/', auth_views.PasswordResetView.as_view(
    #     template_name='users/password_reset.html'), name='password_reset'),
    # path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
    #     template_name='users/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'OURSTORE Dashboard'
admin.site.site_title = "Admin Portal"
admin.site.index_title = 'OURSTORE Administration'
