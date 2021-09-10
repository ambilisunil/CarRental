from django.urls import path
from django.conf.urls.static import static
from.import views
urlpatterns = [
    path('',views.adm),
    path('logdis/',views.adminlogin,name='logdis'),
    path('maindis/', views.adm, name='maindis'),
    path('adminlogin/', views.l1, name='adminlogin'),


    path('userRegister/',views.register,name='userRegister'),


    path('editdetails',views.up,name='editdetails'),
    path('update',views.update,name='update'),

    path('logout/', views.logout, name='logout'),
    path('chp/', views.ch, name='chp'),

    path('ch', views.changepswd, name='ch'),
    path('list/', views.people,name='list'),
    path('list2/', views.serch,name='Serch'),
    path('feedback/', views.feedbacks, name='feedback'),
    path('userfeed/', views.feeduser, name='userfeed'),

    path('carreg/', views.carRegister, name='carreg'),
    path('cardis/', views.discar, name='cardis'),
    path('feedadmin/', views.adminfeed, name='feedadmin'),
    path('rent/', views.discarTo, name='rent'),
    path('rentcalc/', views.rentcal, name='rentcalc'),
    path('rentdis/', views.returnin, name='rentdis'),
    path('rentdisu/', views.returninu, name='rentdisu'),

    path('viewtrans/', views.distrans, name='viewtrans'),
    path('disrentadmin', views.returnind, name='disrentadmin'),
    path('distransuser/', views.distransuser, name='distransuser'),
    path('disrentuser', views.returnuser, name='disrentuser'),
    path('adminaprove/', views.adminapprove, name='adminaprove'),
    path('approvedisadmin/', views.adminupdate, name='approvedisadmin'),
    path('rentdisa/', views.rentdisa, name='rentdisa'),
    path('returnt/', views.returnd, name='returnt'),
    path('returned/', views.returncar, name='returned'),

    path('carupdate/', views.updatecar, name='carupdate'),
    path('carupdated/', views.updatecar1, name='carupdated'),
    path('carupdated/', views.updatecar1, name='carupdated'),

    path('upcr/', views.carUpdaTe, name='upcr'),
    path('dltcar/', views.dltcar, name='dltcar'),
    path('cardlt/', views.dltcar1, name='cardlt'),
    path('retadmin/', views.returnadm, name='retadmin'),
    path('abt/',views.abt,name='abt'),
    path('cnt/',views.cnt,name='cnt'),
    path('hm/',views.hm,name='hm'),

]