# Generated by Django 4.0.3 on 2022-03-22 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='invite_code_incerted',
            new_name='invite_code_list',
        ),
        migrations.AddField(
            model_name='user',
            name='invite_code_incerd',
            field=models.CharField(blank=True, max_length=11, verbose_name='введенный пригласительный код'),
        ),
        migrations.AlterField(
            model_name='invitecode',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец кода'),
        ),
    ]