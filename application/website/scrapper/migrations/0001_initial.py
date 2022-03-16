# Generated by Django 3.1 on 2022-03-16 17:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import scrapper.models.utils.graphql_mixin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=(models.Model, scrapper.models.utils.graphql_mixin.GrapheneMixin),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('counter', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=(models.Model, scrapper.models.utils.graphql_mixin.GrapheneMixin),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('is_ready', models.BooleanField(default=False)),
                ('scraping_interval', models.CharField(choices=[('MINUTE5', 'Minute5'), ('MINUTE10', 'Minute10'), ('MINUTE15', 'Minute15'), ('MINUTE30', 'Minute30'), ('MINUTE45', 'Minute45'), ('HOUR1', 'Hour1'), ('HOUR2', 'Hour2'), ('HOUR3', 'Hour3'), ('HOUR6', 'Hour6'), ('HOUR12', 'Hour12'), ('DAY1', 'Day1'), ('DAY2', 'Day2'), ('DAY3', 'Day3'), ('DAY4', 'Day4'), ('DAY5', 'Day5'), ('DAY6', 'Day6'), ('WEEK', 'Week')], default='HOUR1', max_length=20)),
                ('last_scraping', models.DateTimeField(default=None, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=(models.Model, scrapper.models.utils.graphql_mixin.GrapheneMixin),
        ),
    ]
