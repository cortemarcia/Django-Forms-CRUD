from django.urls import path
from dono.views import *

urlpatterns = [
    path('cadastro/', cadastro),
    path('delete/<int:id>', delete_people),
    path('update/<int:id>', update_people),
]

