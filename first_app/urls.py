from django.urls import path
from .views import Home, Create_student, Update_student, Save_update_student, Delete_student

urlpatterns = [
    path('', Home, name='home'),
    path('create_student/', Create_student, name='create_student'),
    path('update_student/<int:id>/', Update_student, name='update_student'),
    path('save_update_student/<int:id>/', Save_update_student, name='save_update_student'),
    path('delete_student/<int:id>/', Delete_student, name='delete_student'),
]