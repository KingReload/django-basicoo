from django.conf.urls import url
from django.views.decorators.cache import cache_page
from .views import (
    BanUser, CreateStaff, CreateStyles, DeleteUser,
    GetUsers, Home, ForgotPassword, UpdateStyles, ResetPassword,
    Signup, ViewLogs, ViewProfile, ViewUser)

urlpatterns = [
    url(
        r'^$',
        cache_page(60 * 30)(Home.as_view()),
        name='home'
    ),
    url(
        r'^signup/$',
        cache_page(60 * 30)(Signup.as_view()),
        name='signup'
    ),
    url(
        r'^create-staff/$',
        cache_page(60 * 30)(CreateStaff.as_view()),
        name='create-staff'
    ),
    url(r'^users/$', GetUsers.as_view(), name='get-users'),
    url(r'^view-user/$', ViewUser.as_view(), name='view-user'),
    url(r'^ban-user/$', BanUser.as_view(), name='ban-user'),
    url(
        r'^delete-user/$',
        cache_page(60 * 30)(DeleteUser.as_view()),
        name='delete-user'
    ),
    url(r'^profile/$', ViewProfile.as_view(), name='view-profile'),
    url(
        r'^pw-forgot/$',
        cache_page(60 * 30)(ForgotPassword.as_view()),
        name='forgot-password'
    ),
    url(
        r'^pw-reset/$',
        cache_page(60 * 30)(ResetPassword.as_view()),
        name='reset-password'
    ),
    url(
        r'^website-styles/$',
        cache_page(60 * 30)(CreateStyles.as_view()),
        name='website-styles'
    ),
    url(r'^logs/$', ViewLogs.as_view(), name='log-info'),
    url(
        r'^update-styles/(?P<pk>[0-9]+)/$',
        UpdateStyles.as_view(),
        name='update-styles'
    ),
]
