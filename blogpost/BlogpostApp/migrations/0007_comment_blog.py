# Generated by Django 4.0.4 on 2022-05-31 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogpostApp', '0006_alter_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogpostApp.blogpost'),
        ),
    ]
