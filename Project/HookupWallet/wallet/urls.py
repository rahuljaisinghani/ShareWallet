from django.conf.urls import url

from .views import *

app_name = 'event_participants'
urlpatterns = [
    url(r'^wallet', wallet),
    url(r'^user', user),
    url(r'^add_money', add_money),
    url(r'^withdraw_money', withdraw_money),
    url(r'^split_bill', split_bill),
    url(r'^list_users', list_users),
    url(r'^transaction', transaction),
    url(r'^login', login),

]
