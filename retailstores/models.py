from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.urls import reverse
# Create your models here.

WEEKDAYS = [
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
]


class Store(models.Model):
    category = (
        ('Grocery', 'Grocery'),
        ('Pharma', 'Pharma'),
        ('Mobile Retailer', 'Mobile Retailer'),
        ('Departmental Store', 'Departmental Store'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Store Name')
    description = models.TextField(verbose_name='About Store')
    cover_image = models.ImageField(
        upload_to='Cover_image/%Y/%m%d', default='store_default.jpg')
    categories = models.CharField(max_length=100, choices=category)
    url = models.CharField(max_length=1000, verbose_name='Location URL')
    created_at = models.DateTimeField(default=now, blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    mon_start = models.TimeField(
        blank=True, null=True, verbose_name='Monday Opening time(eg. 07:00)')
    mon_end = models.TimeField(
        blank=True, null=True, verbose_name='Monday Closing time(eg. 19:00)')
    tue_start = models.TimeField(
        blank=True, null=True, verbose_name='Tuesday Opening time(eg. 07:00)')
    tue_end = models.TimeField(
        blank=True, null=True, verbose_name='Tuesday Closing time(eg. 19:00)')
    wed_start = models.TimeField(
        blank=True, null=True, verbose_name='Wednesday Opening time(eg. 07:00)')
    wed_end = models.TimeField(
        blank=True, null=True, verbose_name='Wednesday Closing time(eg. 19:00)')
    thu_start = models.TimeField(
        blank=True, null=True, verbose_name='Thursday Opening time(eg. 07:00)')
    thu_end = models.TimeField(
        blank=True, null=True, verbose_name='Thursday Closing time(eg. 19:00)')
    fri_start = models.TimeField(
        blank=True, null=True, verbose_name='Friday Opening time(eg. 07:00)')
    fri_end = models.TimeField(
        blank=True, null=True, verbose_name='Friday Closing time(eg. 19:00)')
    sat_start = models.TimeField(
        blank=True, null=True, verbose_name='Saturday Opening time(eg. 07:00)')
    sat_end = models.TimeField(
        blank=True, null=True, verbose_name='Saturday Closing time(eg. 19:00)')
    sun_start = models.TimeField(
        blank=True, null=True, verbose_name='Sunday Opening time(eg. 07:00)')
    sun_end = models.TimeField(
        blank=True, null=True, verbose_name='Sunday Closing time(eg. 19:00)')

    def __str__(self):
        return self.name

    def blog_photo(self):
        return mark_safe('<img src="{}" width="150" />'.format(self.cover_image.url))
    blog_photo.short_description = 'Image'
    blog_photo.allow_tags = True

    def get_absolute_url(self):
        return reverse('retailstore:store_single', kwargs={'pk': self.pk})
