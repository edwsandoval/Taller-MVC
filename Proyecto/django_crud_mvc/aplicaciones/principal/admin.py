from django.contrib import admin

from .models import persona
from .models import ciudad
from .models import tipodocumento

admin.site.register(persona)
admin.site.register(ciudad)
admin.site.register(tipodocumento)
 