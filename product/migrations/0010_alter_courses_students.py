# Generated by Django 5.2.3 on 2025-06-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_school_courses_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='students',
            field=models.ManyToManyField(related_name='offered', to='product.student'),
        ),
    ]
