from rest_framework.permissions import BasePermission



class IsYouthUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_youth)


class IsAdultUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_adult)
    
class IsModeratorUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_moderator)