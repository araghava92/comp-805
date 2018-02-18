from django.contrib import admin

from .models import Education, Experience

# Registering Education and Experience models with admin panel
admin.site.register(Education)
admin.site.register(Experience)
