"""Project OC DAP 12 - Permissions file."""

from rest_framework import permissions

class AllowedActionsAccount(permissions.BasePermission):
    """Permission that allow only specific actions for account application."""

    message = "This operation is not allowed."

    def has_permission(self, request, view):
        """Check the permission."""
        if view.action in ["list", "create", "retrieve", "partial_update", "destroy"]:
            return True

        return False

class IsManagement(permissions.BasePermission):
    """Permission checking if the user is part of the management team."""

    message = "You must be part of management team for this operation."

    def has_permission(self, request, view):
        """Check the object permission."""
        return request.user.StaffProfileID.Name == "Gestion"


class AllowedActionsClient(permissions.BasePermission):
    """Permission that allow only specific actions for client application."""

    message = "This operation is not allowed."

    def has_permission(self, request, view):
        """Check the permission."""
        if view.action in ["list", "create", "retrieve", "partial_update", 
        "change_status"]:
            return True

        return False

class IsSale(permissions.BasePermission):
    """Permission checking if the user is part of the sales team."""

    message = "You must be part of sales team for this operation."

    def has_permission(self, request, view):
        """Check the object permission."""
        if view.action in ["create"]:
            return request.user.StaffProfileID.Name == "Vente"

        return True

class IsStaffContact(permissions.BasePermission):
    """Permission checking if the staff contact."""

    message = "You must be the sales contact for this operation."

    def has_permission(self, request, view):
        """Check the object permission."""
        if view.action in ["change_status"]:
            return request.user.StaffProfileID.Name == "Vente"

        return True

    def has_object_permission(self, request, view, obj):
        """Check the object permission."""
        if view.action in ["change_status"]:
            return request.user in obj.get_staff_contact()

        return True


class IsStaffContactOrManagement(permissions.BasePermission):
    """Permission checking if the staff contact or part of the management team."""

    message = "You must be the staff contact of this project or from management team."

    def has_permission(self, request, view):
        """Check the permission."""
        if view.action in ["partial_update"]:
            profile_name = request.user.StaffProfileID.Name
            return profile_name in ["Vente", "Gestion", "Support"]

        return True

    def has_object_permission(self, request, view, obj):
        """Check the object permission."""
        if view.action in ["partial_update"]:
            if request.user.StaffProfileID.Name in ["Vente", "Support"]:
                return request.user in obj.get_staff_contact()

        return True

class AllowedActionsContract(permissions.BasePermission):
    """Permission that allow only specific actions for contract application."""

    message = "This operation is not allowed."

    def has_permission(self, request, view):
        """Check the permission."""
        if view.action in ["list", "create", "retrieve", "partial_update", 
        "change_status", 'events']:
            return True

        return False

class AllowedActionsEvent(permissions.BasePermission):
    """Permission that allow only specific actions for event application."""

    message = "This operation is not allowed."

    def has_permission(self, request, view):
        """Check the permission."""
        if view.action in ["list", "create", "retrieve", "partial_update"]:
            return True

        return False