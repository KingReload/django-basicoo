from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', include(
        ('%s.apps.core.urls' % settings.PROJECT_NAME),
        namespace='core')),
    url('', include(
        ('%s.apps.switch.urls' % settings.PROJECT_NAME),
        namespace='switch')),

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
