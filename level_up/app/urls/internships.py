from django.urls import path
from app.views import (
    InternshipListView,
    InternshipCreateView,
    InternshipUpdateView,
    InternshipDeleteView,
)

app_name = "internships"

urlpatterns = [
    path("", InternshipListView.as_view(), name="internship"),
    path("create/", InternshipCreateView.as_view(), name="create_internship"),
    path("<int:pk>/update/", InternshipUpdateView.as_view(), name="update_internship"),
    path("<int:pk>/delete/", InternshipDeleteView.as_view(), name="delete_internship"),
]