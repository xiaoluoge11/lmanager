# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'app_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headImg', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'app_user')


    models = {
        u'app.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'app.hostlist': {
            'Meta': {'object_name': 'HostList'},
            'application': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bianhao': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['app.Group']", 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'app.idc': {
            'Meta': {'object_name': 'Idc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'app.serverasset': {
            'Meta': {'object_name': 'ServerAsset'},
            'cpu_groups': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'cpu_model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cpu_nums': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'disk': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mem': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'productname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'service_tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'app.user': {
            'Meta': {'object_name': 'User'},
            'headImg': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']