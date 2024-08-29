import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
def test_users_creation(client, test_user1_data):
    url = reverse('users_create')
    response = client.get(url)

    assert response.status_code == 200
    assert 'users/create.html' in response.template_name

    response = client.post(url, test_user1_data)
    assert response.status_code == 302
    assert response.url == reverse('login')


@pytest.mark.django_db
def test_users_update_get(client, admin_client, test_users):
    url = reverse('users_update', kwargs={'pk': test_users['user1'].pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')

    client.force_login(test_users['user2'])
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse('users_index')

    client.force_login(test_users['user1'])
    response = client.get(url)
    admin_response = admin_client.get(url)

    assert response.status_code == admin_response.status_code
    assert response.status_code == 200
    assert 'users/update.html' in response.template_name


@pytest.mark.django_db
def test_users_update_post(admin_client, test_users):
    test_user = test_users['user1']
    url = reverse('users_update', kwargs={'pk': test_user.pk})
    response = admin_client.post(url, {
        'username': test_user.username,
        'first_name': 'new_name',
        'last_name': 'new_last',
        'password1': test_user.password,
        'password2': test_user.password,
    })

    assert response.status_code == 302
    assert response.url == reverse('users_index')


@pytest.mark.django_db
def test_users_index_get(client, test_users):
    url = reverse('users_index')
    response = client.get(url)

    assert response.status_code == 200
    assert 'users' in response.context_data
