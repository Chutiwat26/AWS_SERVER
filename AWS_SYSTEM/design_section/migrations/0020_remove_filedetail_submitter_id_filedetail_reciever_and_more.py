# Generated by Django 4.1.2 on 2022-10-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_section', '0019_filedetail_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filedetail',
            name='submitter_id',
        ),
        migrations.AddField(
            model_name='filedetail',
            name='reciever',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='filedetail',
            name='submitter',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]