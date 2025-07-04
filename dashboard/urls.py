from django.urls import path
from . import views

urlpatterns = [
    path('api/demo/', views.DemoDataView.as_view(), name='demo_api'),
]