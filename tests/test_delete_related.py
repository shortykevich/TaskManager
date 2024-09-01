from django.urls import reverse


def test_delete_related(logged_in_client, test_tasks, test_users, test_statuses):
    url = reverse('statuses_delete', kwargs={'pk': test_statuses['status1'].pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('statuses_index')

    url = reverse('users_delete', kwargs={'pk': test_users['user1'].pk})
    response = logged_in_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('users_index')
