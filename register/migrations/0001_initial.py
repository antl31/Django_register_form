# Generated by Django 2.1.1 on 2018-09-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]