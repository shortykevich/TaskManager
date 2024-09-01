import pytest
from django.utils import translation

from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status


@pytest.fixture(autouse=True)
def language():
    return translation.activate('ru')


@pytest.fixture
def logged_in_client(client, test_users):
    client.force_login(test_users['user1'])
    return client


@pytest.fixture
def test_users(db):
    return {
        'user1': User.objects.create_user(
            username='testuser1',
            password='testpassword',
            first_name='test',
            last_name='user',
        ),
        'user2': User.objects.create_user(
            username='testuser2',
            password='testpassword',
            first_name='test',
            last_name='user',
        )
    }


@pytest.fixture
def test_statuses(db):
    return {
        'status1': Status.objects.create(
            title="teststatus1"
        ),
        'status2': Status.objects.create(
            title="teststatus2"
        )
    }


@pytest.fixture
def test_labels(db):
    return {
        'label1': Label.objects.create(
            title="testlabel1"
        ),
        'label2': Label.objects.create(
            title="testlabel2"
        )
    }


@pytest.fixture
def test_tasks(db, test_users, test_statuses):
    test_user1, test_user2 = test_users['user1'], test_users['user2']
    test_status1, test_status2 = test_statuses['status1'], test_statuses['status2']
    return {
        'task1': Task.objects.create(
            title="testtask1",
            description="testdescription",
            author=test_user1,
            executor=test_user2,
            status=test_status1,
        ),
        'task2': Task.objects.create(
            title="testtask2",
            description="testdescription",
            author=test_user2,
            executor=test_user1,
            status=test_status2,
        )
    }


@pytest.fixture
def test_user1_data():
    return {
        'username': 'testuser1',
        'first_name': 'test',
        'last_name': 'user',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
