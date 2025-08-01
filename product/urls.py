from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', Hello.as_view(), name="hello"),
    path('form/', Logistic.as_view(), name="logistic"),
    path('create-school', create_school, name="Create School"),
    path('create-student', create_student, name="Create Student"),
    path('hello-world', HelloWorld.as_view(), name="Helloo World"),
    path('market', MarketList.as_view(), name="marketlist"),
    path('create-market', CreateMarket.as_view(), name="create")
]