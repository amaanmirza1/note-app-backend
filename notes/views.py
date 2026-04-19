from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Note
from .serializers import NoteSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 🔥 Search + Filter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_pinned']
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Note.objects.filter(
            user=self.request.user,
            is_deleted=False
        ).order_by('-created_at')   # Latest first

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True   # Soft delete
        instance.save()