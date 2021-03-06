# Generated by Django 3.0.4 on 2020-03-09 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('image_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('identity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('genres_of_interest', models.TextField()),
                ('is_open_to_queries', models.BooleanField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='sets.Agency')),
            ],
        ),
    ]
