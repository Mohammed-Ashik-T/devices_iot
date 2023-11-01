from django.db import models

class Device(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TemperatureReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField()

class HumidityReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField()
