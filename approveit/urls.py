from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken import views
from rest.views import UserViewSet, ProjectViewSet, PersonRequestViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'requests', PersonRequestViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^', include(router.urls)),

    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += staticfiles_urlpatterns()