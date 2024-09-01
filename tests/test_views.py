import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home(client):
    home_url = reverse('home')
    response = client.get(home_url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_login(client, test_users):
    test_user = test_users['user1']
    url = reverse('login')
    response = client.get(url)

    assert response.status_code == 200

    response = client.post(
        url,
        {'username': test_user.username, 'password': 'testpassword'}
    )

    assert response.status_code == 302
    assert response.url == reverse('home')
    assert test_user.is_authenticated


@pytest.mark.django_db
def test_logout(client):
    response = client.post(reverse('logout'))

    assert response.status_code == 302
    assert response.url == reverse('home')
