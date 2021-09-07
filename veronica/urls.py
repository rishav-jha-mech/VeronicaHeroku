# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve
from django.conf.urls import handler404


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('home.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'