# Generated by Django 4.2.13 on 2024-05-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('skills', models.CharField(max_length=200)),
                ('contact_details', models.CharField(max_length=200)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='portfolio_item',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_images/'),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
