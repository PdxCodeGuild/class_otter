from rest_framework import permissions

# Using from rest_framework.permissions import IsAuthenticatedOrReadOnly
# So this class is no longer needed:
class IsLoggedInOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        

        # print("request.user: ", request.user)
        # # request.user:  AnonymousUser
        # print("request.user == 'AnonymousUser': ", request.user == 'AnonymousUser')
        # # request.user == 'AnonymousUser':  False

        print("request.method in permissions.SAFE_METHODS: ", request.method in permissions.SAFE_METHODS)

        print("request.user.is_authenticated: ", request.user.is_authenticated)

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_authenticated