# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _
from .conf import settings

CONTEXT_CHOICES = (
    ('primary', 'Primary',),
    ('success', 'Success',),
    ('info', 'Info',),
    ('warning', 'Warning',),
    ('danger', 'Danger',),
)
CONTEXT_DEFAULT = 'default'

BUTTON_CONTEXT_CHOICES = (
    ('default', 'Default',),
) + CONTEXT_CHOICES + (
    ('link', 'Link Button',),
    ('', 'Custom',),
)
BUTTON_CONTEXT_DEFAULT = 'default'

TXT_LINK_CONTEXT_CHOICES = (
    ('', 'None',),
) + CONTEXT_CHOICES + (
    # ('alert-link', 'Alert Link',),
    ('muted', 'Muted',),
)
TXT_LINK_CONTEXT_DEFAULT = ''

LABEL_CONTEXT_CHOICES = (
    ('default', 'Default',),
) + CONTEXT_CHOICES + (
    # ('', 'Custom',),
)
LABEL_CONTEXT_DEFAULT = 'default'

PANEL_CONTEXT_CHOICES = (
    ('default', 'Default',),
) + CONTEXT_CHOICES + (
    # ('', 'Custom',),
)
PANEL_CONTEXT_DEFAULT = 'default'

SIZE_CHOICES = (
    ('lg', 'Large',),
    ('md', 'Medium',),
    ('sm', 'Small',),
    ('xs', 'Extra Small',),
)

SIZE_WIDGET_CHOICES = (
    # ('', 'Default'),
) + SIZE_CHOICES
SIZE_WIDGET_DEFAULT = 'md'

SIZES = tuple([size for size, name in SIZE_CHOICES])

SIZE_DEFAULT = 'md'

GUTTER = 30

# WARNING: changing DEVICE_CHOICES identifier will cause model creation to change and
#          requires database migrations!
DEVICES = (
    {
        'identifier': 'xs',
        'name': _("mobile phones"),
        'width': None,
        'width_max': 750,
        'viewport_width_min': 0,
        'viewport_width_max': 767,
        'icon': 'mobile-phone',
    },
    {
        'identifier': 'sm',
        'name': _("tablets"),
        'width': 750,
        'viewport_width_min': 768,
        'viewport_width_max': 991,
        'icon': 'tablet',
    },
    {
        'identifier': 'md',
        'name': _("laptops"),
        'width': 970,
        'viewport_width_min': 992,
        'viewport_width_max': 1199,
        'icon': 'laptop',
    },
    {
        'identifier': 'lg',
        'name': _("large desktops"),
        'width': 1170,
        'viewport_width_min': 1200,
        'viewport_width_max': None,  # TODO: find a better value
        'icon': 'desktop',
    },
)
for device in DEVICES:
    identifier = device['identifier']
    device['long_description'] = "{name} ({viewport_width_min}px to {viewport_width_max}px)".format(**device)
    device['size_name'] = dict(SIZE_CHOICES).get(identifier)
    if 'width_max' not in device.keys():
        device['width_max'] = device['width']

DEVICE_DICT = {device['identifier']: device for device in DEVICES}

DEVICE_CHOICES = (
    ('xs', _("Tiny")),
    ('sm', _("Small")),
    ('md', _("Medium")),
    ('lg', _("Large")),
)
DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])

GRID_SIZE = settings.ALDRYN_BOOTSTRAP3_GRID_SIZE


ASPECT_RATIOS = (
    (1, 1),
    (4, 3),
    (16, 9),
    (16, 10),
    (21, 9),
)
ASPECT_RATIOS_REVERSED = tuple([(y, x) for x, y in ASPECT_RATIOS])

ASPECT_RATIO_CHOICES = \
    tuple([
        ('{}x{}'.format(x, y), '{}x{}'.format(x, y))
        for x, y in ASPECT_RATIOS
    ]) + tuple([
        ('{}x{}'.format(x, y), '{}x{}'.format(x, y))
        for x, y in ASPECT_RATIOS_REVERSED
    ])
