from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _


TITLE = _('Task manager')
GREET_ANON = _('Hello there')
GREET_USER = _('Hello, ')
TEXT = [_('This is the Task Manager,'),
        _('I allow you to set tasks, assign performers and '
          'change their statuses.'),
        _('Registration and authentication are required to '
          'work with my system.'),
        ]


class HomeView(TemplateView):
    """
    Figure out why "{% trans '' %}" doesn't work and move text to home template
    """
    template_name = 'index.html'
    extra_context = {
        'title': TITLE, 'greet_anon': GREET_ANON,
        'greet_user': GREET_USER, 'text': TEXT,
    }


def test_case(request):
    raise Exception('This is a test error')
