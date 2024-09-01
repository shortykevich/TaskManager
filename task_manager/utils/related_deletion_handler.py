from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.db.models.deletion import ProtectedError


class DeleteRelatedMixin(DeleteView):
    def form_valid(self, form):
        try:
            super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect(self.get_success_url())

        messages.success(self.request, self.success_message)
        return redirect(self.get_success_url())
