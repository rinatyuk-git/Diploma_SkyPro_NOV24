from rest_framework import generics

from content.serializers import DocumentSerializer
from content.models import Document
from rest_framework.permissions import IsAuthenticated
from users.permissions import (
    IsOwner,
    IsModerator
)


class DocumentCreateAPIView(generics.CreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated | ~IsModerator,)

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class DocumentListAPIView(generics.ListAPIView):
    """ Viewing List of Documents """
    serializer_class = DocumentSerializer

    # queryset = Document.objects.all()
    # permission_classes = [~IsModerator | IsOwner,]
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Document.objects.all()
        else:
            return Document.objects.filter(owner=user)


class DocumentRetrieveAPIView(generics.RetrieveAPIView):
    """ Viewing Details of Document """
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (IsModerator | IsOwner,)


class DocumentUpdateAPIView(generics.UpdateAPIView):
    """ Document Update """
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (IsModerator | IsOwner,)


class DocumentDestroyAPIView(generics.DestroyAPIView):
    queryset = Document.objects.all()
    permission_classes = (IsModerator | IsOwner,)
    # permission_classes = [~IsModerator | IsOwner]
