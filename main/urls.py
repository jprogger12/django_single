"""single URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('partner/', views.partner, name='partner'),
    path('payment/', views.payment, name='payment'),
    path('news/', views.ShowNews.as_view(), name='news'),
    path('news/<int:pk>', views.ShowNewsDetail.as_view(), name='news-detail'),
    path('gallery/', views.ShowGallery.as_view(), name='gallery'),
    path('gallery/<str:slug>/', views.ShowGalleryDetail.as_view(), name='gallery-detail'),
    path('about/<slug:slug>/', views.about, name='about'),
    path('category/<str:category>/', views.ShowByCategory.as_view(), name='category'),
    path('category/<str:category>/<int:id>/', views.prodDetail, name='prod-detail'),
]
