# Generated by Django 2.1.7 on 2019-03-12 14:04

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_cloud', '0007_delete_hostinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField(verbose_name='帐号id')),
                ('instance_id', models.CharField(max_length=100, verbose_name='实例id')),
                ('instance_name', models.CharField(max_length=100, verbose_name='实例名称')),
                ('os_name', models.CharField(max_length=100, null=True, verbose_name='系统版本')),
                ('instance_type', models.IntegerField(choices=[(0, 'Linux'), (1, 'Windows')], null=True, verbose_name='系统类型')),
                ('instance_status', models.IntegerField(choices=[(0, '运行中'), (1, '启动中'), (2, '停止中'), (3, '已停止')], null=True, verbose_name='实例运行状态')),
                ('instance_pub_ip', models.CharField(max_length=100, null=True, verbose_name='公网ip')),
                ('instance_pri_ip', models.CharField(max_length=100, null=True, verbose_name='内网ip')),
                ('instance_vpc_ip', models.CharField(max_length=100, null=True, verbose_name='专有ip')),
                ('network_interface_id', models.CharField(max_length=100, null=True, verbose_name='弹性网卡ip')),
                ('internet_charge_type', models.IntegerField(choices=[(0, '按流量计费'), (1, '按带宽计费')], null=True, verbose_name='网络计费方式')),
                ('price_per_hour', models.CharField(max_length=50, null=True, verbose_name='每小时最高价')),
                ('instance_charge_type', models.IntegerField(choices=[(0, '包年包月'), (1, '按量付费')], null=True, verbose_name='实例计费方式')),
                ('policy_id', models.IntegerField(null=True, verbose_name='策略id')),
                ('region_id', models.IntegerField(null=True, verbose_name='地区id')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('end_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='到期时间')),
                ('last_buy_time', models.DateTimeField(null=True, verbose_name='上次续费时间')),
                ('is_overdue', models.IntegerField(choices=[(0, '使用中'), (1, '已过期'), (2, '锁定')], default=0, verbose_name='使用状态')),
                ('is_delete', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '主机资源信息',
                'db_table': 'host_info',
            },
        ),
    ]