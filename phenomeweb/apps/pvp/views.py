# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse

from pvp.models import Query
from pvp.forms import QueryForm


class QueryCreateView(CreateView):

    model = Query
    form_class = QueryForm
    template_name = 'pvp/query/create.html'

    def get_success_url(self):
        return reverse('query-result', kwargs={'pk': self.object.pk})


class QueryResultView(DetailView):

    model = Query
    template_name = 'pvp/query/results.html'
