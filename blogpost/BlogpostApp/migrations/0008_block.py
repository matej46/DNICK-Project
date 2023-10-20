# Generated by Django 4.0.4 on 2022-06-01 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogpostApp', '0007_comment_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_user', to=settings.AUTH_USER_MODEL)),
                ('other_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
