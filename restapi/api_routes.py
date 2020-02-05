from rest_framework.routers import SimpleRouter
from restapi.views import StudentOperations
simple_router = SimpleRouter()
simple_router.register("student",StudentOperations) #6 uri
urlpatterns = simple_router.urls

