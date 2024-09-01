import pytest
from django.utils.translation import gettext_lazy as _

from tests import get_response_message
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
    assert _('User created successfully!') == get_response_message(response)


@pytest.mark.django_db
def test_users_update_get(client, test_users):
    url = reverse('users_update', kwargs={'pk': test_users['user1'].pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)

    client.force_login(test_users['user2'])
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse('users_index')
    assert _('You are not authorized to access this page.') == get_response_message(response)

    client.force_login(test_users['user1'])
    response = client.get(url)

    assert response.status_code == 200
    assert 'users/update.html' in response.template_name
    assert _('You are not authorized to access this page.') == get_response_message(response)


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
    assert _('User updated successfully!') == get_response_message(response)


@pytest.mark.django_db
def test_users_index_get(client, test_users):
    url = reverse('users_index')
    response = client.get(url)

    assert response.status_code == 200
    assert 'users' in response.context_data
