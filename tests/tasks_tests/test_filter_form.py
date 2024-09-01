import pytest


@pytest.fixture(scope='module')
def url():
    return '/en/tasks/'


@pytest.mark.django_db
def test_tasks_self_filter(url, logged_in_client, test_tasks, test_statuses):
    data = {'self_tasks': 'on'}
    response = logged_in_client.get(url, data=data)

    assert response.status_code == 200
    assert test_tasks['task1'] in response.context['object_list']
    assert test_tasks['task2'] not in response.context['object_list']


@pytest.mark.django_db
def test_tasks_statuses_filter(url, logged_in_client, test_tasks, test_statuses):
    data = {'status': test_statuses['status2'].pk}
    response = logged_in_client.get(url, data=data)

    assert response.status_code == 200
    assert test_tasks['task1'] not in response.context['object_list']
    assert test_tasks['task2'] in response.context['object_list']


@pytest.mark.django_db
def test_tasks_executor_filter(url, logged_in_client, test_tasks, test_users):
    data = {'executor': test_users['user1'].pk}
    response = logged_in_client.get(url, data=data)

    assert response.status_code == 200
    assert test_tasks['task1'] not in response.context['object_list']
    assert test_tasks['task2'] in response.context['object_list']


@pytest.mark.django_db
def test_tasks_combined_filter(url, logged_in_client, test_tasks, test_statuses, test_users):
    data = {'self_tasks': 'on', 'executor': test_users['user1'].pk, 'status': test_statuses['status2'].pk}
    response = logged_in_client.get(url, data=data)

    assert response.status_code == 200
    assert not response.context['object_list']
