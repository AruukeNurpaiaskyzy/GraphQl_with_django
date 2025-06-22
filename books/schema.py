import graphene
from graphene_django import DjangoObjectType
from books.models import Books



class BooksType(DjangoObjectType):
    class Meta:
        