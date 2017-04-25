"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_complete,password_reset_confirm,password_change,password_change_done
from accounts import views




urlpatterns = [

    url(r'^admin/', admin.site.urls),
   # url(r'^register/$', views.register_view, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^Coach/', include('registration.backends.hmac.urls'), name='Coach_Sign_up'),
    url(r'^Coach/reset/$', password_reset,{'template_name': 'registration/password_reset_form_coach.html','email_template_name': 'registration/password_reset_email_coach.html'}, name='password_reset'),
    url(r'^Coach/reset/done/$', password_reset_done,{'template_name': 'registration/password_reset_done_coach.html'}, name='password_reset_done'),
    url(r'^Coach/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,{'template_name': 'registration/password_reset_confirm_coach.html'}, name='Coach_reset_confirm'),
    url(r'^Coach/reset/complete/$', password_reset_complete,{'template_name': 'registration/password_reset_complete_coach.html'}, name='password_reset_complete'),
    url(r'^Coach/change/$', password_change,{'template_name': 'registration/password_change_form_coach.html'}, name='Coach_change'),
    url(r'^Coach/change/complete$', password_change_done,{'template_name': 'registration/password_change_done_coach.html'}, name='password_change_done'),
    # Coach profile
    url(r'^Coach/Profile/$', views.view_profile, name='Coach_Profile'),
    url(r'^Coach/Profile/Delete/Confirmation$', views.Coach_Delete_Confirmation, name='Coach_Delete_Confirm'),
    url(r'^Coach/Profile/Delete/$', views.Coach_Delete, name='Coach_Delete'),
    url(r'^Coach/location/$', views.edit_profile, name='Coach_Profile_Change_location'),
    url(r'^Coach/Email/$', views.email_edit, name='Coach_Profile_Change_Email'),
    url(r'^Coach/name/change/$', views.flname_edit, name='Coach_Profile_Change_FLname'),
    url(r'^Coach/Addplayer/$', views.Player_view, name='Coach_Profile_Add_Player'),
    url(r'^Coach/AddTeam/$', views.team_view, name='Coach_Profile_Add_Team'),
    url(r'^Coach/Player/View/(?P<player_id>[0-9]+)/$', views.Coach_Profile_Player_View,name='Coach_Player_View'),
    url(r'^Coach/Player/View/Update/(?P<player_id>[0-9]+)/$', views.Coach_Profile_Player_View_Update,name='Coach_Player_View_Update'),
    url(r'^Coach/Player/View/Delete/(?P<player_id>[0-9]+)/$', views.Coach_Profile_Player_View_Delete,name='Coach_Player_View_Delete'),
    url(r'^Coach/Team/View/(?P<team_id>[0-9]+)/$', views.Coach_Profile_Team_View,name='Coach_Team_View'),
    url(r'^Coach/Team/View/Update/(?P<team_id>[0-9]+)/$', views.Coach_Profile_Team_View_Update,name='Coach_Team_Update'),
    url(r'^Coach/Team/View/Delete/(?P<team_id>[0-9]+)/$', views.Coach_Profile_Team_View_Delete,name='Coach_Team_Delete'),
    url(r'^Coach/Team/$', views.Coach_Profile_Team, name='Coach_Profile_Team'),
    #url(r'^Coach/password_reset/$', views.Coach_Profile_Team, name='Coach_Reset_Password'),


    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
