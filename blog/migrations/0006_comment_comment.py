# Generated by Django 4.2.2 on 2023-08-23 11:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
