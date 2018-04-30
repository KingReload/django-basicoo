$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });

    if (window.location.pathname.startsWith('/update-styles/')) {

        $(".jscolor").each(function() {
            $(this).addClass("form-control")
        });

        var save = document.getElementById("id_save_template").checked;

        if (save) {
            $("#id_template_name").prop('required', true);
            $(".template_name").show();
        } else {
            $("#id_template_name").prop('required', false);
            $(".template_name").hide();
        }
        
        $("#id_save_template").click(function () {
            var save = document.getElementById("id_save_template").checked;

            if (save) {
                $("#id_template_name").prop('required', true);
                $(".template_name").show();
            } else {
                $("#id_template_name").prop('required', false);
                $(".template_name").hide();
            }
        });
    }
});

$(function () {
    var _alphabets = $('.alphabet > a');
    var _contentRows = $('#table-control tbody tr');

    _alphabets.click(function () {
        var _letter = $(this),
            _text = $(this).text(),
            _count = 0;

        _alphabets.removeClass("active");
        _letter.addClass("active");

        _contentRows.hide();
        _contentRows.each(function (i) {
            var _cellText = $(this).children('td').eq(0).text().toUpperCase();
            if (RegExp('^' + _text).test(_cellText)) {console.log(this);
                _count += 1;
				$(this).fadeIn(400);
            }
        });
    });
});
