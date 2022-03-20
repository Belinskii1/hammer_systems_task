from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import get_confirmation_code

router_v1 = DefaultRouter()

app_name = 'api'

v1_auth_patterns = [
    path('signup/', get_confirmation_code)
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(v1_auth_patterns)),
]
