# Generated by Django 4.0.6 on 2022-11-20 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerservice', '0004_contract_state_alter_customer_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='kind',
            field=models.CharField(choices=[('عادی', 'عادی'), ('ویژه', 'ویژه')], default='عادی', max_length=4, verbose_name='نوع'),
        ),
        migrations.CreateModel(
            name='Wireless',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popsite', models.CharField(choices=[('بوتان', 'بوتان'), ('شریعتی', 'شریعتی'), ('زرین', 'زرین'), ('کردستان', 'کردستان'), ('سنایی', 'سنایی'), ('پلاستیران', 'پلاستیران')], max_length=25, verbose_name='پاپ سایت')),
                ('internet_t_bw', models.BigIntegerField(blank=True, null=True, verbose_name='پهنای باند ارسال اینترنت')),
                ('internet_r_bw', models.BigIntegerField(blank=True, null=True, verbose_name='پهنای باند دریافت اینترنت')),
                ('intranet_t_bw', models.BigIntegerField(blank=True, null=True, verbose_name='پهنای باند ارسال اینترانت')),
                ('intranet_r_bw', models.BigIntegerField(blank=True, null=True, verbose_name='پهنای باند دریافت اینترانت')),
                ('throughput_t_bw', models.BigIntegerField(blank=True, null=True, verbose_name='پهنای باند ارسال نقطه به نقطه')),
                ('throughput_r_bw', models.BigIntegerField(blank=True, null=True, verbose_name='پهنای باند دریافت تقطه به نقطه')),
                ('ip', models.GenericIPAddressField(verbose_name='آدرس IP')),
                ('notes', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.agent')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.contract')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('micro', 'Micro'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('xlarge', 'XLarge'), ('xxlarge', 'XXLarge')], default='medium', max_length=7)),
                ('ip', models.GenericIPAddressField(verbose_name='آدرس IP')),
                ('notes', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.agent')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.contract')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.customer')),
            ],
        ),
    ]