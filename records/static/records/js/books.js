$(function (){

  var loadform = function(){
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function(){
        $("#modal-book").modal("show");
      },
      success: function(data){
        $("#modal-book .modal-content").html(data.html_form);
      },
    });
  };

  var saveform = function(){
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list); // <-- Replace the table body with the updated list
          $("#modal-book").modal("hide");  // <-- Close the modal
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  // book create
  $(".js-create-book").click(loadform);
  $("#modal-book").on("submit", ".js-book-create-form",saveform);

  // Update book
  $("#book-table").on("click", ".js-book-update",loadform);
  $("#modal-book").on("submit", ".js-book-update-form",saveform);

  // Update book
  $("#book-table").on("click", ".js-book-delete",loadform);
  $("#modal-book").on("submit", ".js-book-delete-form",saveform);

});