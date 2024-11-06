from rest_framework import serializers

from content.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """ Creation of Document's serializer """
    class Meta:
        model = Document
        fields = "__all__"
