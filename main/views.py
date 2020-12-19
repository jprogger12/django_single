from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, ProductDetail, ProductDetailImage, CategoryProduct, SubCategoryProduct, Partner, About, \
    Gallery, GalleryDetail, NewsLetter, Sertificate


# Create your views here.
class Index(ListView):
    model = Product


    template_name = 'main/index.html'

    # def get_queryset(self):
    #     # print(get_blog_popular())
    #     return Product.objects.filter(category__name=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = CategoryProduct.objects.all()
        context['news'] = NewsLetter.objects.all()[:4]
        context['product2'] = Product.objects.all()[:2]
        context['partner'] = Partner.objects.all()
        context['sertific'] = Sertificate.objects.all()

        return context


def index(request):
    pr = Product.objects.all()
    cat = CategoryProduct.objects.all()
    return render(request, 'main', {'prod': pr, 'categories': cat})


def prodDetail(request, category, id):
    pr = Product.objects.get(id=id)
    img = ProductDetailImage.objects.filter(product_id=id)
    prDet = ProductDetail.objects.filter(product_id=id)
    cat = CategoryProduct.objects.all()
    return render(request, 'main/product_detail.html', {'prod': pr, 'img': img, 'pdet': prDet, 'categories': cat})


def contact(request):
    cat = CategoryProduct.objects.all()
    return render(request, 'main/contact.html', {'categories': cat})


def payment(request):
    cat = CategoryProduct.objects.all()
    return render(request, 'main/payment.html', {'categories': cat})


def about(request, slug='bosh'):
    cat = CategoryProduct.objects.all()
    ab = About.objects.all()
    if slug == 'bosh':
        try:
            letter = About.objects.get(id=1)

        except:
            letter = []
            return render(request, 'main/about.html', {'categories': cat, 'about': ab, 'letter': letter})
    else:
        letter = About.objects.get(slug=slug)

    return render(request, 'main/about.html', {'categories': cat, 'about': ab, 'letter': letter})


def partner(request):
    part = Partner.objects.all()
    cat = CategoryProduct.objects.all()
    return render(request, 'main/partners.html', {'partner': part, 'categories': cat})


class ShowByCategory(ListView):
    model = Product
    paginate_by = 2

    template_name = 'main/product.html'

    def get_queryset(self):
        # print(get_blog_popular())
        return Product.objects.filter(category__name=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        context['categories'] = CategoryProduct.objects.all()

        return context


class ShowGallery(ListView):
    model = Gallery
    paginate_by = 3

    template_name = 'main/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = CategoryProduct.objects.all()
        return context


class ShowGalleryDetail(ListView):
    model = GalleryDetail
    paginate_by = 3

    template_name = 'main/gallerydetail.html'

    def get_queryset(self):
        # print(get_blog_popular())
        return GalleryDetail.objects.filter(gallery__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Gallery.objects.get(slug=self.kwargs['slug'])
        context['categories'] = CategoryProduct.objects.all()

        return context


class ShowNews(ListView):
    model = NewsLetter
    paginate_by = 3

    template_name = 'main/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = CategoryProduct.objects.all()

        return context


class ShowNewsDetail(DetailView):
    model = NewsLetter
    slug_field = 'id'
    template_name = 'main/newsdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newslist'] = NewsLetter.objects.all()[:5]

        context['categories'] = CategoryProduct.objects.all()

        return context

