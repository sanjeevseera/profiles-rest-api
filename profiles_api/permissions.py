from rest_framework import permissions

class UpdateOwnProfilePermissions(permissions.BasePermission):
    """Allow user to create own permissions"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
