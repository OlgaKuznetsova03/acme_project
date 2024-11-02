from django.contrib import admin

from .models import Birthday

class BirthdayAdmin(admin.ModelAdmin): 
    list_display = ( 
        'first_name', 
        'last_name', 
        'birthday',
    ) 
    list_editable = ( 
        'birthday', 
    ) 
    search_fields = ('first_name',) 
    list_filter = ('first_name',) 
    list_display_links = ('first_name',) 
    empty_value_display = 'Не задано'


admin.site.register(Birthday, BirthdayAdmin)
