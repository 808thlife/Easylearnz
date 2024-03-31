from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("<str:title>", views.course_view, name = "course_view")
]