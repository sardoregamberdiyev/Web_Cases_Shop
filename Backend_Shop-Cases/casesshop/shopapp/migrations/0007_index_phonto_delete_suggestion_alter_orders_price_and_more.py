# Generated by Django 4.2.1 on 2023-05-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_alter_orders_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_Phonto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(null=True, upload_to='static/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Suggestion',
        ),
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='price_type',
            field=models.CharField(choices=[('$', '$'), ('UZS', 'UZS')], max_length=3),
        ),
        migrations.AlterField(
            model_name='orders',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
