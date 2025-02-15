# Generated by Django 2.2.3 on 2019-07-31 18:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.IntegerField(choices=[(1, 'Allow Global Access'), (2, 'Read'), (3, 'Comment'), (4, 'Share')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserCreatedNerve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('members', models.ManyToManyField(related_name='NerveMembers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NervesPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('permissionList', models.ManyToManyField(related_name='Permissions', to='Nerves.PermissionModel')),
            ],
        ),
    ]
