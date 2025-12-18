$('#register').click(function (event) {
    event.preventDefault();
    let registerUrl = $(this).data('url');
    let csrfToken = $(this).data('csrf-token');

    // Загрузка формы в модальное окно
    $.ajax({
        url: registerUrl,
        type: 'GET',
        success: function (response) {
            $('#registerModal .modal-body').html(response);
            $('#registerModal').modal('show');

            // Обработка отправки формы
            $('#registerModal form').submit(function (event) {
                event.preventDefault();
                let formData = $(this).serialize();

                $.ajax({
                    url: registerUrl,
                    type: 'POST',
                    data: formData + '&csrfmiddlewaretoken=' + csrfToken,
                    success: function (response) {
                        if (response.indexOf('alert-danger') === -1) {
                            location.reload(); // Успешная регистрация
                        } else {
                            $('#registerModal .modal-body').html(response); // Ошибки
                        }
                    },
                    error: function () {
                        alert('Ошибка при обработке запроса.');
                    }
                });
            });
        },
        error: function () {
            alert('Ошибка при загрузке формы.');
        }
    });
});