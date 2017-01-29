from django.contrib import admin
from django.conf.urls import url
from .models import TermData
from .models import Term
from .models import Tag
from .models import Company


# Register your models here.
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    raw_id_fields = ("company_name",)

'''@admin.register(TermData)
class TermDataAdmin(admin.ModelAdmin):
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'^my_view/$', self.admin_site.admin_view(self.my_view)),
        ]
        
        return my_urls + urls

    def my_view(self, request):
        
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/termDBFront/termdata/admin_editor.html", context)
'''
    
'''admin.site.register(Term)'''
admin.site.register(Tag)
admin.site.register(TermData)
admin.site.register(Company)

