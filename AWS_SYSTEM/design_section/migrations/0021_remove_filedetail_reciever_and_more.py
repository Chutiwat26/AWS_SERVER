# Generated by Django 4.1.2 on 2022-10-31 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design_section', '0020_remove_filedetail_submitter_id_filedetail_reciever_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filedetail',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='filedetail',
            name='submitter',
        ),
    ]
