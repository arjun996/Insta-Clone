from django.urls import path
from msgapp.views import *
from msgapp.views import *

urlpatterns = [
    path('', inbox, name="inbox"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
    path('search/', UserSearch, name="search-users"),
    path('new/<username>', NewConversation, name="conversation"),
]