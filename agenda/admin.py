from agenda.models import Person, Group
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    # Autofill slugs
    #prepopulated_fields = {"slug": ("nickname")}
    list_display = ('name', 'surname', 'phone', 'email', 'website',  'birthday', 'nickname')
    list_filter = ['name', 'surname', 'birthday', 'nickname']
    search_fields = ['name', 'surname', 'nickname']

    # TinyMCE
    #class Media:
        #js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)