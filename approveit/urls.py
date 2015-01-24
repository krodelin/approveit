from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import authtoken
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
import rest

from rest.views import UserViewSet, ProjectViewSet, PersonRequestViewSet, delete_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'requests', PersonRequestViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-token-logout/', delete_auth_token),

    url(r'^', include(router.urls)),

    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += staticfiles_urlpatterns()