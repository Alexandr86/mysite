#coding: utf8
from django.contrib.auth.decorators import login_required
from django.db import models


def get_upload_file_name(instance, filename):
    """
    upload file
    """
    return "images/%s" % (filename)


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    datetime = models.DateField(u'Дата публикации')
    intro = models.TextField(max_length=1000, verbose_name=u'Введение')
    content = models.TextField(max_length=10000, verbose_name=u'Cодержимое')
    image = models.ImageField(upload_to=get_upload_file_name, verbose_name=u'Рисунок', help_text='150x150px'    )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i" % self.id


class Person(models.Model):
    first_name = models.CharField(max_length=60, verbose_name=u'Имя')
    last_name = models.CharField(max_length=60, verbose_name=u'Фамилия')
    date_birth = models.DateField(verbose_name=u'Дата рождения')
    phone = models.CharField(max_length=25, verbose_name=u'Телефон')
    skype = models.CharField(max_length=30, verbose_name=u'Cкайп')
    email = models.EmailField(u'Почтовый ящик')
    about = models.TextField(max_length=10000, verbose_name=u'Информация')
    photo = models.ImageField(upload_to=get_upload_file_name, verbose_name=u'Фото',
                              help_text=u'Размер рисунка должен быть: 150x150px')
    def __unicode__(self):
        return '%s %s' %(self.last_name, self.first_name)

class Portfolio(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Название')
    url = models.URLField(verbose_name=u'Ссылка')
    screen_shot = models.ImageField(upload_to=get_upload_file_name, verbose_name=u'Стартовая страница')

    def __unicode__(self):
        return '%s' % self.name

class Contacts(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Ваше имя')
    email = models.EmailField(verbose_name=u'e-mail')
    message = models.TextField(max_length=60,verbose_name=u'Текст сообщения')

    def __unicode__(self):
        return '%s' % self.name