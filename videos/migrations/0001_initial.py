# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'videos_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('thumbnail', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'videos', ['Video'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'videos_video')


    models = {
        u'videos.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['videos']