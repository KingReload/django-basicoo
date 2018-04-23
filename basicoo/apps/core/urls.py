from django.conf.urls import url
from .views import (
    BanUser, CreateStaff, CreateStyles, DeleteUser,
    GetUsers, Home, ForgotPassword, UpdateStyles, ResetPassword,
    Signup, ViewProfile, ViewUser)

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^create-staff/$', CreateStaff.as_view(), name='create-staff'),
    url(r'^get-users/$', GetUsers.as_view(), name='get-users'),
    url(r'^view-user/$', ViewUser.as_view(), name='view-user'),
    url(r'^ban-user/$', BanUser.as_view(), name='ban-user'),
    url(r'^delete-user/$', DeleteUser.as_view(), name='delete-user'),
    url(r'^profile/$', ViewProfile.as_view(), name='view-profile'),
    url(r'^pw-forgot/$', ForgotPassword.as_view(), name='forgot-password'),
    url(r'^pw-reset/$', ResetPassword.as_view(), name='reset-password'),
    url(r'^website-styles/$', CreateStyles.as_view(), name='website-styles'),

    url(
        r'^update-styles/(?P<pk>[0-9]+)/$',
        UpdateStyles.as_view(),
        name='update-styles'
    ),
]
