from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView

from .models import Project, Note
from .serializers import ProjectModelSerializer, NoteModelSerializer


class ProjectView(ListAPIView, CreateAPIView):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()


class SingleProjectView(CreateAPIView, UpdateAPIView, RetrieveAPIView):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    lookup_field = "project_id"


class NoteView(ListAPIView, CreateAPIView, UpdateAPIView):
    serializer_class = NoteModelSerializer

    def get_queryset(self):
        return Note.objects.filter(project=self.kwargs["project_id"])

    def perform_create(self, serializer):
        print(serializer)
        project = Project.objects.get(project_id=self.kwargs["project_id"])
        serializer.save(project=project)


class SingleNoteView(CreateAPIView, UpdateAPIView, RetrieveAPIView):
    serializer_class = NoteModelSerializer
    lookup_field = "note_id"

    def get_queryset(self):
        return Note.objects.filter(note_id=self.kwargs["note_id"])
