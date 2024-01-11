from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("student_add/",student_add),
    path("student_delete/<int:roll>",student_delete),
    path("student_update/<int:roll>",student_update),
    path("do_student_update/<int:roll>",do_student_update),
]