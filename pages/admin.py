from django.contrib import admin
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['image_tag',]
    exclude = ['image_small']

    class Meta:
        model = Review


class ServiceStepInline(admin.TabularInline):
    model = ServiceStep
    extra = 0

class ProjectAddressInline(admin.TabularInline):
    model = ProjectAddress
    extra = 0

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 0

class ServiceNameAdmin(admin.ModelAdmin):
    exclude = ['nameSlug','views']
    inlines = (ServiceStepInline,ServiceFeatureInline,)
    class Meta:
        model = Service

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    readonly_fields = ('image_tag',)
    exclude = ('image_small',)
    extra = 0

class ProjectAdmin(admin.ModelAdmin):

    exclude = ['nameSlug']
    inlines = (ProjectAddressInline,)
    class Meta:
        model = Project

class ProjectAddressAdmin(admin.ModelAdmin):

    exclude = ['nameSlug']
    inlines = (ProjectImageInline,)
    class Meta:
        model = ProjectAddress
admin.site.register(Service,ServiceNameAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Banner)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Callback)
admin.site.register(SeoTag)
admin.site.register(BlogPost)
admin.site.register(Client)
admin.site.register(Cert)
admin.site.register(ProjectAddress,ProjectAddressAdmin)
