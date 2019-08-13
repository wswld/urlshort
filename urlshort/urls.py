from django.conf.urls import url
from django.contrib import admin

from graphene_django.views import GraphQLView
from urlshort.views import out

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^graphql$", GraphQLView.as_view(graphiql=True)),
    url(r"^(?P<slug>\w{6})", out),
]