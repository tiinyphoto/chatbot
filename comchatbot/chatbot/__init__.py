from django.conf.urls import url
from .views import Chat


urlpatterns = [
    url(r'^Hook', Chat.as_view(), name='bot')
]