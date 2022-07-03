from django.urls import path
 
from account.views import *


urlpatterns = [
    path('', ParseChatView.as_view(), name="parse_chat"),
]
