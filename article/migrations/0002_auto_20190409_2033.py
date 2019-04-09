# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimg',
            name='link',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name='\u56fe\u7247\u5916\u94fe', blank=True),
        ),
        migrations.AlterField(
            model_name='carouselimg',
            name='path',
            field=models.CharField(max_length=255, verbose_name='\u56fe\u7247\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='links',
            name='avatar',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u7f51\u7ad9\u56fe\u6807', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.CharField(max_length=255, verbose_name='\u7f51\u7ad9\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.CharField(max_length=255, verbose_name='\u97f3\u4e50\u5c01\u9762'),
        ),
        migrations.AlterField(
            model_name='music',
            name='lrc',
            field=models.CharField(default=b'', max_length=1000, null=True, verbose_name='\u97f3\u4e50\u6b4c\u8bcd', blank=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='url',
            field=models.CharField(max_length=255, verbose_name='\u97f3\u4e50\u5730\u5740'),
        ),
    ]
