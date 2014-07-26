# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shop'
        db.create_table(u'etsy3_app_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('listing_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'etsy3_app', ['Shop'])


    def backwards(self, orm):
        # Deleting model 'Shop'
        db.delete_table(u'etsy3_app_shop')


    models = {
        u'etsy3_app.shop': {
            'Meta': {'object_name': 'Shop'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_id': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['etsy3_app']