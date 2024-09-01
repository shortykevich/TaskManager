import pytest
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from tests import get_response_message


@pytest.mark.django_db
def test_labels_permissions(client, test_labels, test_users):
    response = client.get(reverse('labels_index'))

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)

    url = reverse('labels_create')
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)

    url = reverse('labels_update', kwargs={'pk': test_labels['label1'].pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)

    url = reverse('labels_delete', kwargs={'pk': test_labels['label1'].pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert _('You are not authenticated! Please login.') == get_response_message(response)


@pytest.mark.django_db
def test_labels_index_get(client, test_users):
    client.force_login(test_users['user1'])
    response = client.get(reverse('labels_index'))

    assert response.status_code == 200
    assert 'labels/index.html' in response.template_name


@pytest.mark.django_db
def test_labels_create_get(client, test_users):
    client.force_login(test_users['user1'])
    response = client.get(reverse('labels_create'))

    assert response.status_code == 200
    assert 'labels/create.html' in response.template_name


@pytest.mark.django_db
def test_labels_create_post(logged_in_client, test_users):
    url = reverse('labels_create')
    response = logged_in_client.post(url, {'title': 'title'})

    assert response.status_code == 302
    assert response.url == reverse('labels_index')
    assert _('Your label has been created.') == get_response_message(response)
    assert Label.objects.filter(title='title').exists()


@pytest.mark.django_db
def test_labels_update_get(client, test_labels, test_users):
    test_label = test_labels['label1']
    test_user = test_users['user1']
    url = reverse('labels_update', kwargs={'pk': test_label.pk})

    client.force_login(test_user)
    response = client.get(url)

    assert response.status_code == 200
    assert 'labels/update.html' in response.template_name


@pytest.mark.django_db
def test_labels_update_post(logged_in_client, test_labels, test_users):
    url = reverse('labels_update', kwargs={'pk': test_labels['label1'].pk})
    response = logged_in_client.post(url, {'title': 'title'})

    assert response.status_code == 302
    assert response.url == reverse('labels_index')
    assert _('Your label has been updated.') == get_response_message(response)
    assert Label.objects.filter(title='title').exists()


@pytest.mark.django_db
def test_labels_delete_get(client, test_labels, test_users):
    test_label = test_labels['label1']
    test_user = test_users['user1']
    url = reverse('labels_delete', kwargs={'pk': test_label.pk})

    client.force_login(test_user)
    response = client.get(url)

    assert response.status_code == 200
    assert 'labels/delete.html' in response.template_name


@pytest.mark.django_db
def test_labels_delete_post(logged_in_client, test_labels, test_users):
    test_label = test_labels['label1']
    url = reverse('labels_delete', kwargs={'pk': test_label.pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('labels_index')
    assert _('Your label has been deleted.') == get_response_message(response)
