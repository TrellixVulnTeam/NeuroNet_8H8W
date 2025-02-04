"""
NeuroNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from public_fulfillment.views import about, root, corona_hackathon_root
from public_fulfillment.views import disclaimer, agreement, back_from_disclaimer
from public_fulfillment.views import corona_hackathon_redirection
from public_fulfillment.views import favicon
from django.contrib.auth.views import LoginView, LogoutView
from public_fulfillment import forms
from coplay.views import extention_add_with_url
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', root, name="home"),
    path('favicon.ico/', favicon, name="favicon"),
    #path('CoronaVirusHackathon/', corona_hackathon_redirection, name="corona_hackathon_redirection"),
    path('disclaimer/', disclaimer, name="disclaimer"),
    path('agreement/', agreement, name="agreement"),

    path('back_from_disclaimer/', back_from_disclaimer, name="back_from_disclaimer"),
    path('about/', about, name="about"),
    #path('ntmu/', include(('nice_to_meet_you.urls', "nice_to_meet_you"), "nice_to_meet_you")),
    path('coplay/', include(('coplay.urls', 'coplay'), 'coplay')),
    path('memecache/', include(('memecache.urls', 'memecache'), 'memecache')),
    path('site/', include(('public_fulfillment.urls', "public_fulfillment"), "public_fulfillment")),
    #path('labs/', labs_root, name="labs_root"),
    path('login/',
        LoginView.as_view
        (
            template_name='login.html',
            authentication_form=forms.BootstrapAuthenticationForm,
            redirect_authenticated_user = True,
            #extra_context=
            #{
            #    'title': 'Log in',
            #    'year' : datetime.now().year,
            #}
        ),
    name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    #path('password_reset/', include(('password_reset.urls', "password_reset"), "password_reset")),
    path('api-auth/', include(('rest_framework.urls', "rest_framework"), "rest_framework")),
    path('api-token-auth/', obtain_auth_token, name='obtain_auth_token'),

    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('reset-password', PasswordResetView.as_view(template_name='password_reset_form.html', html_email_template_name='password_reset_email.html'), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    #path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    #path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),password_reset
    path('reset-password/complete/',
    PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('CoronaVirusHackathon/', corona_hackathon_root, name="corona_hackathon_root"),
    path('CoronaVirusHackathon/about/', about, name="about"),
    path('CoronaVirusHackathon/coplay/extention_add_with_url/', extention_add_with_url, name="obsolete_extention_handler"),	
    #path('ntmu/', include(('nice_to_meet_you.urls', "nice_to_meet_you"), "nice_to_meet_you")),
    path('CoronaVirusHackathon/coplay/', include(('coplay.urls', 'coplay'), 'coplay_hackathon')),
    path('CoronaVirusHackathon/memecache/', include(('memecache.urls', "memecache"), "memecache_hackathon")),
    path('CoronaVirusHackathon/site/', include(('public_fulfillment.urls', "public_fulfillment"), "public_fulfillment_hackathon")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
