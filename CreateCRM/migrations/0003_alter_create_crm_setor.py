# Generated by Django 4.1.1 on 2022-10-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
        ('CreateCRM', '0002_create_crm_setor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_crm',
            name='setor',
            field=models.ManyToManyField(related_name='setores_crmm', to='registration.setor'),
        ),
    ]
