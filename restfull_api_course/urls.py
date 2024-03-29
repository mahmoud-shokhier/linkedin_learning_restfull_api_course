"""restfull_api_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import store.views 
import store.api_views
urlpatterns = [
    path('api/v1/products', store.api_views.ProductList.as_view()),
    path('api/v1/products/new', store.api_views.ProductCreate.as_view()),
    path('api/v1/products/<int:id>/', store.api_views.ProductRetrieveUpdateDestroy.as_view()),
    path('api/v1/products/<int:id>/stats', store.api_views.ProductStats.as_view()),
    path('admin/', admin.site.urls),
]
