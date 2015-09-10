$(function() {

    //$('.module *').hide();
    //$('.module h3').show();
    $('.module img').hide();
    $('.droppable-modules').sortable({
        connectWith: '.droppable-modules', 
        placeholder: 'module-placeholder alert alert-warning',
        forcePlaceholderSize: true,
        dropOnEmpty: true,
        distance: 0.5,
    });
    $('.droppable-modules').disableSelection();

    $('#module-form').click(function() {
        var sidebar_left = $('.sidebar-left .module').map(function() {
            return $(this).attr('data-module');
        }).toArray();
        var topbar = $('.topbar .module').map(function() {
            return $(this).attr('data-module');
        }).toArray();
        var sidebar_right = $('.sidebar-right .module').map(function() {
            return $(this).attr('data-module');
        }).toArray();

        var data = {
            left_l: sidebar_left.join(','),
            top_l: topbar.join(','),
            right_l: sidebar_right.join(','),
        };
        $('#id_sidebar_left').val(data.left_l);
        $('#id_topbar').val(data.top_l);
        $('#id_sidebar_right').val(data.right_l);


        console.log(data);
    });

})
