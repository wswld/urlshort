from django.db import models
from django.utils import baseconv
import random, string


def _get_slug(size=6, chars=string.ascii_uppercase + string.digits):
    # using the simplest possible solution for now
    return (''.join(random.choice(chars) for _ in range(size))).lower()


class URLEntry(models.Model):
    url = models.URLField()
    slug = models.CharField(max_length=6, blank=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self):
        if not self.slug:
            self.slug = _get_slug()
            while URLEntry.objects.filter(slug=self.slug).exists():
                self.slug = _get_slug()
        super(URLEntry, self).save()
