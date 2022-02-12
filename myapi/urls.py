from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'14feb', views.YasherkaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Pashalkaone/', views.PashalkaoneCreate.as_view(), name='Pashalkaone'),
    path('Pashalkatwo/', views.PashalkatwoCreate.as_view(), name='Pashalkatwo'),

]