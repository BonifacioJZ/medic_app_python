from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import permissions

 
User=get_user_model()

def is_in_group(user,group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return False

class HasGroupPermission(BasePermission):
    def has_permission(self, request, view):
        required_groups = view.permission_groups.get(view.action)
        if required_groups == None:
            return False
        elif '_Public' in required_groups:
            return True
        else:
            return any([is_in_group(request.user,group_name) for group_name in required_groups])

class IsSuperuser(BasePermission):
    message='Esta funcion solo esta permitida para el usuario root'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)

class IsUserActive(BasePermission):
    message='Este usuario no tiene accesso'
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)

class CustomObjectPermissions(permissions.DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }