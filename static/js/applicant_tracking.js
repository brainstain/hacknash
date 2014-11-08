

$(document).ready(function () {

    $("#interviewed_by_div").hide();

    $('.date').each(function () {

        $(this).datepicker({"format": "yyyy-mm-dd", "now": true});

    });


    $("#previously_interviewed").click(function () {

        $("#interviewed_by_div").toggle(this.checked);

        $("#interviewed_by").focus();

    });

});