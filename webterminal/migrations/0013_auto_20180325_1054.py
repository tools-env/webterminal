# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-25 10:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webterminal', '0012_auto_20180321_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-start_time'], 'permissions': (('can_delete', 'Can delete log info'), ('can_view', 'Can view log info'))},
        ),
        migrations.AlterField(
            model_name='credential',
            name='key',
            field=models.TextField(blank=True, verbose_name=b'Key'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='method',
            field=models.CharField(choices=[(b'password', b'password'), (b'key', b'key')], default=b'password', max_length=40, verbose_name=b'Method'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.CharField(blank=True, max_length=40, verbose_name=b'Password'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='port',
            field=models.PositiveIntegerField(default=22, verbose_name=b'Port'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='protocol',
            field=models.CharField(choices=[(b'ssh-password', b'ssh-password'), (b'ssh-key', b'ssh-key'), (b'vnc', b'vnc'), (b'rdp', b'rdp'), (b'telnet', b'telnet')], default=b'ssh-password', max_length=40, verbose_name=b'Protocol'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='proxy',
            field=models.BooleanField(default=False, verbose_name=b'Proxy'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='proxyport',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name=b'Proxy port'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='proxyserverip',
            field=models.GenericIPAddressField(blank=True, null=True, protocol=b'ipv4', verbose_name=b'Proxy ip'),
        ),
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name=b'End time'),
        ),
        migrations.AlterField(
            model_name='log',
            name='height',
            field=models.PositiveIntegerField(default=40, verbose_name=b'Height'),
        ),
        migrations.AlterField(
            model_name='log',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name=b'Is finished'),
        ),
        migrations.AlterField(
            model_name='log',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webterminal.ServerInfor', verbose_name=b'Server'),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Start time'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'User'),
        ),
        migrations.AlterField(
            model_name='log',
            name='width',
            field=models.PositiveIntegerField(default=90, verbose_name=b'Width'),
        ),
        migrations.AlterField(
            model_name='servergroup',
            name='createdatetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Create time'),
        ),
        migrations.AlterField(
            model_name='servergroup',
            name='servers',
            field=models.ManyToManyField(related_name='servers', to='webterminal.ServerInfor', verbose_name=b'Servers'),
        ),
        migrations.AlterField(
            model_name='servergroup',
            name='updatedatetime',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name=b'Update time'),
        ),
        migrations.AlterField(
            model_name='serverinfor',
            name='createdatetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Create time'),
        ),
        migrations.AlterField(
            model_name='serverinfor',
            name='ip',
            field=models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'ip'),
        ),
        migrations.AlterField(
            model_name='serverinfor',
            name='updatedatetime',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name=b'Update time'),
        ),
    ]