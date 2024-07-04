from django.urls import re_path
from .consumers import HealthCheckConsumer, ChatConsumer

websocket_urlpatterns = [
  re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
  re_path(r'ws/health_check/$', HealthCheckConsumer.as_asgi())
]