# tests/test_views.py
import pytest
from django.urls import reverse
from tasks.models import Task

@pytest.mark.django_db
def test_create_task(client):
    url = reverse('create_task') 
    
    data = {
        'title': 'Tarea de prueba',
        'description': 'Descripción de la tarea de prueba'
    }

    response = client.post(url, data)
    
    task = Task.objects.get(title='Tarea de prueba')
    assert task.description == 'Descripción de la tarea de prueba'
    assert response.url == '/tasks/'

