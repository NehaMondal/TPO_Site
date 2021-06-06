# Generated by Django 3.1.1 on 2021-06-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_App', '0011_usermarksmodel_supplees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfomodel',
            name='branch',
            field=models.CharField(choices=[('CS', 'computer_science'), ('ME', 'mechanical'), ('ELE', 'electrical'), ('ECE', 'electronics_comm'), ('IT', 'information_technology')], default='CS', max_length=10),
        ),
    ]
