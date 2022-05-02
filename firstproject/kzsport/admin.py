from django.contrib import admin

from .models import *

class TraditionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}

# Register your models here.
admin.site.register(Sportsman)
admin.site.register(City)
admin.site.register(University)
admin.site.register(Food)
admin.site.register(Tradition, TraditionsAdmin)
admin.site.register(Feedback)
admin.site.register(User)