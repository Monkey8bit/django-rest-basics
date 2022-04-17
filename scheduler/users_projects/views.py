from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .models import Project, Note
from .serializers import ProjectModelSerializer, NoteModelSerializer


class NoteFilter(filters.FilterSet):
    is_active = filters.BooleanFilter()
    created = filters.DateFromToRangeFilter()


class ProjectFilter(filters.FilterSet):
    project_name = filters.CharFilter(field_name="name", lookup_expr="contains")


class NoteLimitOffset(LimitOffsetPagination):
    default_limit = 20


class ProjectLimitOffset(LimitOffsetPagination):
    default_limit = 10


class ProjectView(ListAPIView, CreateAPIView):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffset
    filterset_class = ProjectFilter
    filter_backends = [filters.DjangoFilterBackend]


class SingleProjectView(CreateAPIView, UpdateAPIView, RetrieveAPIView):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    lookup_field = "project_id"


class NoteView(ListAPIView, CreateAPIView, UpdateAPIView):
    serializer_class = NoteModelSerializer
    pagination_class = NoteLimitOffset
    filterset_class = NoteFilter
    filter_backends = [filters.DjangoFilterBackend]

    def get_queryset(self):
        return Note.objects.filter(project=self.kwargs["project_id"])

    def perform_create(self, serializer):
        print(serializer)
        project = Project.objects.get(project_id=self.kwargs["project_id"])
        serializer.save(project=project)


class SingleNoteView(CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView):
    serializer_class = NoteModelSerializer
    lookup_field = "note_id"

    def get_queryset(self):
        return Note.objects.filter(note_id=self.kwargs["note_id"])

    def delete(self, request, *args, **kwargs):
        note = self.get_object()
        note.is_active = False
        note.save()
        return Response(f"Task '{note.name}' closed.")
