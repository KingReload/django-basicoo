from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('', include('basicoo.apps.core.urls', namespace='core')),

    url(
        r'^login/$',
        auth_views.login,
        {'template_name': 'unauthorized/login.html'},
        name='login'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': 'login'},
        name='logout'
    ),

    url(r'^admin/', admin.site.urls),
]
