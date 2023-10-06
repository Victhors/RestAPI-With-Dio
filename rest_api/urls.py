from rest_framework.routers import SimpleRouter
from rest_api.views import RegisteModelViewSet
from django.urls import path

app_name =  'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('register',RegisteModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls