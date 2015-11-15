# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models, forms, constants, widgets
from cms.models import CMSPlugin


link_fieldset = (
    ('Link', {
        'fields': (
            'page_link', 'file', 'url', 'mailto', 'phone',
        ),
        'description': 'Choose one of the link types below.',
    }),
    ('Link options', {
        'fields': (
            ('target', 'anchor',),
        ),
    }),
)


class Bootstrap3BlockquoteCMSPlugin(CMSPluginBase):
    model = models.Boostrap3BlockquotePlugin
    name = _("Blockquote")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/blockquote/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/blockquote.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3BlockquoteCMSPlugin)


class Bootstrap3IconCMSPlugin(CMSPluginBase):
    model = models.Boostrap3IconPlugin
    name = _("Icon")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/icon/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/icon.html'
    text_enabled = True
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'icon',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3IconCMSPlugin)


class Bootstrap3LabelCMSPlugin(CMSPluginBase):
    model = models.Boostrap3LabelPlugin
    name = _("Label")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/label/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/label.html'
    text_enabled = True
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'label',
            'context',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3LabelCMSPlugin)


class Bootstrap3WellCMSPlugin(CMSPluginBase):
    model = models.Boostrap3WellPlugin
    name = _("Well")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/well/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/well.html'
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'size',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3WellCMSPlugin)


class Bootstrap3AlertCMSPlugin(CMSPluginBase):
    model = models.Boostrap3AlertPlugin
    name = _("Alert")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/alert/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/alert.html'
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'context',
            'icon',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3AlertCMSPlugin)


class Bootstrap3ButtonCMSPlugin(CMSPluginBase):
    model = models.Boostrap3ButtonPlugin
    name = _("Link/Button")
    module = _('Bootstrap3')
    form = forms.LinkForm
    change_form_template = 'admin/aldryn_bootstrap3/plugins/button/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/button.html'
    text_enabled = True
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'label',
                'type',
                'btn_context',
                'btn_size',
                'btn_block',
                'txt_context',
                'icon_left',
                'icon_right',
            ),
        }),
    ) + link_fieldset + (
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            )
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

    def icon_src(self, instance):
        from django.contrib.staticfiles.templatetags.staticfiles import static
        return static("cms/img/icons/plugins/link.png")

plugin_pool.register_plugin(Bootstrap3ButtonCMSPlugin)


class Bootstrap3ImageCMSPlugin(CMSPluginBase):
    model = models.Boostrap3ImagePlugin
    name = _("Image")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/image/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/image.html'
    allow_children = True
    cache = False

    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'label',
    #             'context',
    #             'size',
    #             'icon_left',
    #             'icon_right',
    #         )
    #     }),
    # ) + link_fieldset + (
    #     ('Advanced', {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'classes',
    #         )
    #     }),
    # )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3ImageCMSPlugin)


#########
# Panel #
#########


class Bootstrap3PanelCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelPlugin
    name = _("Panel")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel.html'
    form = forms.PanelPluginBaseForm
    allow_children = True

    fieldsets = (
        ('Create', {
            'fields': (
                ('create_heading', 'create_body', 'create_footer'),
            )
        }),
        (None, {'fields': (
            'context',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

    def save_model(self, request, obj, form, change):
        response = super(Bootstrap3PanelCMSPlugin, self).save_model(request, obj, form, change)
        data = form.cleaned_data
        extra = {}
        subplugins = (
            ('create_heading', models.Boostrap3PanelHeadingPlugin, Bootstrap3PanelHeadingCMSPlugin),
            ('create_body', models.Boostrap3PanelBodyPlugin, Bootstrap3PanelBodyCMSPlugin),
            ('create_footer', models.Boostrap3PanelFooterPlugin, Bootstrap3PanelFooterCMSPlugin),
        )
        existing_plugins = [p.plugin_type for p in obj.get_children()]
        for field, model_class, plugin_class in subplugins:
            if not data.get(field):
                # TODO: delete?
                continue
            if plugin_class.__name__ in existing_plugins:
                continue
            plugin = model_class(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=CMSPlugin.objects.filter(parent=obj).count(),
                plugin_type=plugin_class.__name__,
                **extra
            )
            plugin.save()
        return response

plugin_pool.register_plugin(Bootstrap3PanelCMSPlugin)


class Bootstrap3PanelHeadingCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelHeadingPlugin
    name = _("Panel Heading")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel_heading/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_heading.html'
    allow_children = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        (None, {'fields': (
            'title',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3PanelHeadingCMSPlugin)


class Bootstrap3PanelBodyCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelBodyPlugin
    name = _("Panel Body")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel_body/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_body.html'
    allow_children = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        # (None, {'fields': (
        #     'title',
        # )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3PanelBodyCMSPlugin)


class Bootstrap3PanelFooterCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelFooterPlugin
    name = _("Panel Footer")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel_footer/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_footer.html'
    allow_children = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        # (None, {'fields': (
        #     'title',
        # )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3PanelFooterCMSPlugin)


########
# Grid #
########


class Bootstrap3RowCMSPlugin(widgets.BootstrapMediaMixin, CMSPluginBase):
    model = models.Bootstrap3RowPlugin
    name = _('Row')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/row/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/row.html'
    allow_children = True
    child_classes = ['Bootstrap3ColumnCMSPlugin']
    form = forms.RowPluginForm
    fieldsets = [
        ("Create Columns", {
            # 'classes': ('collapse',),
            'fields': (
                'create',
            ) + tuple([
                (
                    'create_{}_col'.format(size),
                    'create_{}_offset'.format(size),
                    'create_{}_push'.format(size),
                    'create_{}_pull'.format(size),
                ) for size in constants.DEVICE_SIZES
            ])
        }),
        ("Advanced", {
            'fields': (
                'classes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3RowCMSPlugin, self).render(context, instance, placeholder)
        return context

    def save_model(self, request, obj, form, change):
        response = super(Bootstrap3RowCMSPlugin, self).save_model(request, obj, form, change)
        data = form.cleaned_data
        for x in xrange(int(data['create']) if data['create'] is not None else 0):
            extra = {}
            for size in constants.DEVICE_SIZES:
                for element in ['col', 'offset', 'push', 'pull']:
                    extra['{}_{}'.format(size, element)] = data.get(
                        'create_{}_{}'.format(size, element)) or None
            col = models.Bootstrap3ColumnPlugin(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=CMSPlugin.objects.filter(parent=obj).count(),
                plugin_type=Bootstrap3ColumnCMSPlugin.__name__,
                **extra
            )
            col.save()
        return response


class Bootstrap3ColumnCMSPlugin(CMSPluginBase, widgets.BootstrapMediaMixin):
    model = models.Bootstrap3ColumnPlugin
    name = _('Column')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/column/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/column.html'
    allow_children = True
    parent_classes = ['Bootstrap3RowCMSPlugin']

    fieldsets = [
        (None, {
            'fields': tuple([
                (
                    '{}_col'.format(size),
                    '{}_offset'.format(size),
                    '{}_push'.format(size),
                    '{}_pull'.format(size),
                ) for size in constants.DEVICE_SIZES
            ])
        }),
        ("Advanced", {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'tag',
            )
        }),
    ]


plugin_pool.register_plugin(Bootstrap3RowCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ColumnCMSPlugin)
