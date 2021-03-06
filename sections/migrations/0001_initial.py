# Generated by Django 2.2.3 on 2020-01-27 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptName', models.CharField(max_length=50, verbose_name='dept_name')),
                ('deptCode', models.CharField(max_length=50, verbose_name='dept_code')),
                ('active', models.CharField(default='Y', max_length=10, verbose_name='isactive')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studName', models.CharField(max_length=100, verbose_name='stud_name')),
                ('studAge', models.IntegerField(verbose_name='stud_age')),
                ('studFees', models.FloatField(verbose_name='stud_fees')),
                ('studAddress', models.TextField(max_length=100, verbose_name='stud_adr')),
                ('active', models.CharField(default='Y', max_length=10, verbose_name='isactive')),
                ('deptref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studsref', to='sections.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjName', models.CharField(max_length=50, verbose_name='subj_name')),
                ('subjCode', models.CharField(max_length=50, verbose_name='subj_code')),
                ('active', models.CharField(default='Y', max_length=10, verbose_name='isactive')),
                ('studentsref', models.ManyToManyField(related_name='coursesref', to='sections.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(max_length=50, verbose_name='adr_city')),
                ('pinCode', models.CharField(max_length=50, verbose_name='pin_code')),
                ('active', models.CharField(default='Y', max_length=10, verbose_name='isactive')),
                ('studref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adrref', to='sections.Student')),
            ],
        ),
    ]
