$("#calculation").click(function () {
    if ($("#calculation").html() === "Başla") {
        $("#calculation").html("Bitir");
        $("#calculation").removeClass("btn-warning");
        $("#calculation").addClass("btn-danger");
        $("#calculationSide").append(
            `
            <div class="d-flex justify-content-between pb-5" id="hideSide">
                <input type="number" name="numberOfPage" id="numberOfPage" class="border rounded" style="width: 39%;">
                <input type="number" name="numberOfDay" id="numberOfDay" class="border rounded" style="width: 39%">
                <button type="button" name="calculate" class="btn text-light bg-info" id="calculate" style="width: 20%">Hesabla</button>
            </div>
            `
        );
        $("#calculate").click(function () {
            $("#infoAlert").remove();
            var numberOfPage = $("#numberOfPage").val();
            var numberOfDay = $("#numberOfDay").val();
            if (numberOfPage > 0 && numberOfDay > 0) {
                var result = Math.ceil(numberOfPage / numberOfDay);
                $("#calculationSide").prepend(
                    `
                    <div class="alert alert-success py-4 mb-5 text-center fs-5" role="alert" id="infoAlert">
                       Hər gün ən az səhifə <span id="page"></span> oxumalısınız!
                    </div>
                    `
                );
                $("#page").html(result).addClass("fs-3 fw-bold");
            }
            else {
                $("#calculationSide").prepend(
                    `
                    <div class="alert alert-danger py-4 mb-5 text-center fs-5" role="alert" id="infoAlert">
                        Hesablamada xəta baş verdi!
                    </div>
                    `
                );
            }
        });
    }
    else {
        $("#calculation").html("Başla");
        $("#calculation").removeClass("btn-danger");
        $("#calculation").addClass("btn-warning");
        $("#hideSide").remove();
        $("#infoAlert").remove();
    }
})
