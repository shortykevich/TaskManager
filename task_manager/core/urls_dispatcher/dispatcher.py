from django.urls import path


def generate_crud_urls(view_module, base_name):
    return [
        path(
            '',
            getattr(view_module, f'{base_name.capitalize()}IndexView').as_view(),
            name=f'{base_name}_index'
        ),
        path(
            'create/',
            getattr(view_module, f'{base_name.capitalize()}CreateView').as_view(),
            name=f'{base_name}_create'
        ),
        path(
            '<int:pk>/update/',
            getattr(view_module, f'{base_name.capitalize()}UpdateView').as_view(),
            name=f'{base_name}_update'
        ),
        path(
            '<int:pk>/delete/',
            getattr(view_module,
                    f'{base_name.capitalize()}DeleteView').as_view(),
            name=f'{base_name}_delete'
        ),
    ]
