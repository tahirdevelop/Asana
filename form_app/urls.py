from .views import *
from django.urls import path

urlpatterns = [
    path('', index.as_view(), name='helo world'),
]