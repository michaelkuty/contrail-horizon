# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 NEC Corporation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls import include  # noqa
from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from contrail_openstack_dashboard.openstack_dashboard.dashboards.admin.networking \
    import views

from contrail_openstack_dashboard.openstack_dashboard.dashboards.admin.networking.subnets \
    import urls as subnet_urls
from contrail_openstack_dashboard.openstack_dashboard.dashboards.admin.networking.subnets \
    import views as subnet_views

from contrail_openstack_dashboard.openstack_dashboard.dashboards.admin.networking.ports \
    import urls as port_urls
from contrail_openstack_dashboard.openstack_dashboard.dashboards.admin.networking.ports \
    import views as port_views


NETWORKS = r'^(?P<network_id>[^/]+)/%s$'


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(NETWORKS % 'update', views.UpdateView.as_view(), name='update'),
    # for detail view
    url(NETWORKS % 'detail', views.DetailView.as_view(), name='detail'),
    url(NETWORKS % 'subnets/create',
        subnet_views.CreateView.as_view(), name='addsubnet'),
    url(NETWORKS % 'ports/create',
        port_views.CreateView.as_view(), name='addport'),
    url(r'^(?P<network_id>[^/]+)/subnets/(?P<subnet_id>[^/]+)/update$',
        subnet_views.UpdateView.as_view(), name='editsubnet'),
    url(r'^(?P<network_id>[^/]+)/ports/(?P<port_id>[^/]+)/update$',
        port_views.UpdateView.as_view(), name='editport'),

    url(r'^subnets/', include(subnet_urls, namespace='subnets')),
    url(r'^ports/', include(port_urls, namespace='ports')))
