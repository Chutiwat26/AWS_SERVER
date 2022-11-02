# Generated by Django 4.1.1 on 2022-10-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_section', '0005_drawingfile_finish_date_drawingfile_process_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drawingfile',
            old_name='drawing_status',
            new_name='drawing1_status',
        ),
        migrations.AddField(
            model_name='drawingfile',
            name='drawing2_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='drawingfile',
            name='drawing3_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='drawingfile',
            name='drawing4_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='drawingfile',
            name='drawing5_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]