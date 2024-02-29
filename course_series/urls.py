from django.urls import path

from . import views

app_name = "course_series"

urlpatterns = [
    path("course-series/test/", views.test_page, name="test_page"),
]
