from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from tests import get_response_message


def test_o2m_delete_related(logged_in_client, test_tasks, test_users, test_statuses):
    url = reverse('statuses_delete', kwargs={'pk': test_statuses['status1'].pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('statuses_index')
    assert _('Cannot delete a status because it is in use') == get_response_message(response)

    url = reverse('users_delete', kwargs={'pk': test_users['user1'].pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('users_index')
    assert _('Cannot delete a user because it is in use') == get_response_message(response)


def test_m2m_delete_related(logged_in_client, test_tasks, test_users, test_statuses, test_labels):
    url = reverse('labels_delete', kwargs={'pk': test_labels['label1'].pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('labels_index')
    assert _('Your label has been deleted.') == get_response_message(response)

    test_task = test_tasks['task1']
    test_task.labels.add(test_labels['label2'])

    url = reverse('labels_delete', kwargs={'pk': test_labels['label2'].pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('labels_index')
    assert _('Cannot delete a label because it is in use') == get_response_message(response)
