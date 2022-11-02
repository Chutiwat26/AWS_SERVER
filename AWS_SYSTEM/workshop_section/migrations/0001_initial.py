# Generated by Django 4.1.1 on 2022-10-13 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('design_section', '0007_drawingfile_drawing1_name_drawingfile_drawing2_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='design_section.drawingfile')),
            ],
        ),
    ]
