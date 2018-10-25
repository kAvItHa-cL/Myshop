from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.product_list,name='product_list'),
    url(r'^(?p<category_slug>[-\W+)/$', views.product_list, name='product_list_by_cateogry'),
    url(r'^(?p<id>\d+)/(?p<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
    ]