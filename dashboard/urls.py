from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base_view, name='base'),
    path('financial/', views.financial_view, name='financial'),
    path('hr/', views.hr_view, name='hr'),
    path('rd/', views.rd_view, name='rd'),
    path('security/', views.security_view, name='security'),
    path('supply/', views.supply_view, name='supply'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)