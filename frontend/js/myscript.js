$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

$(function () {
    var _alphabets = $('.alphabet > a');
    var _contentRows = $('#assignments-table tbody tr, #mechanics-table tbody tr, #users-table tbody tr');

    _alphabets.click(function () {      
        var _letter = $(this), _text = $(this).text(), _count = 0;

        _alphabets.removeClass("active");
        _letter.addClass("active");

        _contentRows.hide();
        _contentRows.each(function (i) {
            var _cellText = $(this).children('td').eq(0).text().toUpperCase();
            if (RegExp('^' + _text).test(_cellText)) {
                _count += 1;
                $(this).fadeIn(400);
            }
        });                   
    });
});
