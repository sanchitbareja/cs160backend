# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Coupon.end'
        db.delete_column(u'coupon_coupon', 'end')

        # Deleting field 'Coupon.start'
        db.delete_column(u'coupon_coupon', 'start')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Coupon.end'
        raise RuntimeError("Cannot reverse this migration. 'Coupon.end' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Coupon.end'
        db.add_column(u'coupon_coupon', 'end',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Coupon.start'
        raise RuntimeError("Cannot reverse this migration. 'Coupon.start' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Coupon.start'
        db.add_column(u'coupon_coupon', 'start',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10),
                      keep_default=False)


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['coupon']