$(document).ready(function() {
    function showOutput(data) {
        try {
            $("#output").text(JSON.stringify(JSON.parse(data), null, 4));
        }
        catch (e) {
            console.error(e);
            $("#output").text(data);
        }
    }

    var param_default = $(".param").clone();

    $("#add-param").click(function(e) {
        e.preventDefault();
        $("#param-list").append(param_default.clone());
    });

    $("#param-list").on("click", ".btn-danger", function(e) {
        e.preventDefault();
        $(this).closest(".param").remove();
    });

    $("#request button").click(function(e) {
        e.preventDefault();

        if (!$("#url").val() || $("#url").val() == "/") {
            $("#output").text("Please enter a valid API endpoint!");
            return;
        }

        var type = $(this).attr("id");

        var params = {};

        $("#param-list .param").each(function() {
            var key = $(this).find(".key").val();
            var v = $(this).find(".value").val();

            if (key) {
                params[key] = v;
            }
        });

        $.ajax({
            url: $("#url").val(),
            method: type,
            data: params,
            dataType: "text",
            success: function(data) {
                showOutput(data);
            },
            error: function(xhr, status, error) {
                showOutput(xhr.responseText);
            }
        });
    });
    $("#examples button").click(function(e) {
        e.preventDefault();

        $("#url").val($(this).attr("data-endpoint"));
        $(".param .btn-danger").click();

        var keys = $(this).attr("data-data");
        if (keys) {
            keys = keys.split(",");
            while ($(".param").length < keys.length) {
                $("#add-param").click();
            }
            var fields = $(".key");
            for (var i = 0; i < keys.length; i++) {
                fields.eq(i).val(keys[i]);
            }
        }

        var method = $(this).attr("data-method");

        if (method) {
            $("#" + method).click();
        }
    });
});
