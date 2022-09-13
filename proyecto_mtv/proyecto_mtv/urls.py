from django.contrib import admin
from django.urls import path
from proyecto_mtv.views import vista_familiar1, vista_familiar2, vista_familiar3, plantilla_familiar1, plantilla_familiar2, plantilla_familiar3
from App_mtv.views import familiar_1, familiar_2, familiar_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiar1/<nombre>/<edad>/<fecha>', vista_familiar1), 
    path('familiar2/<nombre>/<edad>/<fecha>', vista_familiar2),
    path('familiar3/<nombre>/<edad>/<fecha>', vista_familiar3),
    path('familiar-1/', plantilla_familiar1),
    path('familiar-2/', plantilla_familiar2),
    path('familiar-3/', plantilla_familiar3),
    path('familiar_1/', familiar_1),
    path('familiar_2/', familiar_2),
    path('familiar_3/', familiar_3),
]