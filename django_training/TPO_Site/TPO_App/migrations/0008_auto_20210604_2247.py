# Generated by Django 3.1.1 on 2021-06-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_App', '0007_auto_20210604_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfomodel',
            name='alternate_gmail',
            field=models.EmailField(max_length=254),
        ),
    ]