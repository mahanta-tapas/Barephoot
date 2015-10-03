from django.contrib import admin
from barephoot.models import Movdata
from  barephoot.models import Restdata
from barephoot.models import Events
from barephoot.models import PlacestoVisit
# Register your models here.

admin.site.register(Movdata)
admin.site.register(Restdata)
admin.site.register(Events)
admin.site.register(PlacestoVisit)