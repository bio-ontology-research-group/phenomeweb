# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from pvp.constants import PENDING, INHERITANCE_MODE_CHOICES


class Disease(models.Model):
    did = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=127, null=True, blank=True)
    phenotypes = ArrayField(models.CharField(max_length=15))


class Query(models.Model):
    phenotypes = ArrayField(
        models.CharField(
            max_length=15, null=True, blank=True), null=True, blank=True)
    disease = models.ForeignKey(
        Disease, related_name='queries', null=True, blank=True)
    inheritance_mode = models.CharField(
        max_length=31, choices=INHERITANCE_MODE_CHOICES)
    vcf_file = models.FileField(upload_to='pvp/%Y/%m/%d/')
    status = models.CharField(max_length=31, default=PENDING)
    date_created = models.DateTimeField(default=timezone.now)
