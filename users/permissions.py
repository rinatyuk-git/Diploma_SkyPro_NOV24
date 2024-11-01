from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Checking Owner role for User """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
