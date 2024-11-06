from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Checking Owner role for User """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsModerator(BasePermission):
    """ Checking Moderator role """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()
