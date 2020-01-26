# Generated by Django 3.0.2 on 2020-01-26 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houseapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='members',
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houseapp.House')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='members',
            field=models.ManyToManyField(through='houseapp.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]