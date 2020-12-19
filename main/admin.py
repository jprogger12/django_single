from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Product, CategoryProduct, SubCategoryProduct, ProductDetailImage, ProductDetail, Partner, About, \
    Gallery, GalleryDetail, NewsLetter, Sertificate


class subCatProdInline(admin.TabularInline):
    model = SubCategoryProduct
    extra = 2


class ProdDetImageInline(admin.TabularInline):
    model = ProductDetailImage
    extra = 2


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

    search_fields = ('name',)
    inlines = [subCatProdInline]
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height =auto>')

    get_image.short_description = "rasm"


class ProdDetInline(admin.TabularInline):
    model = ProductDetail
    extra = 4


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'prise', 'img')

    search_fields = ('title', 'prise')
    inlines = [ProdDetInline, ProdDetImageInline]
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height =auto>')

    get_image.short_description = "rasm"


admin.site.register(Partner)
admin.site.register(About)
admin.site.register(NewsLetter)
admin.site.register(Sertificate)


class GalDetInline(admin.TabularInline):
    model = GalleryDetail
    extra = 4


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'img')

    search_fields = ('title', )
    inlines = [GalDetInline]
    save_on_top = True
