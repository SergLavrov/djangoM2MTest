$(function() {
$('#logModal3').click(function (event) {
  event.preventDefault();

  let loginUrl = $(this).data('url');
  let csrfToken = $(this).data('csrf-token');

  function bindFormSubmit() {
      $('#loginModal form').submit(function (event) {
          event.preventDefault();

          let formData = $(this).serialize();

          $.ajax({
              url: loginUrl,
              type: 'POST',
              data: formData,
              headers: {
                  'X-CSRFToken': csrfToken,
                  // {#'X-Requested-With': 'XMLHttpRequest'#}
              },
              dataType: 'json',   // <--- важно!
              success: function (response) {
                  if (response.success) {
                      location.reload();
                  } else {
                      $('#loginModal .modal-body').html(response.html);
                      bindFormSubmit();
                  }
              },
              error: function () {
                  alert('Ошибка при входе в систему.');
              }
          });
      });
  }

  $.ajax({
      url: loginUrl,
      type: 'GET',
      success: function (response) {
          $('#loginModal .modal-body').html(response);
          $('#loginModal').modal('show');
          bindFormSubmit();
      },
      error: function () {
          alert('Ошибка при загрузке формы.');
      }
  });
});
});





// {/*$('#regModal3').click(function (event) {*/}
// {/*    event.preventDefault();*/}
// {/*    let registerUrl = $(this).data('url');*/}
// {/*    let csrfToken = $(this).data('csrf-token');*/}
// {/*    // Загрузка формы в модальное окно*/}
// {/*    $.ajax({*/}
// {/*        url: registerUrl,*/}
// {/*        type: 'GET',*/}
// {/*        success: function (response) {*/}
// {/*            $('#registerModal .modal-body').html(response);*/}
// {/*            $('#registerModal').modal('show');*/}
// {/*            // Обработка отправки формы*/}
// {/*            $('#registerModal form').submit(function (event) {*/}
// {/*                event.preventDefault();*/}
// {/*                let formData = $(this).serialize();*/}
// {/*                $.ajax({*/}
// {/*                    url: registerUrl,*/}
// {/*                    type: 'POST',*/}
// {/*                    data: formData + '&csrfmiddlewaretoken=' + csrfToken,*/}
// {/*                    success: function (response) {*/}
// {/*                        if (response.indexOf('alert-danger') === -1) {*/}
// {/*                            location.reload(); // Успешная регистрация*/}
// {/*                        } else {*/}
// {/*                            $('#registerModal .modal-body').html(response); // Ошибки*/}
// {/*                        }*/}
// {/*                    },*/}
// {/*                    error: function () {*/}
// {/*                        alert('Ошибка при обработке запроса.');*/}
// {/*                    }*/}
// {/*                });*/}
// {/*            });*/}
// {/*        },*/}
// {/*        error: function () {*/}
// {/*            alert('Ошибка при загрузке формы.');*/}
// {/*        }*/}
// {/*    });*/}
// {/*});*/}