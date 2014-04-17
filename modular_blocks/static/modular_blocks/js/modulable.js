$(function() {

    $('.module *').hide();
    $('.module h3').show();
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
        var sidebar_right = $('.sidebar-right .module').map(function() {
            return $(this).attr('data-module');
        }).toArray();

        var data = {
            left: sidebar_left.join(','),
            right: sidebar_right.join(','),
        };
        $('#id_sidebar_left').val(data.left);
        $('#id_sidebar_right').val(data.right);


        console.log(data);
    });

})
