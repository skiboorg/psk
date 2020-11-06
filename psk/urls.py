from django.contrib import admin
from django.urls import path, include
import psk.settings
from django.conf.urls.static import static
#from pages.sitemaps import *
# from django.contrib.sitemaps.views import sitemap

admin.site.site_header = "PSK"
admin.site.site_title = "PSK администрирование"
admin.site.index_title = "PSK администрирование"

# sitemaps = {
#     'static': StaticViewSitemap,
#     'services': ServicesSitemap,
#     'posts': BlogSitemap,
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('', include('pages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(psk.settings.MEDIA_URL, document_root=psk.settings.MEDIA_ROOT)
