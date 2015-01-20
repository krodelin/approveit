from django.conf.urls import url, include
from django.contrib import admin
from rest import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'requests', views.PersonRequestViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]