from django.urls import path

from . import views

urlpatterns = [
    path("get_tokens/", views.RefferCodeJsonListView.as_view(), name='get_tokens')
]