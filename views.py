from django.shortcuts import render
from rest_framework import generics
from .models import Device, TemperatureReading, HumidityReading
from .serializers import DeviceSerializer, TemperatureReadingSerializer, HumidityReadingSerializer
from django.shortcuts import render



# Other view functions in your views.py


# Other view functions in your views.py



class DeviceCreateView(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDeleteView(generics.DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'uid'

class DeviceRetrieveView(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'uid'

class DeviceListView(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceReadingsView(generics.ListAPIView):
    def get_queryset(self):
        device_uid = self.kwargs['device_uid']
        parameter = self.kwargs['parameter']
        start_on = self.request.query_params.GET('start_on')
        end_on = self.request.query_params.GET('end_on')



        if parameter == 'temperature':
            queryset = TemperatureReading.objects.filter(
                device__uid=device_uid, timestamp__range=(start_on, end_on)
            )
        elif parameter == 'humidity':
            queryset = HumidityReading.objects.filter(
                device__uid=device_uid, timestamp__range=(start_on, end_on)
            )
        else:
            queryset = None

        return queryset

    serializer_class = TemperatureReadingSerializer  # You can use a separate serializer for humidity if needed

def device_graph_view(request, device_uid):
    # Pass the device UID to the template
    return render(request, 'devices_graph.html', {'deviceUid': device_uid})
def device_graph(request):
    return render(request, 'device_graph.html')
def view(request):
    return render(request,'index.html')