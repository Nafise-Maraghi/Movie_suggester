from django.urls import path

from .views import suggestion

urlpatterns = [
    path('suggest/', suggestion),
]
