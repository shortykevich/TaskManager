import pytest

from tests import get_response_message
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


@pytest.mark.django_db
def test_tasks_authentication(client, test_tasks, test_users):
    url = reverse('tasks_index')
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)

    url = reverse('tasks_detail', kwargs={'pk': test_tasks['task1'].pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)

    url = reverse('tasks_update', kwargs={'pk': test_tasks['task2'].pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)

    url = reverse('tasks_delete', kwargs={'pk': test_tasks['task1'].pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)


@pytest.mark.django_db
def test_tasks_index(logged_in_client, test_tasks, test_users):
    url = reverse('tasks_index')
    response = logged_in_client.get(url)

    assert response.status_code == 200
    assert 'tasks/index.html' in response.template_name


@pytest.mark.django_db
def test_tasks_detail(logged_in_client, test_tasks, test_users):
    url = reverse('tasks_detail', kwargs={'pk': test_tasks['task1'].pk})
    response = logged_in_client.get(url)

    assert response.status_code == 200
    assert 'tasks/task_page.html' in response.template_name


@pytest.mark.django_db
def test_tasks_create_get(logged_in_client, test_tasks, test_users):
    url = reverse('tasks_create')
    response = logged_in_client.get(url)

    assert response.status_code == 200
    assert 'tasks/create.html' in response.template_name


@pytest.mark.django_db
def test_tasks_create_post(client, test_tasks, test_users, test_statuses):
    current_user = test_users['user1']
    url = reverse('tasks_create')
    client.force_login(current_user)
    response = client.post(url, {
        'name': 'title',
        'description': 'description',
        'executor': test_users['user2'].id,
        'status': test_statuses['status1'].id
    })

    assert response.status_code == 302
    assert response.url == reverse('tasks_index')
    assert _('Task created successfully') == get_response_message(response)


@pytest.mark.django_db
def test_tasks_delete_get(client, test_tasks, test_users):
    test_user1, test_user2 = test_users['user1'], test_users['user2']
    url = reverse('tasks_delete', kwargs={'pk': test_tasks['task1'].pk})

    client.force_login(test_user2)
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('tasks_index')
    assert _('Only author can delete task') == get_response_message(response)

    client.force_login(test_user1)
    response = client.get(url)

    assert response.status_code == 200
    assert 'tasks/delete.html' in response.template_name


@pytest.mark.django_db
def test_tasks_delete_post(client, test_tasks, test_users):
    url = reverse('tasks_delete', kwargs={'pk': test_tasks['task1'].pk})
    client.force_login(test_users['user1'])
    response = client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('tasks_index')
    assert _('Task deleted successfully') == get_response_message(response)
