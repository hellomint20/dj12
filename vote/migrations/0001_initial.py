# Generated by Django 4.1.3 on 2022-12-28 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maker', to=settings.AUTH_USER_MODEL)),
                ('voter', models.ManyToManyField(blank=True, related_name='voter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('choicer', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('top', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.topic')),
            ],
        ),
    ]
