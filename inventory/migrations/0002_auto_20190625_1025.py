# Generated by Django 2.2.2 on 2019-06-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='shop.Category'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='Attribute',
            field=models.ForeignKey(on_delete='models.CASCADE', related_name='attribute_values', to='inventory.Attribute'),
        ),
    ]
