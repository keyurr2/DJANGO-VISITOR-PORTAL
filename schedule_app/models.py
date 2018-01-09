from __future__ import unicode_literals

from django.db import models


class VisitorInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=10)
    person_to_meet = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    from_time = models.CharField(max_length=300)
    to_time = models.CharField(max_length=300)
    visitor_image = models.FileField(upload_to='visitors/')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.name