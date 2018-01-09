from django.conf.urls import url
from views import visitor_form, login_form, VisitorInfoAPI, change_password
from django.contrib.auth.views import logout
from django.conf import settings

urlpatterns = [
    url(r'^$', login_form, name='login_form'),
    url(r'^logout/?$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^change_password/?$', change_password, name='change_password'),
    url(r'^form/?$', visitor_form, name='visitor_form'),
    url(r'^visitor-data/?$', VisitorInfoAPI.as_view()),
]

