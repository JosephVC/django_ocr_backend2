from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # actual admin site
    path('factory/', admin.site.urls),

    # honeypot admin site
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

]
