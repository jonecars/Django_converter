from django.urls import path
from . import views
# Paths to our views
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.back, name='back'),
    path("calc", views.calc, name="calc"),
]