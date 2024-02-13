// GetCommune by Province_id for zone form
$(function() {
    $('#province_id').on("change", function () {
        province_id = $(this).val();
        //alert(province_id);
        $.get(
            "/admin/templates/zones/getCommunes",
            {
                province_id: province_id,
            },
            function (data, textStatus, jqXHR) {
                $("#id_commune").html(data);
            }
        );
    } );
});  

// GetCommune by Province_id for cabinet form
$(function() {
    $('#id_province').on("change", function () {
        province_id = $(this).val();
        //alert(province_id);
        $.get(
            "/admin/templates/cabinets/getCommunes",
            {
                province_id: province_id,
            },
            function (data, textStatus, jqXHR) {
                $("#id_commune").html(data);
            }
        );
    } );
});  

// GetCommune by Province_id for zone form
$(function() {
    $('#commune_id').on("change", function () {
        commune_id = $(this).val();
       // alert(commune_id);
        $.get(
            "/admin/templates/cabinets/getZones",
            {
                commune_id: commune_id,
            },
            function (data, textStatus, jqXHR) {
                $("#id_zone").html(data);
            }
        );
    } );
});  