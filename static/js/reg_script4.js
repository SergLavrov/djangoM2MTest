$('#regModalBtn4').click(function (event) {
    event.preventDefault();

    let registerUrl = $(this).data('url');

    function bindFormSubmit() {
        $('#registerModal form').on('submit', function (event) {
            event.preventDefault();

            let formData = $(this).serialize();

            $.ajax({
                url: registerUrl,
                type: 'POST',
                data: formData,
                headers: {'X-Requested-With': 'XMLHttpRequest'},
                success: function (response) {
                    if (response.success) {
                        // Вариант 3: КРАСИВО - тоже понравилось !!!
                        // Результат:
                        // После успешной регистрации модалка закрывается.
                        // Сверху страницы появляется зелёный Alert с сообщением.
                        // Через 3 секунды он автоматически исчезает (или пользователь может закрыть вручную).
                        $('#registerModal').modal('hide'); // закрываем модалку
                        // создаём алерт
                        let alertHtml = `
                              <div class="alert alert-success alert-dismissible fade show shadow" role="alert">
                                    Регистрация прошла успешно!
                                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                              </div> `;
                        $('#alertContainer').html(alertHtml); // Добавляем контейнер в шаблон home4.html после <body>
                        // автозакрытие через 3 секунды
                        setTimeout(function () {
                            $('#alertContainer .alert').alert('close');
                        }, 3000);

                        // Вариант 2: Inline сообщение прямо в модалке ! КРАСИВО - понравилось !!!
                        // {#$('#registerModal .modal-body').html(`#}
                        // {#<div class="alert alert-success">Регистрация прошла успешно!#}
                        // {#</div> `); #}

                        // {#location.reload(); // Стандартный Вариант - перезагрузка на главную страницу !#}

                        // {#window.location.href = '/reg/reg_success/'; // Вариант 1 через шаблон reg_success.html #}
                    } else {
                        $('#registerModal .modal-body').html(response.html);  // Ошибки !
                        bindFormSubmit();
                    }
                },
                error: function () {
                    alert('Ошибка при обработке запроса.');
                }
            });
        });
    }

    // Загружаем форму в модалку:
    $.ajax({
        url: registerUrl,
        type: 'GET',
        success: function (response) {
            $('#registerModal .modal-body').html(response.html);
            $('#registerModal').modal('show');  // показываем модалку
            bindFormSubmit();                   // привязываем обработчик формы
        },
        error: function () {
            alert('Ошибка при загрузке формы.');
        }
    });
});
