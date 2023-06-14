from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.admin import OTPAdminSite
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap 

sitemaps = {
    'static': StaticViewSitemap
}

from home import views

class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name="OTPAdmin")

admin_site.register(User)
admin_site.register(TOTPDevice)

urlpatterns = [
    path('django_admin/', admin.site.urls),
    path('admin/', admin_site.urls),

    path('', include('home.urls', namespace='home')),
    # path('about', views.about, name='about'),
    path('windshild/', views.service, name='windshild'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),

    path('windshild/<slug:slug>', views.service_detail, name='service_detail'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots.txt', include('robots.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
