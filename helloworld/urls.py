from django.urls import path

from helloworld.views import hello_user_name

app_name = 'helloworld'

urlpatterns = [
    path('', hello_user_name, name="hello_world"),
]
