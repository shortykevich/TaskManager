from django.contrib.messages import get_messages


def get_response_message(response):
    """Get the last message in queue"""
    return str(
        list(get_messages(response.wsgi_request))[-1]
    )
