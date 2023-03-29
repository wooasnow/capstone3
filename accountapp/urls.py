from django.urls import path

from accountapp.views import hello_world, AccountView

app_name="accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/',AccountView.as_view(),name='create'),
]