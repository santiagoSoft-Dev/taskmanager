from django.urls import path
from .views import list_tasks, create_task, update_task, delete_task

urlpatterns = [
    path('', list_tasks),
    path('new_task/', create_task, name='create_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task')
]

