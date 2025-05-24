from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils import timezone
from jinja2 import Environment


def date_format(value, format_string='%B %d, %Y'):
    """Format a date/datetime object."""
    if value is None:
        return ''
    return value.strftime(format_string)


def truncate_text(value, length=100, killwords=False):
    """Truncate a string to a certain length."""
    if len(value) <= length:
        return value
    
    if killwords:
        return value[:length] + '...'
    
    # Find the last space before the length limit
    truncated = value[:length]
    last_space = truncated.rfind(' ')
    if last_space > 0:
        return truncated[:last_space] + '...'
    return truncated + '...'


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'now': timezone.now,
    })
    
    # Add custom filters
    env.filters['date'] = date_format
    env.filters['truncate'] = truncate_text
    env.filters['default'] = lambda v, d='': v if v else d
    
    # Add context processors
    from pages.context_processors import global_context
    env.globals.update(global_context(None))
    
    return env