# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coupon'
        db.create_table(u'coupon_coupon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('end', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('business', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['business.Business'], null=True, blank=True)),
        ))
        db.send_create_signal(u'coupon', ['Coupon'])


    def backwards(self, orm):
        # Deleting model 'Coupon'
        db.delete_table(u'coupon_coupon')


    models = {
        u'business.business': {
            'Meta': {'object_name': 'Business'},
            'avg_wait_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'organization_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'coupon.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['business.Business']", 'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'})
        }
    }

    complete_apps = ['coupon']