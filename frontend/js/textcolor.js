/*
$(".dropdown-toggle").click(function() {
    $(".dropdown-toggle").each(function() {
        if ($(this).parent().hasClass('open')) {
            $(this).css('cssText', 'color: ');
        }
    });
});

$(".dropdown-toggle, .dropdown-menu").mouseover(function() {
    if ($(this).parent().toggleClass('open')) {
        if ($(this).hasClass('dropdown-toggle')) {
            var hex = getRGB($(this).css('background'));
        } else {
            var parent = $($(this).parent()[0]).children('a')[0];
            var hex = getRGB($(parent).css('background'));
        }

        var o = Math.round(((parseInt(hex['red']) * 299) +
            (parseInt(hex['green']) * 587) +
            (parseInt(hex['blue']) * 114)) / 1000);

        var fore = (o > 125) ? 'black' : 'white';

        if ($(this).hasClass('dropdown-toggle')) {
            $(this).css('cssText', 'color: ' + fore + ' !important;');
        } else {
            $(parent).css('cssText', 'color: ' + fore + ' !important;');
        }
    }
});

$(".dropdown-toggle, .dropdown-menu").mouseleave(function() {
    if (!$(this).parent().hasClass('open')) {
        if ($(this).hasClass('dropdown-toggle')) {
            $(this).css('cssText', 'color: ');
        } else {
            var parent = $($(this).parent()[0]).children('a')[0];
            $(parent).css('cssText', 'color: ');
        }
    }
});

function getRGB(str){
    var match = str.match(/rgba?\((\d{1,3}), ?(\d{1,3}), ?(\d{1,3})\)?(?:, ?(\d(?:\.\d?))\))?/);
    return match ? {
        red: match[1],
        green: match[2],
        blue: match[3]
    } : {};
}
*/
