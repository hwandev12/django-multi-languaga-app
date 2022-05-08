from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('', include('multilanguage.urls'))
)
