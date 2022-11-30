# Generated by Django 4.0.6 on 2022-09-24 22:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix_Admin', '0002_alter_netflixmodel_poster_movie_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Background_Logo_Image',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Background_Mini_Image',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Movie_Audio',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Movie_Cast',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Movie_Description',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Movie_Genres',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Movie_Maker_Name',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Movie_Subtitles',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Poster_Movie_Categories',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Poster_Movie_Hours',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Poster_Movie_Rank',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Poster_Movie_Starring',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='Poster_Movie_Year',
        ),
        migrations.RemoveField(
            model_name='netflixmodel',
            name='User_Id',
        ),
        migrations.AddField(
            model_name='netflixmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=datetime.datetime(2022, 9, 24, 22, 38, 30, 755721, tzinfo=utc), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]