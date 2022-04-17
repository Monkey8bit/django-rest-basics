from django.contrib import admin
from django.urls import path, include

from .views import ProjectView, SingleProjectView, NoteView, SingleNoteView

app_name = "projects"

urlpatterns = [
    path("", ProjectView.as_view()),
    path("<int:project_id>/", NoteView.as_view()),
    path("<int:project_id>/<int:note_id>", SingleNoteView.as_view())
]