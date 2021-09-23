# Generated by Django 2.1.2 on 2021-09-22 13:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.CharField(max_length=100, verbose_name='标号')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(blank=True, null=True, verbose_name='正文')),
                ('status', models.CharField(choices=[('d', '草稿'), ('p', '发表')], default='p', max_length=1, verbose_name='状态')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章列表',
                'db_table': 'article',
                'ordering': ['-created_time'],
                'get_latest_by': 'created_time',
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('username', models.CharField(max_length=50)),
                ('userimg', models.CharField(max_length=70)),
                ('nickname', models.CharField(default='一颗小树苗', max_length=50)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('article', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论列表',
                'db_table': 'comment',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='类别名称')),
            ],
            options={
                'verbose_name': '类别名称',
                'verbose_name_plural': '分类列表',
                'db_table': 'category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签名称',
                'verbose_name_plural': '标签列表',
                'db_table': 'tag',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('nickname', models.CharField(default='一颗小树苗', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created_time', models.CharField(default=django.utils.timezone.now, max_length=50)),
                ('comment_num', models.PositiveIntegerField(default=0, verbose_name='评论数')),
                ('avatar', models.ImageField(default='media/default.png', upload_to='media')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'blog_user',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tags', verbose_name='标签'),
        ),
    ]
