# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0010_auto_20140922_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='audio_link',
            field=models.URLField(help_text='A link to an mp3 file to publish on this story', max_length=255, null=True, blank=True),
        ),
    ]
