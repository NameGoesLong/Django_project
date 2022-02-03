from django.urls import path

from apps.users.views import UsernameCountView

# Unpack the request using urlpatterns
# <username:username> will call the converter included in ddprobe_mall/urls.py and do the regex check
urlpatterns = [
    path('usernames/<username:username>/count/',UsernameCountView.as_view()),
    
]
