from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('batken/', batken, name='batken'),
    path('chuy/', chuy, name='chuy'),
    path('jalal_abad/', jalal_abad, name='jalal_abad'),
    path('naryn/', naryn, name='naryn'),
    path('osh/', osh, name='osh'),
    path('talas/', talas, name='talas'),
    path('ysyk_kol/', ysyk_kol, name='ysyk_kol'),

    #РАЙОНЫ

    path('batken/raiony/', r_batken, name='b_raion'),
    path('chuy/raiony/', r_chuy, name='ch_raion'),
]

