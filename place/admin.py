from django.contrib import admin
from .models import Place, BucketList

# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "location")
    prepopulated_fields = {"slug": ("name",)}

class BucketListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Place, PlaceAdmin)
admin.site.register(BucketList, BucketListAdmin)