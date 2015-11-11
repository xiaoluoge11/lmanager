from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from app.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CMDB.views.home', name='home'),
    # url(r'^CMDB/', include('CMDB.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^index/$',index),
    (r'^$',login),
    (r'^login/$',login),
    (r'^idc/$',idc),
    (r'^addidc/$',addidc),
    (r'^idc/idc_delete/$',idc_delete),
    (r'^mac/$',mac),
    (r'^addmac/$',addmac),
    (r'^mac/mac_delete/$',mac_delete),
    (r'^mac/mac_edit/$',mac_edit),
    (r'^macresult/$',macresult),
    (r'^group/$',group),
    (r'^group_result/$',group_result),
    (r'^group/group_delete/$',group_delete),
    (r'^group_manage/$',group_manage),
    (r'^group_manage/group_manage_delete/$',group_manage_delete), 
    (r'addgroup_host/$',addgroup_host),
    (r'^file/$',file),
    (r'^file_result',file_result),
    (r'^command/$',command),
    (r'^command_group/$',command_group),
    (r'^command_group/check_result/$',check_result),
    (r'^command_group_result/$',command_group_result), 
    (r'^command_result/$',command_result),
    (r'^job/$',job),
    (r'^asset/$',asset),
    (r'^asset_auto/$',asset_auto),
    (r'^asset_auto_result/$',asset_auto_result),
    (r'asset/asset_delete/$',asset_delete),
    (r'^authin/$',authin),
    (r'accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^monitor/$',monitor),
    (r'^data/$',getdata),
    (r'monitor_result/$',monitor_result),
    (r'monitor_data/$',monitor_data), 
)
