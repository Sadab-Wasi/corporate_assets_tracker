# Generated by Django 4.2.5 on 2023-09-28 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_employees_company_id_equipments_company_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='employee_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equip_employ_id', to='home.employees'),
        ),
    ]
