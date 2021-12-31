$('.x_title').on('click', function () {
    var $BOX_PANEL = $(this).closest('.x_panel'),
        $ICON = $(this).find('.collapse-link i'),
        $BOX_CONTENT = $BOX_PANEL.find('.x_content');

    // fix for some div with hardcoded fix class
    if ($BOX_PANEL.attr('style')) {
        $BOX_CONTENT.slideToggle(200, function () {
            $BOX_PANEL.removeAttr('style');
        });
    } else {
        $BOX_CONTENT.slideToggle(200);
        $BOX_PANEL.css('height', 'auto');
    }

    $ICON.toggleClass('fa-chevron-up fa-chevron-down');
});

$('body').tooltip({
    selector: '[data-toggle="tooltip"]'
});