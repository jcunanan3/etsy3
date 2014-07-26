# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Shop.price'
        db.alter_column(u'etsy3_app_shop', 'price', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Shop.title'
        db.alter_column(u'etsy3_app_shop', 'title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Shop.description'
        db.alter_column(u'etsy3_app_shop', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Shop.listing_id'
        db.alter_column(u'etsy3_app_shop', 'listing_id', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Shop.price'
        db.alter_column(u'etsy3_app_shop', 'price', self.gf('django.db.models.fields.FloatField')(default=''))

        # Changing field 'Shop.title'
        db.alter_column(u'etsy3_app_shop', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Shop.description'
        db.alter_column(u'etsy3_app_shop', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Shop.listing_id'
        db.alter_column(u'etsy3_app_shop', 'listing_id', self.gf('django.db.models.fields.IntegerField')(default=''))

    models = {
        u'etsy3_app.shop': {
            'Meta': {'object_name': 'Shop'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['etsy3_app']