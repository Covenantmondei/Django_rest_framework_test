from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', Hello.as_view(), name="hello"),
    path('form/', Logistic.as_view(), name="logistic"),
    path('create-school', create_school, name="Create School"),
    path('create-student', create_student, name="Create Student")
]