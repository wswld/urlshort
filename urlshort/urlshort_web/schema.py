from urlshort.urlshort_web.models import URLEntry
from graphene import Node, String
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class URLEntryNode(DjangoObjectType):
    class Meta:
        model = URLEntry
        fields = ('slug',)


class Query(object):
    url = String(slug=String())

    def resolve_url(self, info, *args, **kwargs):
        slug = kwargs.get('slug')
        short_url = URLEntry.objects.get(slug=slug)
        return short_url.url
