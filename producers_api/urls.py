"""producers_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from producers.views import (
    ProducerTypeViewSet,
    ProducerStatusViewSet,
    ProducerViewSet,
)
from products.views import (
    ProductTypeViewSet,
    ProductViewSet,
    ProductPresentationViewSet,
    ProductsByProducerApiView,
)

router = routers.DefaultRouter()
router.register(r'producer_types', ProducerTypeViewSet)
router.register(r'producer_status', ProducerStatusViewSet)
router.register(r'producers', ProducerViewSet)
router.register(r'producttypes', ProductTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productpresentations', ProductPresentationViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/products_import/$', ProductsByProducerApiView.as_view()),
]
