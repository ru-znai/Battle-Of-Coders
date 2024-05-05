document.addEventListener('DOMContentLoaded', () => {
    const popupContainer = document.getElementById('popupContainer');

    // Список текстов для всплывающих надписей
    const hints = [
        "First hint message",
        "Second hint message",
        "Third hint message"
    ];

    // Функция для создания и отображения всплывающих надписей
    function showHints() {
        hints.forEach((hint, index) => {
            const popupText = document.createElement('div');
            popupText.className = 'popup-text';
            popupText.textContent = hint;

            setTimeout(() => {
                popupText.classList.add('show');
                setTimeout(() => {
                    popupText.style.top = '-100%'; // После отображения сдвигаем надпись вверх
                }, 2000); // Настройка времени отображения
            }, index * 3000); // Задержка перед показом следующей надписи

            popupContainer.appendChild(popupText);
        });
    }

    // Запускаем функцию показа всплывающих надписей при загрузке страницы
    showHints();
});
