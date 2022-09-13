from django.urls import path
from App_mtv.views import *


urlpatterns = [
    path('familia/', familia),
    path('gemelos/', hermanos),
    path('hermana/', hermana),
]
