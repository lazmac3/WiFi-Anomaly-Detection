from django.contrib import admin

# Register your models here.
from .models import Prediction
from .models import Attack
admin.site.register(Prediction)
admin.site.register(Attack)
