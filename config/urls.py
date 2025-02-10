from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import  DefaultRouter
from alunos.views import AlunoViewSet

router = DefaultRouter()
router.register(r"Alunos", AlunoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
