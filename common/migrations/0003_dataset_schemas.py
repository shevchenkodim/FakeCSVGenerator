# Generated by Django 3.1.4 on 2020-12-20 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20201220_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='schemas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.schemas', verbose_name='Schemas'),
            preserve_default=False,
        ),
    ]
