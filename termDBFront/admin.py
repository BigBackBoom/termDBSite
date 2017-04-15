from django.contrib import admin
from django.contrib.admin import AdminSite
from django.conf.urls import url
from django.template.response import TemplateResponse
from .models import TermData
from .models import Term
from .models import Tag
from .models import Company


# Register your models here.
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    raw_id_fields = ("company_name",)


#add custom admin page to TermData admin page groups by admin.register
@admin.register(TermData)
class TermDataAdmin(admin.ModelAdmin):
    #givin url to access this custom page. it can be accessed by admin/termDBFront/$(registered.model)/######
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            #this url can be access by admin/termDBFront/termdata/my_views
            url(r'^my_view/$', self.admin_site.admin_view(self.my_view)),
        ]
        print (my_urls)
        return my_urls + urls
    
    #actual my_view Responding
    def my_view(self, request):
        #context data are taken out
        context = dict(
           self.admin_site.each_context(request),
        )
        #can be access this admin site by admin/termDBFront/termdata/my_view
        return TemplateResponse(request, "admin/termDBFront/termdata/my_view.html", context)



'''admin.site.register(Term)'''
admin.site.register(Tag)
'''admin.site.register(TermData)'''
admin.site.register(Company)

