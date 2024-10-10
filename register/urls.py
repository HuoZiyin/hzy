from django.urls import path

from register.views import index, register_name_password

urlpatterns = [

    path("", index, name="index"),
    path("name_password/", register_name_password),

]
