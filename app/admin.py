from django.contrib import admin
from .models import dictionary

# Register your models here.
class dictionaryAdmin(admin.ModelAdmin):
    list_display = ('question','answer','created')
    list_filter = ('created',)
    exclude = ('usage',)

admin.site.register(dictionary,dictionaryAdmin)