from django.core.exceptions import ObjectDoesNotExist
from graphene import Node, String
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from urlshort.urlshort_web.models import URLEntry


class URLEntryNode(DjangoObjectType):
    class Meta:
        model = URLEntry
        fields = ('slug',)


class Query(object):
    url = String(short_url=String())
    short_url = String(url=String())

    def resolve_url(self, info, *args, **kwargs):
        short_url = kwargs.get('short_url')
        short_url = URLEntry.objects.get(slug=short_url)
        return short_url.url

    def resolve_short_url(self, info, *args, **kwargs):
        url = kwargs.get('url')
        obj = URLEntry.objects.get_or_create(url=url)[0]
        return obj.slug
