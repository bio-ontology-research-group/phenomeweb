# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

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

    def get_context_data(self, **kwargs):
        context = super(QueryCreateView, self).get_context_data(**kwargs)
        context['section'] = "pvp"
        return context


class QueryResultView(DetailView):

    model = Query
    template_name = 'pvp/query/results.html'

    def get_context_data(self, **kwargs):
        context = super(QueryResultView, self).get_context_data(**kwargs)
        context['section'] = "pvp"
        results = list()
        res = self.get_object()
        res_path = res.vcf_file.path + '.res'
        if os.path.exists(res_path):
            f = open(res_path, 'r')
            lines = 0
            for line in f:
                lines += 1
                if lines > 20:
                    break
                items = line.strip().split('\t')
                results.append(items)
        context['results'] = results
        return context
