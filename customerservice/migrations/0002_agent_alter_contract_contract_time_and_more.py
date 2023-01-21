# Generated by Django 4.0.6 on 2022-11-10 20:57

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('customerservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('role', models.CharField(choices=[('tec', 'فنی'), ('com', 'بازرگانی'), ('leg', 'حقوقی')], default='tec', max_length=3, verbose_name='نقش نماینده')),
                ('notes', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
            ],
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_time',
            field=django_jalali.db.models.jDateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='end_time',
            field=django_jalali.db.models.jDateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='start_time',
            field=django_jalali.db.models.jDateField(),
        ),
    ]