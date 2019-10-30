from django.urls import path, include
from . import views
app_name='textileapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.oneitem,name='oneitem'),

    path('<int:id>/delete/', views.delete),
    path('add/', views.add, name='add'),
    path('login/', views.log, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.reg, name='register'),
    path('search/', views.search, name='search'),
    path('search/<int:id>/', views.searchitem, name='searchitem'),
    path('carts/', views.carts, name='carts'),
    path('buynow/<int:id>/', views.buynow, name='buynow'),
    # path('savebuynow/<int:id>/', views.savebuynow, name='savebuynow'),
    # path('coupon/', views.coupon, name='coupon'),
    path('deletecart/<int:id>/', views.removecart, name='deletecart'),
    # path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
]
