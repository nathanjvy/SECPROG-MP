from django.conf.urls import url
from . import views
from django.views.defaults import page_not_found
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^shop$', views.shop, name='shop'),
    url(r'^shop/analog$', views.shopAnalog, name='shopA'),
    url(r'^shop/digital$', views.shopDigital, name='shopD'),
    url(r'^shop/smart$', views.shopSmart, name='shopS'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login$',views.login, name='login'),
    url(r'^signup$',views.register,name='signup'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^adminpage$',views.admin,name='adminPage'),
    url(r'^prodmanagement$',views.productManagement,name='prod'),
    url(r'^prodmanagement/edit/(?P<id>[0-9]+)$',views.productManagementEdit,name='prodEdit'),
    url(r'^prodmanagement/add$',views.addItem,name='add'),
    url(r'^shop/viewitem/(?P<id>[0-9]+)$',views.productDetails,name='productDetail'),
    url(r'^userprofile/(?P<user_id>[0-9]+)$', views.userProfile, name='userprofile'),
    url(r'^userprofile/edit/(?P<user_id>[0-9]+)$', views.editProfile, name='editprofile'),
    url(r'^cart/(?P<user_id>[0-9]+)$', views.cart, name='cart'),
    url(r'^review/(?P<item_id>[0-9]+)$', views.review, name='review'),
    url(r'^history$',views.history,name='history'),
    url(r'^accounting$',views.accounting,name='accounting'),
    url(r'^resetaccount$',views.resetaccount,name='reset'),
]
