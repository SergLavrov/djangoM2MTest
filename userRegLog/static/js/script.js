$(document).ready(function () {
  $('#openRegisterModal').click(function (e) {
    e.preventDefault();
    $.get('/register/', function (data) {
      $('#registerModalBody').html(data);
      $('#registerModal').modal('show');
      bindRegisterForm();
    });
  });

  function bindRegisterForm() {
    $('#registerModal form').submit(function (e) {
      e.preventDefault();
      $.ajax({
        url: '/register/',
        type: 'POST',
        data: $(this).serialize(),
        success: function (data) {
          if (data.success) {
            $('#registerModal').modal('hide');
            location.reload(); // или показать сообщение об успехе
          } else {
            $('#registerModalBody').html(data);
            bindRegisterForm(); // повторно привязать обработчик
          }
        },
        error: function () {
          alert('Ошибка при регистрации.');
        }
      });
    });
  }
});