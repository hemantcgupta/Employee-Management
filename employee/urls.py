from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, signup, login

# Register the Employee ViewSet
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('', include(router.urls)),  # Include all routes registered with the router
]
