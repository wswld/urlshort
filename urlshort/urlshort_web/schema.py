from urlshort.urlshort_web.models import URLEntry
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class URLEntryNode(DjangoObjectType):
    class Meta:
        model = URLEntry


class Query(object):
    url_entry = Node.Field(URLEntryNode)
