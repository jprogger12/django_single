from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Product(models.Model):
    img = models.ImageField('Maxsulot rasmi', upload_to='products')
    title = models.CharField('Maxsulot nomi', max_length=255)
    slug = models.SlugField('Ssilka')
    category = models.ForeignKey(to='CategoryProduct', on_delete=models.CASCADE, verbose_name='Categoriya', null=True)
    subcategory = models.ForeignKey(to='SubCategoryProduct', on_delete=models.CASCADE, verbose_name='SubCategoriya',
                                    null=True)
    prise = models.DecimalField(verbose_name='Narxini kiriting', decimal_places=2, max_digits=20, null=True)
    about = models.TextField(verbose_name='Maxsulot Haqida', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('prod-detail', kwargs={'category': self.category.name, 'id': self.id})

    def __str__(self):
        return self.title


class CategoryProduct(models.Model):
    name = models.CharField('Categoriya', max_length=255)

    def __str__(self):
        return self.name


class SubCategoryProduct(models.Model):
    category = models.ForeignKey(to=CategoryProduct, on_delete=models.CASCADE, related_name='category',
                                 verbose_name='Categoriyani tanlang')
    name = models.CharField(verbose_name='SubCategoriyani kiriting', max_length=255)

    def __str__(self):
        return self.category.name + " > " + self.name


class ProductDetail(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Maxsulot')
    productfeatures = models.CharField('Maxsulot Xususiyati nomi', max_length=255)
    productfeaturestext = models.CharField('Maxsulot Xususiyati', max_length=255)


class ProductDetailImage(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Maxsulot')
    img = models.ImageField('Qo\'shimcha rasm', upload_to='prodThumbImg')


class Partner(models.Model):
    name = models.CharField('Hamkorning nomi', max_length=200)
    img = models.ImageField('Hamkorning logotipi', upload_to='partners')

    def __str__(self):
        return self.name


class Sertificate(models.Model):
    name = models.CharField('Sertifikatning nomi', max_length=200)
    img = models.ImageField('Sertifikatning rasmi', upload_to='partners')

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField('Mavzu', max_length=255)
    text = models.TextField('Maqola')
    slug = models.SlugField('link', max_length=255)

    def get_absolute_url(self):
        return reverse('about', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField('Galereyaga sarlavha', max_length=255)
    date = models.DateField('galerreya qoshilgan vaqti', default=timezone.now)
    img = models.ImageField('Rasm', upload_to='gallery')
    slug = models.SlugField('link', max_length=255)

    def get_absolute_url(self):
        return reverse('gallery-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class GalleryDetail(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Galereya')
    img = models.ImageField('Rasm', upload_to='gallery')


class NewsLetter(models.Model):
    title = models.CharField('Mavzu', max_length=255)
    letter = models.TextField('Maqola')
    img = models.ImageField('rasm', upload_to='newsletter')
    date = models.DateField('Maqola yozilgan sana ', default=timezone.now)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title
