from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from .views import (
    DeviceCreateView,
    DeviceDeleteView,
    DeviceRetrieveView,
    DeviceListView,
    DeviceReadingsView,
   
)

urlpatterns = [
    path('api/devices/', DeviceCreateView.as_view(), name='device-create'),
    path('api/devices/<str:uid>/', DeviceDeleteView.as_view(), name='device-delete'),
    path('api/devices/<str:uid>/', DeviceRetrieveView.as_view(), name='device-retrieve'),
    path('api/devices/', DeviceListView.as_view(), name='device-list'),
    path(
        'api/devices/<str:device_uid>/readings/<str:parameter>/',
        DeviceReadingsView.as_view(),
        name='device-readings',
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 
