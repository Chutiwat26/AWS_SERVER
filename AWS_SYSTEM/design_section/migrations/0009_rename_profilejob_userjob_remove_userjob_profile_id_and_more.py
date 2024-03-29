# Generated by Django 4.1.2 on 2022-10-21 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('design_section', '0008_drawingdetail_jobdrawing_jobtiltles_picturedetail_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileJob',
            new_name='UserJob',
        ),
        migrations.RemoveField(
            model_name='userjob',
            name='profile_id',
        ),
        migrations.AddField(
            model_name='userjob',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobtiltles',
            name='customer',
            field=models.IntegerField(default=0),
        ),
    ]
