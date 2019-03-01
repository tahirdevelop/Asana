function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(document).ready(function () {

    $('.submit').bind('click', function () {
        $.ajax({
            url: "",
            type: "POST",
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'fullName': $('#id_fullName').val(),
                'email': $('#id_email').val(),
                'phoneNumber': $('#id_phoneNumber').val(),
                'company': $('#id_company').val(),
                'message': $('#id_message').val()
            }
        });
    });

    $(".submit").click(function () {
        $(".submit").addClass("loading");
        setTimeout(function () {
            $(".submit").addClass("hide-loading");
            $(".done").addClass("finish");
        }, 1000);
        setTimeout(function () {
            $(".submit").removeClass("loading");
            $(".submit").removeClass("hide-loading");
            $(".done").removeClass("finish");
            $(".failed").removeClass("finish");
        }, 2500);
    })

});