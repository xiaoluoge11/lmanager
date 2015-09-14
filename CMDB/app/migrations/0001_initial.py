# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idc'
        db.create_table(u'app_idc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idc_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'app', ['Idc'])

        # Adding model 'HostList'
        db.create_table(u'app_hostlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(unique=True, max_length=15)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('application', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bianhao', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('idc_name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['HostList'])

        # Adding model 'ServerAsset'
        db.create_table(u'app_serverasset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('productname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('service_tag', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
            ('cpu_model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cpu_nums', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('cpu_groups', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mem', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('disk', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'app', ['ServerAsset'])


    def backwards(self, orm):
        # Deleting model 'Idc'
        db.delete_table(u'app_idc')

        # Deleting model 'HostList'
        db.delete_table(u'app_hostlist')

        # Deleting model 'ServerAsset'
        db.delete_table(u'app_serverasset')


    models = {
        u'app.hostlist': {
            'Meta': {'object_name': 'HostList'},
            'application': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bianhao': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
        }
    }

    complete_apps = ['app']