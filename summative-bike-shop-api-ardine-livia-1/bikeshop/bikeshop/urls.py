from django.urls import path, include
from shop import views
from rest_framework import routers
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'bikes', views.BikeViewSet, basename='bikes'),
router.register(r'customers', views.CustomerViewSet, basename='customers'),
router.register(r'sales', views.SaleViewSet, basename='sales'),

urlpatterns = [
 
    path('', include(router.urls)),

] 
