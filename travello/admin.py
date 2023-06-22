from django.contrib import admin
from .models import Destination
from .models import Detailed_desc
from .models import pessanger_detail
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(Destination)
admin.site.register(Detailed_desc)
admin.site.register(pessanger_detail)


# Unregister

admin.site.unregister(Group)
