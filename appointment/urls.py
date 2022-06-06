from django.urls  import path
from .views import home,services
urlpatterns=[
    path("", home, name="home_view"),
    path("services", services, name="services"),
]
