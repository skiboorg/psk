from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from pytils.translit import slugify
from random import choices
import string
from django.utils.safestring import mark_safe
from PIL import Image
# import settings
import psk.settings
import os
import uuid


class Client(models.Model):
    order = models.IntegerField('Номер по порядку', default=1)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    image = models.ImageField('Постоянный клиент', upload_to='client_img/', blank=False, null=True)
    def __str__(self):
        return f'Постоянный клиент : {self.name} №ПП:{self.order}'

    class Meta:
        verbose_name = "Постоянный клиент"
        verbose_name_plural = "Постоянный клиент"

class BlogPost(models.Model):
    name = models.CharField('Название статьи', max_length=255, blank=False, null=True)
    short_description = models.CharField('Краткое описание (255 символов)',max_length=255, blank=False, null=True)
    description = RichTextUploadingField('Статья', blank=False, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    image = models.ImageField('Изображение превью (360 x 240)', upload_to='post_img/', blank=False)
    pageH1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    pageTitle = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    pageDescription = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    pageKeywords = models.TextField('Keywords SEO', blank=True, null=True)
    views = models.IntegerField('Просмотров', default=0)
    isActive = models.BooleanField('Отображается?', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.nameSlug:
            slugRandom = ''
            testSlug = BlogPost.objects.filter(nameSlug=slug)
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.nameSlug = slug + slugRandom
            else:
                self.nameSlug = slug
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/blog/{self.nameSlug}/'

    def __str__(self):
        return 'Статья : %s ' % self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class Banner(models.Model):
    order = models.IntegerField('Номер по порядку', default=1)
    bigText = models.CharField('Заголовок на баннере (100 символов)', max_length=100, blank=True, null=True)
    smallText = models.CharField('Описание на баннере (200 символов)', max_length=200, blank=True, null=True)
    image = models.ImageField('Картинка для баннера (1920 x 660)', upload_to='slides/', blank=True, null=True)
    buttonText = models.CharField('Надпись на первой кнопке', max_length=10, blank=True, null=True)
    buttonUrl = models.CharField('Ссылка с кнопки', max_length=100, blank=True, null=True)
    isActive = models.BooleanField('Отображать ?', default=True)

    def __str__(self):
        return f'Баннер № П/П {self.order}'

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"



class Service(models.Model):
    name = models.CharField('Название услуги', max_length=255, blank=False, null=True)
    short_description = models.TextField('Краткое описание (380 символов)', blank=True, null=True)
    description = RichTextUploadingField('Полное описание услуги', blank=True, null=True)
    isHomeVisible = models.BooleanField('Отображать на главной?', default=True, db_index=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    image = models.ImageField('Изображение превью (360 x 240)', upload_to='service_img/', blank=False)
    pageH1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    pageSpecialText = models.CharField('Специальное предложение', max_length=255, blank=True, null=True)
    pageTitle = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    pageDescription = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    pageKeywords = models.TextField('Keywords SEO', blank=True, null=True)
    price = models.IntegerField('Стоимость услуги', default=0)
    views = models.IntegerField('Просмотров', default=0)
    isActive = models.BooleanField('Активная услуга?', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.nameSlug:
            slugRandom = ''
            testSlug = Service.objects.filter(nameSlug=slug)
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.nameSlug = slug + slugRandom
            else:
                self.nameSlug = slug
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/service/{self.nameSlug}/'

    def __str__(self):
        return 'Услуга : %s ' % self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class ServiceStep(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,blank=False,null=True,verbose_name='Услуга',related_name='steps')
    number = models.CharField('Номер шага', max_length=10,blank=False, null=True)
    text = models.TextField('Текст', blank=False, null=True)

    def __str__(self):
        return 'Шаг для услуги : %s ' % self.service.name

    class Meta:
        verbose_name = "Шаг для услуги"
        verbose_name_plural = "Шаги для услуг"


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=False, null=True, verbose_name='Услуга',related_name='features')
    icon = models.ImageField('Иконка', upload_to='service_img/', blank=False, null=True)
    text = models.TextField('Текст', blank=False, null=True)

    def __str__(self):
        return 'Приемущество для услуги : %s ' % self.service.name

    class Meta:
        verbose_name = "Приемущество для услуги"
        verbose_name_plural = "Приемущества для услуг"

class Review(models.Model):
    image = models.ImageField('Отзыв', upload_to='review_img/', blank=False, null=True)
    image_small = models.CharField(max_length=255, blank=True, null=True)
    is_home = models.BooleanField('Отображать на главной', default=False)
    def image_tag(self):
        if self.image_small:
            return mark_safe('<img src="{}" width="150" height="150" style="object-fit:cover" />'.format(self.image_small))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'

    def save(self, *args, **kwargs):
        fill_color = '#fff'
        image = Image.open(self.image)
        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background
        image.thumbnail((250, 250), Image.ANTIALIAS)
        small_name = '/media/review_img/{}'.format(str(uuid.uuid4()) + '.jpg')
        os.makedirs('{}/media/review_img/'.format(psk.settings.BASE_DIR), exist_ok=True)
        image.save(f'{psk.settings.BASE_DIR}/{small_name}', 'JPEG', quality=90)
        self.image_small =  small_name
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return 'Отзыв  : %s ' % self.id

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Cert(models.Model):
    image = models.ImageField('Сертификат', upload_to='cert_img/', blank=False, null=True)
    image_small = models.CharField(max_length=255, blank=True, null=True)
    is_home = models.BooleanField('Отображать на главной', default=False)
    def image_tag(self):
        if self.image_small:
            return mark_safe('<img src="{}" width="150" height="150" style="object-fit:cover" />'.format(self.image_small))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'

    def save(self, *args, **kwargs):
        fill_color = '#fff'
        image = Image.open(self.image)
        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background
        image.thumbnail((250, 250), Image.ANTIALIAS)
        small_name = '/media/cert_img/{}'.format(str(uuid.uuid4()) + '.jpg')
        os.makedirs('{}/media/cert_img/'.format(psk.settings.BASE_DIR), exist_ok=True)
        image.save(f'{psk.settings.BASE_DIR}/{small_name}', 'JPEG', quality=90)
        self.image_small =  small_name
        super(Cert, self).save(*args, **kwargs)

    def __str__(self):
        return 'Сертификат  : %s ' % self.id

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"


class Project(models.Model):
    short_description = models.TextField('Краткое описание (380 символов)', blank=False, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    image = models.ImageField('Изображение (360 x 240)', upload_to='project_img/', blank=True, null=True)
    description = RichTextUploadingField('Полное описание проекта', blank=True, null=True)
    pageH1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    pageTitle = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    pageDescription = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    pageKeywords = models.TextField('Keywords SEO', blank=True, null=True)


    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.nameSlug:
            slugRandom = ''
            testSlug = Project.objects.filter(nameSlug=slug)
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.nameSlug = slug + slugRandom
            else:
                self.nameSlug = slug

        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/projects/{self.nameSlug}/'

    def __str__(self):
        return 'Проект : %s ' % self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class ProjectAddress(models.Model):
    project = models.ForeignKey(Project, blank=False, null=True, on_delete=models.CASCADE,
                                verbose_name='Проект')
    address = models.CharField('Адрес', max_length=255, blank=False, null=True)
class ProjectImage(models.Model):
    project_address = models.ForeignKey(ProjectAddress,blank=False,null=True,on_delete=models.CASCADE,verbose_name='Фото для проекта')

    image = models.ImageField('Фото', upload_to='project_img/', blank=False, null=True)
    image_small = models.CharField(max_length=255, blank=True, default='')
    image_before = models.BooleanField('До?', default=False)

    def __str__(self):
        return 'Фото для проекта : {}'.format(self.project_address.project.name)

    class Meta:
        verbose_name = "Фото для проекта"
        verbose_name_plural = "Фото для проекта"

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.image_small:
            return mark_safe('<img src="{}" width="150" height="150" style="object-fit:cover" />'.format(self.image_small))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'

    def save(self, *args, **kwargs):
        fill_color = '#fff'
        image = Image.open(self.image)

        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background

        image.thumbnail((250, 250), Image.ANTIALIAS)

        small_name = '/media/project_img/{}/{}'.format(self.project_address.id, str(uuid.uuid4()) + '.jpg')
        os.makedirs('{}/media/project_img/{}'.format(psk.settings.BASE_DIR,self.project_address.id), exist_ok=True)
        image.save(f'{psk.settings.BASE_DIR}/{small_name}', 'JPEG', quality=90)

        self.image_small =  small_name

        super(ProjectImage, self).save(*args, **kwargs)

class Callback(models.Model):
    name = models.CharField('Имя',max_length=255, blank=True, default='Нет данных')
    phone = models.CharField('Телефон', max_length=255, blank=True, default='Нет данных')
    email = models.CharField('Почта', max_length=255, blank=True, default='Нет данных')
    # service = models.CharField('Услуга', max_length=255, blank=True, default='Нет данных')
    message = models.TextField('Сообщение', blank=True, default='Нет данных')
    # file = models.FileField('Прикрепленный файл',blank=True,null=True)
    created_at = models.DateTimeField('Дата заполнения', auto_now_add=True)


    def __str__(self):
        return 'Форма заказа звонка. Заполнена {}'.format(self.created_at)



    class Meta:
        verbose_name = "Форма заказа звонка"
        verbose_name_plural = "Формы заказа звонка"


class SeoTag(models.Model):
    indexTitle = models.CharField('Тег Title для главной', max_length=255, blank=True, null=True)
    indexDescription = models.CharField('Тег Description для главной', max_length=255, blank=True, null=True)
    indexKeywords = models.TextField('Тег Keywords для главной', blank=True, null=True)
    servicesTitle = models.CharField('Тег Title для страницы со всеми услугами', max_length=255, blank=True, null=True)
    servicesDescription = models.CharField('Тег Description для страницы со всеми услугам', max_length=255, blank=True,
                                           null=True)
    servicesKeywords = models.TextField('Тег Keywords для страницы со всеми услугам', blank=True, null=True)
    projectsTitle = models.CharField('Тег Title для страницы со всеми проектами', max_length=255, blank=True, null=True)
    projectsDescription = models.CharField('Тег Description для страницы со всеми проектами', max_length=255, blank=True,
                                        null=True)
    projectsKeywords = models.TextField('Тег Keywords для страницы со всеми проектами', blank=True, null=True)

    contactTitle = models.CharField('Тег Title для страницы контакты', max_length=255, blank=True, null=True)
    contactDescription = models.CharField('Тег Description для страницы контакты', max_length=255, blank=True,
                                        null=True)
    contactKeywords = models.TextField('Тег Keywords для страницы контакты', blank=True, null=True)

    aboutTitle = models.CharField('Тег Title для страницы о компании', max_length=255, blank=True, null=True)
    aboutDescription = models.CharField('Тег Description для страницы о компании', max_length=255, blank=True,
                                        null=True)
    aboutKeywords = models.TextField('Тег Keywords для страницы о компании', blank=True, null=True)

    blogTitle = models.CharField('Тег Title для страницы блог', max_length=255, blank=True, null=True)
    blogDescription = models.CharField('Тег Description для страницы блог', max_length=255, blank=True,
                                        null=True)
    blogKeywords = models.TextField('Тег Keywords для страницы блог', blank=True, null=True)

    yandexMetrika = models.TextField('Код Яндекс метрики', blank=True, null=True)
    fbPixel = models.TextField('Код пикселя', blank=True, null=True)
    yandexTAG = models.CharField('Код подтверждения Яндекс', max_length=255, blank=True, null=True)
    googleTAG = models.CharField('Код подтверждения google', max_length=255, blank=True, null=True)

    indexText = RichTextUploadingField('Текст на главную', blank=True, null=True)
    aboutText = RichTextUploadingField('Текст на страницу о нас', blank=True, null=True)

    def __str__(self):
        return 'Теги и текста для статических страниц'

    class Meta:
        verbose_name = "Теги и текста для статических страниц"
        verbose_name_plural = "Теги и текста для статических страниц"

# def callback_ps(sender, instance, **kwargs):
#     msg_html = render_to_string('email/callback.html', {'user': instance.name,
#                                                         'phone': instance.phone,
#                                                         'email': instance.email,
#                                                         'service': instance.service,
#                                                         'message': instance.message,
#                                                         'file': instance.file})
#     send_mail('Заполнена форма обратной связи', None, 'callback@pto-msk.com', [settings.SEND_TO],
#               fail_silently=False, html_message=msg_html)
#
# post_save.connect(callback_ps, sender=Callback)