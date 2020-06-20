# Generated by Django 3.0.5 on 2020-06-20 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_auto_20200619_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('amount', models.IntegerField()),
                ('dueDate', models.DateField(verbose_name='Due Date')),
                ('category', models.CharField(choices=[('MC', 'Miscellaneous'), ('MO', 'Mortgage'), ('RE', 'Rent'), ('EN', 'Entertainment'), ('UT', 'Utilities'), ('IN', 'Insurance'), ('CC', 'Credit Cards'), ('LO', 'Loans')], default='MC', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
