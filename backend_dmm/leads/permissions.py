from rest_framework import permissions


class IsPostRequest(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method == "POST"


class IsOptionsRequest(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method == "OPTIONS"
