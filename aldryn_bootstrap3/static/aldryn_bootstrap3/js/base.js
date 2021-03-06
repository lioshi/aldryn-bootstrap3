/*
 * Copyright https://github.com/divio/django-cms
 */

// #############################################################################
// ALDRYN-BOOTSTRAP3
(function ($) {
    'use strict';

    // shorthand for jQuery(document).ready();
    $(function () {
        /**
         * Handles all reauired JavaScript for the aldryn-bootstrap3 addon.
         *
         * @class bootstrap3
         */
        var bootstrap3 = {

            /**
             * Widget used in aldryn_bootstrap3/widgets/context.html.
             * Provides a button group list and enables the user
             * to select one of the choices.
             *
             * @method contextWidget
             * @param {jQuery} element context element to render
             */
            contextWidget: function contextWidget(element) {
                var data = element.data();
                var fieldName = data.context;
                var contextInputs = element.find('.js-btn-group-context-' + fieldName + ' label');
                var selectedContextInput;

                contextInputs.find('input').each(function (index, item) {
                    var input = $(item);
                    var label = input.parent();
                    var element = contextInputs.find('input[value="default"]');

                    // initial active state
                    if (input.prop('checked')) {
                        selectedContextInput = input;
                        label.addClass('active');
                    }

                    if (!selectedContextInput) {
                        selectedContextInput = element;
                    }

                    // set color context
                    if (item.value && item.value !== 'muted') {
                        label.addClass('btn btn-' + item.value);
                    } else {
                        label.addClass('btn btn-default');
                    }

                    // set active states
                    label.on('click', function () {
                        var input = $(this).find('input');

                        selectedContextInput.prop('checked', false);
                        input.prop('checked', true);

                        selectedContextInput = input;
                    });

                });
            },

            /**
             * Widget used in aldryn_bootstrap3/widgets/icon.html.
             * Renders a selectable icon dropdown where you can choose
             * from font-awesome or glyphicons depending on your settings.
             *
             * @method iconWidget
             * @param {jQuery} element context element to render
             */
            iconWidget: function iconWidget(element) {
                var data = element.data();
                var name = data.name;
                var iconPicker = element.find('.js-icon-' + name + ' .js-icon-picker');
                var iconSet = element.find('.js-icon-' + name + ' .js-iconset');
                var enableIconCheckbox = element.find('.js-icon-' + name + ' .js-icon-enable');
                var widgets = element.find('.js-icon-' + name + ' .js-icon-widgets');
                var iconPickerButton = iconPicker.find('button');
                var initialValue = iconPickerButton.data('icon');
                var initialIconset = iconSet.find('option[data-prefix=' + data.iconset + ']').attr('value');

                // initialize bootstrap iconpicker functionality
                iconPickerButton.iconpicker({
                    arrowClass: 'btn-default',
                    icon: initialValue,
                    iconset: initialIconset
                });

                // show label instead of dropdown if there is only one choice available
                if (iconSet.find('option').length === 1) {
                    iconSet.hide();
                    iconSet.parent().prepend('' +
                        '<label class="form-control-static">' +
                            iconSet.find('option').text() +
                        '</label>');
                }

                // set correct iconset when switching the font via dropdown
                iconSet.on('change', function () {
                    iconPickerButton.iconpicker('setIconset', $(this).val());
                });

                // checkbox is shown if field is not required, switches visibility
                // of icon selection to on/off
                enableIconCheckbox.on('change', function () {
                    if ($(this).prop('checked')) {
                        widgets.removeClass('hidden');
                        iconPicker.trigger('change');
                    } else {
                        widgets.addClass('hidden');
                        iconPickerButton.find('input').val('');
                    }
                }).trigger('change');
            },

            /**
             * Renders the preview on top of the button/ling widget page.
             * Only one button widget allowed per page.
             *
             * @method buttonPreview
             */
            buttonPreview: function buttonPreview() {
                var container = $('.aldryn-bootstrap3-button');
                var previewBtn = container.find('.js-preview-btn .js-button');
                var previewBtnText = previewBtn.find('span');
                var defaultBtnText = previewBtn.text();
                var typeState = '';
                var blockClass = '';
                var sizeClass = '';
                var timer = function () {};
                var timeout = 50;

                // helper references
                var labelContext = $('#id_label');
                var typeContext = $('#id_type_0, #id_type_1');
                var sizeContext = $('.field-btn_size');
                var btnContext = $('.field-btn_context');
                var colorContext = $('.field-txt_context');
                var blockContext = $('.field-btn_block');
                var iconContext = $('.js-icon-picker button');

                // attach event to the label
                labelContext.on('keydown', function () {
                    clearTimeout(timer);
                    timer = setTimeout(function () {
                        updatePreview({
                            type: 'text',
                            text: labelContext.val()
                        });
                    }, timeout);
                }).trigger('keydown');

                // attach event to the link/button switch
                typeContext.on('change', function () {
                    updatePreview({
                        type: 'markup',
                        context: $(this).val()
                    });
                });

                // handle button context selection
                // autotrigger will be handled by link/button switcher
                btnContext.find('label').on('click', function () {
                    updatePreview({
                        type: 'context',
                        cls: cleanClass($(this).attr('class'))
                    });
                });

                // handle text color button context selection
                colorContext.find('label').on('click', function () {
                    updatePreview({
                        type: 'context',
                        cls: cleanClass($(this).attr('class'))
                    });
                });

                // handle block checkbox
                blockContext.find('input').on('change', function () {
                    updatePreview({
                        type: 'block',
                        state: $(this).prop('checked')
                    });
                });

                // handle size selection
                sizeContext.find('label').on('click', function () {
                    updatePreview({
                        type: 'size',
                        cls: cleanClass($(this).attr('class'))
                    });
                });

                // handle icon picker
                iconContext.on('change', function () {
                    var el = $(this);
                    if (el.attr('name') === 'icon_left') {
                        // icon left alignment
                        previewBtn.find('.pre').attr('class', 'pre ' + el.find('i').attr('class'));
                    } else {
                        // icon right alignment
                        previewBtn.find('.post').attr('class', 'post ' + el.find('i').attr('class'));
                    }
                }).trigger('change');

                // control visibility of icons
                $('#id_icon_left').on('change', function () {
                    if ($(this).is(':checked')) {
                        previewBtn.find('.pre').show();
                    } else {
                        previewBtn.find('.pre').hide();
                    }
                });
                $('#id_icon_right').on('change', function () {
                    if ($(this).is(':checked')) {
                        previewBtn.find('.post').show();
                    } else {
                        previewBtn.find('.post').hide();
                    }
                });

                // certain elements can only be loaded after a timeout
                setTimeout(function () {
                    blockContext.find('input:checked').trigger('change');
                    typeContext.filter(':checked').trigger('change');
                    sizeContext.find('input:checked').parent().trigger('click');
                }, 0);

                // every event fires updatePreview passing in arguments what
                // has to be done
                function updatePreview(obj) {
                    // handle "label" inputs
                    if (obj.type === 'text') {
                        if (obj.text !== '') {
                            previewBtnText.text(obj.text);
                        } else {
                            previewBtnText.text(defaultBtnText);
                        }
                    }

                    // handle link/button selection which hides/shows text context
                    if (obj.type === 'markup') {
                        if (obj.context === 'lnk') {
                            typeState = obj.context;
                            blockContext.hide();
                            btnContext.hide();
                            colorContext.show();
                            colorContext.find('label.active').trigger('click');
                        } else {
                            typeState = obj.context;
                            blockContext.show();
                            colorContext.hide();
                            btnContext.show();
                            btnContext.find('label.active').trigger('click');
                        }
                    }

                    // update context
                    if (obj.type === 'context') {
                        if (typeState === 'lnk') {
                            previewBtn.attr('class', 'text text-' + obj.cls + blockClass + sizeClass);
                        } else {
                            previewBtn.attr('class', 'btn btn-' + obj.cls + blockClass + sizeClass);
                        }
                    }

                    // change block type
                    if (obj.type === 'block') {
                        if (obj.state) {
                            blockClass = ' btn-block';
                            previewBtn.addClass(blockClass);
                        } else {
                            blockClass = '';
                            previewBtn.removeClass('btn-block');
                        }
                    }

                    // change text size
                    if (obj.type === 'size') {
                        if ($('#id_type_0').is('checked')) {
                            sizeClass = ' text-' + obj.cls;
                        } else {
                            sizeClass = ' btn-' + obj.cls;
                        }
                        previewBtn.removeClass('text-lg text-md text-sm text-xs');
                        previewBtn.removeClass('btn-lg btn-md btn-sm btn-xs');
                        previewBtn.addClass(sizeClass);
                    }
                }

                // make sure we only pass the required class argument
                function cleanClass(cls) {
                    cls = cls
                        .replace('btn btn-', '')
                        .replace('active', '')
                        .replace('default ', '')
                        .replace('text-', '')
                        .replace(' ', '');
                    return cls;
                }

            },

            /**
             * Widget used in aldryn_bootstrap3/widgets/size.html.
             * Provides the choice to select the size of the element.
             * It can large, medium, small or extra small
             *
             * @method sizeWidget
             * @param {jQuery} element context element to render
             */
            sizeWidget: function sizeWidget(element) {
                var sizesInputs = element.find('label input');
                var selectedSizesInput;

                sizesInputs.each(function (index, item) {
                    var input = $(item);
                    var label = input.parent();

                    // Initial active state
                    if (input.prop('checked')) {
                        selectedSizesInput = input;
                        label.addClass('active');
                    }

                    // Set sizes
                    label.addClass('btn btn-default text-' + item.value);

                    // Add icon
                    $('<span class="glyphicon glyphicon-record"></span>')
                        .insertAfter(input);

                    // Set active states
                    label.on('click', function () {
                        var input = $(this).find('input');

                        selectedSizesInput.prop('checked', false);
                        input.prop('checked', true);

                        selectedSizesInput = input;
                    });

                });
            },

            /**
             * Plugin used in aldryn_bootstrap3/plugins/column and
             * aldryn_bootstrap3/plugins/row.
             *
             * @method rowColumnPlugin
             */
            rowColumnPlugin: function rowColumnPlugin() {
                var container = $('.aldryn-bootstrap3-grid');
                var formRows = container.find('.form-row');
                var fieldBoxes = container.find('.field-box');
                var form = $('#bootstrap3rowplugin_form');
                var tpl = $('<span class="form-row-icon fa fa-fw"></span>');

                // set tooltips and labels
                fieldBoxes.each(function(index, item) {
                    var el = $(item);
                    var tooltip = el.find('.help');
                    var label = el.find('label');
                    var labelText = label.text();

                    label.html(labelText.replace(':', ''));

                    // only create tooltip if one is present
                    if (tooltip.length) {
                        el.append('' +
                            '<span class="fa fa-question-circle" ' +
                            '   data-toggle="tooltip" ' +
                            '   data-placement="right" ' +
                            '   title="' + tooltip.text() + '">' +
                            '</span>');
                    }
                });

                formRows.each(function(index, item) {
                    var el = $(item);
                    // set fieldbox icons
                    if (el.hasClass('field-create_xs_col')) {
                        el.prepend(tpl.clone().addClass('fa-mobile'));
                    }
                    if (el.hasClass('field-create_sm_col')) {
                        el.prepend(tpl.clone().addClass('fa-tablet'));
                    }
                    if (el.hasClass('field-create_md_col')) {
                        el.prepend(tpl.clone().addClass('fa-laptop'));
                    }
                    if (el.hasClass('field-create_lg_col')) {
                        el.prepend(tpl.clone().addClass('fa-desktop'));
                    }
                    if (el.hasClass('field-create')) {
                        el.prepend(tpl.clone().addClass('fa-columns text-primary'));
                    }
                });

                // initialize tooltip
                $('[data-toggle="tooltip"]').tooltip();

                // browser validation gets in the way of the ajax
                // form submission from django-cms
                form.attr('novalidate', 'novalidate');
            },

            /**
             * Plugin used in aldryn_bootstrap3/plugins/image.
             *
             * @method imagePlugin
             */
            imagePlugin: function imagePlugin() {
                var image = $('#id_file_thumbnail_img');
                var imagePreview = $('.js-image-preview .image');
                var aspectRatio;
                var aspectRatioBase = 80;
                var url;

                var aspectRatioContext = $('#id_aspect_ratio');
                var shapeContext = $('#id_shape');
                var thumbnailContext = $('#id_thumbnail');
                var thumbnailTooltipText = thumbnailContext.parent().find('.help').text();
                var previewContainer = imagePreview.parent();

                // change image
                image.on('load', function () {
                    url = parseImage($(this).attr('src'));
                    imagePreview.css('background-image', 'url(' + url + ')');
                }).trigger('load');

                // attach aspect ratio handler
                aspectRatioContext.on('change', function () {
                    aspectRatio = aspectRatioContext.val().split('x');
                    imagePreview.css('height', aspectRatioBase * aspectRatio[1] / aspectRatio[0]);
                }).trigger('change');

                // attach shape handler
                shapeContext.on('change', function () {
                    imagePreview.removeClass('img-rounded img-circle');
                    previewContainer.removeClass('img-rounded img-circle');
                    imagePreview.addClass('img-' + $(this).val());
                    previewContainer.addClass('img-' + $(this).val());
                    // remove empty "img-" when selection is "-----"
                    imagePreview.removeClass('img-');
                    previewContainer.removeClass('img-');
                }).trigger('change');

                // attach shape handler
                thumbnailContext.on('change', function () {
                    if (thumbnailContext.is(':checked')) {
                        previewContainer.addClass('img-thumbnail');
                    } else {
                        previewContainer.removeClass('img-thumbnail');
                    }
                }).trigger('change');

                // tooltip handling
                thumbnailContext.parent().append('' +
                    '<span class="fa fa-question-circle" ' +
                    '   data-toggle="tooltip" ' +
                    '   data-placement="right" ' +
                    '   title="' + thumbnailTooltipText + '">' +
                    '</span>');

                // initialize tooltip
                $('[data-toggle="tooltip"]').tooltip();

                // image processing
                // /media/filer_public_thumbnails/filer_public/2d/2a/2d2a4d96-8a07-44b7-948b-dd1e7353342e/4855487.jpeg__48x48_q85_crop_subsampling-2_upscale.jpg
                // /media/filer_public/2d/2a/2d2a4d96-8a07-44b7-948b-dd1e7353342e/4855487.jpeg
                function parseImage(url) {
                    // trying to get the large size image with default filer options
                    if (url.indexOf('filer_public_thumbnails/') > -1) {
                        url = url.split('__')[0];
                        url = url.replace('filer_public_thumbnails/', '');
                    }
                    return url;
                }
            },

            /**
             * Plugin used in aldryn_bootstrap3/plugins/label.
             *
             * @method labelPlugin
             */
            labelPlugin: function labelPlugin() {
                var container = $('.aldryn-bootstrap3-label');
                var previewBtn = container.find('.js-label-preview span');
                var defaultBtnText = previewBtn.text();
                var timer = function () {};
                var timeout = 50;

                // helper references
                var labelContext = $('#id_label');
                var btnContext = $('.field-context');

                // attach event to the label
                labelContext.on('keydown', function () {
                    clearTimeout(timer);
                    timer = setTimeout(function () {
                        updatePreview({
                            type: 'text',
                            text: labelContext.val()
                        });
                    }, timeout);
                }).trigger('keydown');

                // handle button context selection
                // autotrigger will be handled by link/button switcher
                btnContext.find('label').on('click', function () {
                    updatePreview({
                        type: 'context',
                        cls: cleanClass($(this).attr('class'))
                    });
                });

                // initial state
                btnContext.find('label.active').trigger('click');

                // every event fires updatePreview passing in arguments what
                // has to be done
                function updatePreview(obj) {
                    // handle "label" inputs
                    if (obj.type === 'text') {
                        if (obj.text !== '') {
                            previewBtn.text(obj.text);
                        } else {
                            previewBtn.text(defaultBtnText);
                        }
                    }

                    // update context
                    if (obj.type === 'context') {
                        previewBtn.attr('class', 'label label-' + obj.cls);
                    }
                }

                // make sure we only pass the required class argument
                function cleanClass(cls) {
                    cls = cls
                        .replace('btn btn-', '')
                        .replace('active', '')
                        .replace('text-', '')
                        .replace(' ', '');
                    return cls;
                }
            }

        };

        // auto initialize widgets
        if ($('.aldryn-bootstrap3-context').length) {
            $('.aldryn-bootstrap3-context').each(function () {
                bootstrap3.contextWidget($(this));
            });
        }
        if ($('.aldryn-bootstrap3-icon').length) {
            $('.aldryn-bootstrap3-icon').each(function () {
                bootstrap3.iconWidget($(this));
            });
        }
        if ($('.aldryn-bootstrap3-button').length) {
            bootstrap3.buttonPreview();
        }
        if ($('.js-btn-group-sizes').length) {
            $('.js-btn-group-sizes').each(function () {
                bootstrap3.sizeWidget($(this));
            });
        }
        // auto initialize plugins
        if ($('.aldryn-bootstrap3-grid').length) {
            bootstrap3.rowColumnPlugin();
        }
        if ($('.aldryn-bootstrap3-label').length) {
            bootstrap3.labelPlugin();
        }
        if ($('#boostrap3imageplugin_form').length) {
            bootstrap3.imagePlugin();
        }
    });
})(window.jQuery || django.jQuery);
