# Generated by Django 3.2.6 on 2021-09-21 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_archivo', models.CharField(max_length=100)),
                ('Descarga_archivo', models.FileField(upload_to='archivos/')),
            ],
        ),
        migrations.DeleteModel(
            name='Files_All',
        ),
    ]