from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils import timezone
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'now': timezone.now,
    })
    
    # Add context processors
    from pages.context_processors import global_context
    env.globals.update(global_context(None))
    
    return env