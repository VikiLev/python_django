from tastypie.resources import ModelResource
from shop.models import Category, Book


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        allowed_methods = ['get', 'post', 'delete']