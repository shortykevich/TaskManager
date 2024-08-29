import pytest


@pytest.mark.django_db
def test_user_model(test_users):
    test_user = test_users['user1']
    assert str(test_user) == 'testuser1'
