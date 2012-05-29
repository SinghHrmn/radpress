from django.conf.urls import patterns, url
from radpress.views import Archive, Detail, Index, Preview

urlpatterns = patterns(
    '',

    url(r'^$',
        view=Index.as_view(),
        name='radpress-index'),

    url(r'^archives/$',
        view=Archive.as_view(),
        name='radpress-archive'),

    url(r'^detail/(?P<slug>[-\w]+)/$',
        view=Detail.as_view(),
        name='radpress-detail'),

    url(r'^preview/$',
        view=Preview.as_view(),
        name='radpress-preview'),
)