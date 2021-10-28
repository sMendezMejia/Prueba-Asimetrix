$(document).ready(function () {
  $("#lesionTipoDrop").selectpicker();
  $("#granjaDrop").selectpicker();
});

function replace_page_param_url(new_page_number) {
  let url = new URL(window.location.href);
  let search_params = url.searchParams;
  search_params.set("page", String(new_page_number));
  url.search = search_params.toString();
  let new_url = url.toString();
  console.log(new_url);
  window.location.href = new_url;
  return new_url;
}

function fill_multiple_dropdowns() {
  let url = new URL(window.location.href);
  let lesionTipos_params = url.searchParams.getAll("lesionTipos");
  let granjas_params = url.searchParams.getAll("granjas");
  if (lesionTipos_params) {
    $.each(lesionTipos_params, function (i, e) {
      $("#lesionTipoDrop option[value='" + e + "']").prop("selected", true);
    });
  }
  if (granjas_params) {
    $.each(granjas_params, function (i, e) {
      $("#granjaDrop option[value='" + e + "']").prop("selected", true);
    });
  }
}
// Se llenan los dropdowns con los anteriores filtros usados al cargar la página
fill_multiple_dropdowns();

