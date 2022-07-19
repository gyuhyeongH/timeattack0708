from rest_framework.permissions import BasePermission


class IsCandidateUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.user_type.user_type == "candidate"

