from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', Hello.as_view(), name="hello"),
    path('form/', Logistic.as_view(), name="logistic"),
]