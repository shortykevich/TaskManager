import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home(client):
    home_url = reverse('home')
    response = client.get(home_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login(client, test_users):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(
        url,
        {'username': 'testuser1', 'password': 'testpassword'}
    )
    assert response.url == reverse('home')
    assert response.status_code == 302


@pytest.mark.django_db
def test_logout(client):
    response = client.post(reverse('logout'))
    assert response.status_code == 302
