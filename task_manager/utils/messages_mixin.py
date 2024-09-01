from django.contrib import messages


class MsgSuccessMixin:
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
