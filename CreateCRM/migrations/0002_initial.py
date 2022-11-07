# Generated by Django 4.1.1 on 2022-11-07 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0001_initial'),
        ('CreateCRM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_crm',
            name='setor',
            field=models.ManyToManyField(related_name='setores_crm', to='registration.setor'),
        ),
        migrations.AddField(
            model_name='create_crm',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='create_crm',
            unique_together={('id', 'versao')},
        ),
    ]