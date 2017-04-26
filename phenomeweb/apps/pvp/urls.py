from django.conf.urls import url
from pvp.views import QueryCreateView, QueryResultView

urlpatterns = [
    url(r'^$', QueryCreateView.as_view(), name='create-query'),
    url(r'^view/(?P<pk>\d+)/$',
        QueryResultView.as_view(), name='query-result')
]
