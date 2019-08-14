from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


def redirect_view(request, slug):
    """This view redirects to a full URL if accessed with a short slug"""
    entry = get_object_or_404("URLEntry", slug=slug)
    return HttpResponseRedirect(entry.url)
