# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from pvp.models import Query
from pvp.forms import QueryForm


class QueryCreateView(CreateView):

    model = Query
    form_class = QueryForm
    template_name = 'pvp/query/create.html'


class QueryResultView(DetailView):

    model = Query
    template_name = 'pvp/query/results.html'
