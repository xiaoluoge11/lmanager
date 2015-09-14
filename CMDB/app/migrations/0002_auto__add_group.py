# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'app_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'app', ['Group'])

        # Adding M2M table for field group on 'HostList'
        m2m_table_name = db.shorten_name(u'app_hostlist_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hostlist', models.ForeignKey(orm[u'app.hostlist'], null=False)),
            ('group', models.ForeignKey(orm[u'app.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hostlist_id', 'group_id'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'app_group')

        # Removing M2M table for field group on 'HostList'
        db.delete_table(db.shorten_name(u'app_hostlist_group'))


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
        }
    }

    complete_apps = ['app']