import pytest
from django.shortcuts import reverse
from django.contrib.auth import login


@pytest.mark.django_db
def test_user_creation(client, test_user1_data):
    url = reverse('users_create')
    response = client.get(url)

    assert response.status_code == 200
    assert 'users/create.html' in response.template_name

    response = client.post(url, test_user1_data)
    assert response.status_code == 302
    assert response.url == reverse('login')


@pytest.mark.django_db
def test_update_user_get(client, admin_client, test_users):
    test_user1, test_user2 = test_users['user1'], test_users['user2']
    url = reverse('users_update', kwargs={'pk': test_user1.pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')

    client.force_login(test_user2)
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse('users_index')

    client.force_login(test_user1)
    response = client.get(url)
    admin_response = admin_client.get(url)

    assert response.status_code == admin_response.status_code
    assert response.status_code == 200
    assert 'users/update.html' in response.template_name
    assert 'user' in response.context


@pytest.mark.django_db
def test_update_user_post(admin_client, test_users):
    test_user1, test_user2 = test_users['user1'], test_users['user2']
    url = reverse('users_update', kwargs={'pk': test_user1.pk})
    response = admin_client.post(url, {
        'username': test_user1.username,
        'first_name': 'new_name',
        'last_name': 'new_last',
        'password1': test_user1.password,
        'password2': test_user1.password,
    })

    assert response.status_code == 302
    assert response.url == reverse('users_index')


@pytest.mark.django_db
def test_index_view(client, test_users):
    url = reverse('users_index')
    response = client.get(url)

    assert response.status_code == 200
    assert 'users' in response.context_data
