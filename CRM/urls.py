from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('crmlist/', include('CRMlist.urls')),
    path('registration/', include('registration.urls')),
    path('createcrm/', include('CreateCRM.urls')),
    path('', include('homepage.urls')),
    path('login/', include('Login.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^download/(?P<path>.*)$',serve,{'documento_root':settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



#re_path(r'^download/(?P<path>.*)$',serve,{'documento_root':settings.MEDIA_ROOT}),