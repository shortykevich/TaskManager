import pytest
from django.shortcuts import reverse
from task_manager.statuses.models import Status


@pytest.mark.django_db
def test_statuses_index_get(client, test_users):
    response = client.get(reverse('statuses_index'))

    assert response.status_code == 302
    assert response.url == reverse('login')

    client.force_login(test_users['user1'])
    response = client.get(reverse('statuses_index'))

    assert response.status_code == 200
    assert 'statuses/index.html' in response.template_name


@pytest.mark.django_db
def test_statuses_create_get(client, test_users):
    url = reverse(
        'users_update',
        kwargs={'pk': test_users['user1'].pk}
    )
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')

    client.force_login(test_users['user1'])
    response = client.get(reverse('statuses_create'))

    assert response.status_code == 200
    assert 'statuses/create.html' in response.template_name


@pytest.mark.django_db
def test_statuses_create_post(logged_in_client, test_users):
    url = reverse('statuses_create')
    response = logged_in_client.post(url, {'title': 'title'})

    assert response.status_code == 302
    assert response.url == reverse('statuses_index')
    assert Status.objects.filter(title='title').exists()


@pytest.mark.django_db
def test_statuses_update_get(client, test_statuses, test_users):
    test_status = test_statuses['status1']
    test_user = test_users['user1']
    url = reverse('statuses_update', kwargs={'pk': test_status.pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')

    client.force_login(test_user)
    response = client.get(url)

    assert response.status_code == 200
    assert 'statuses/update.html' in response.template_name


@pytest.mark.django_db
def test_statuses_update_post(logged_in_client, test_statuses, test_users):
    url = reverse('statuses_create')
    response = logged_in_client.post(url, {'title': 'title'})

    assert response.status_code == 302
    assert response.url == reverse('statuses_index')
    assert Status.objects.filter(title='title').exists()


@pytest.mark.django_db
def test_statuses_delete_get(client, test_statuses, test_users):
    test_status = test_statuses['status1']
    test_user = test_users['user1']
    url = reverse('statuses_delete', kwargs={'pk': test_status.pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')

    client.force_login(test_user)
    response = client.get(url)

    assert response.status_code == 200
    assert 'statuses/delete.html' in response.template_name


@pytest.mark.django_db
def test_statuses_delete_post(logged_in_client, test_statuses, test_users):
    test_status = test_statuses['status1']
    url = reverse('statuses_delete', kwargs={'pk': test_status.pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('statuses_index')
