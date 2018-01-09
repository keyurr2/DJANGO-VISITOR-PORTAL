from django.contrib import admin
from .models import VisitorInfo
# Register your models here.

class VisitorInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('added', 'updated', )

admin.site.register(VisitorInfo, VisitorInfoAdmin)