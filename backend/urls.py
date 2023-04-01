from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bapz import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'bapz', views.BapzView, 'bapz')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bapz', views.BapzView.as_view()), 
    path('api/bapz/id', views.BapzId), 
    path('api/bapz/apparel', views.BapzCatView ),
    path('api/bapz/product', views.BapzProduct ), 
    path('api/customer', views.GetCustomer),
    path('api/customer/commands', views.UpdateCommands),
    path('api/customer/token', views.getUserCommandsByJwt),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
