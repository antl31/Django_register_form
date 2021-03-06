# Generated by Django 2.1.1 on 2018-09-10 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20180910_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='Brand',
            field=models.ForeignKey(default='brand', on_delete=django.db.models.deletion.CASCADE, to='register.Phones', to_field='Brand'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
