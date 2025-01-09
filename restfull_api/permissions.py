from rest_framework import permissions

class UpdateOwnPermission(permissions.BasePermission):
    """Allow users to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow users to edit their own post status"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own post status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.post.id == request.user.id