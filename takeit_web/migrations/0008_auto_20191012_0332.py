# Generated by Django 2.2.4 on 2019-10-12 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takeit_web', '0007_auto_20191012_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='order',
            name='orderer_request',
            field=models.CharField(blank=True, help_text='고객님 요청사항', max_length=500),
        ),
    ]