from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='название',
        help_text='Макс. 64 символа'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    def get_category_slug(self):
        return reverse('category_list_filter', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'blog_categories'


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='заголовок'
    )
    descr = models.TextField(verbose_name='описание')
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='дата создания'
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='категория'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )

    image = models.ImageField(
        upload_to='post',  # от папки media/ поэтому не прописываем media/post
        null=True,
        blank=True,
        verbose_name='картинка'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'post_slug': self.slug})

    @property
    def date(self) -> str:
        return self.date_created.strftime('%d.%m.%y')

    @property
    def full_name(self):
        return self.author.first_name + ' ' + self.author.last_name

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-date_created']


class Contact(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Имя'
    )

    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.CharField(
        max_length=1024,
        verbose_name='Сообщение'
    )

    date_created = models.DateTimeField(default=now, verbose_name='Дата обращения')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'blob_contacts'
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['date_created']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='посты')
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.body


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
