from django.contrib import messages
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError


class DeleteOneToManyMixin:
    def form_valid(self, form):
        try:
            super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect(self.get_success_url())

        messages.success(self.request, self.success_message)
        return redirect(self.get_success_url())


class DeleteManyToManyMixin(DeleteOneToManyMixin):
    def form_valid(self, form):
        if self.object.task_labels.exists():
            messages.error(self.request, self.error_message)
            return redirect(self.get_success_url())
        return super().form_valid(form)
