$('#logModalBtn4').click(function (event) {
    event.preventDefault();

    let loginUrl = $(this).data('url');

    function bindFormSubmit() {
        $('#loginModal form').on('submit', function (event) {
            event.preventDefault();

            let formData = $(this).serialize();

            $.ajax({
                url: loginUrl,
                type: 'POST',
                data: formData,
                headers: {'X-Requested-With': 'XMLHttpRequest'},
                success: function (response) {
                    if (response.success) {
                        location.reload(); // Стандартный Вариант - перезагрузка на главную страницу !
                    } else {
                        $('#loginModal .modal-body').html(response.html);  // Ошибки !
                        bindFormSubmit();
                    }
                },
                error: function () {
                    alert('Ошибка при обработке запроса.');
                }
            });
        });
    }

    $.ajax({
        url: loginUrl,
        type: 'GET',
        success: function (response) {
            $('#loginModal .modal-body').html(response.html);
            $('#loginModal').modal('show');
            bindFormSubmit();
        },
        error: function () {
            alert('Ошибка при загрузке формы.');
        }
    });
});
