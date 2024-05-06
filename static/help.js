// Открытие popup окна при клике на кнопку "Help"
document.getElementById("helpButton").addEventListener("click", function() {
    document.getElementById("popup").style.display = "block";

    // Добавляем обработчик события клика для закрытия popup окна при клике вне него
    document.addEventListener("click", closePopupOutside);
});

// Закрытие popup окна
function closePopup() {
    document.getElementById("popup").style.display = "none";
    // Удаляем обработчик события клика при закрытии popup окна
    document.removeEventListener("click", closePopupOutside);
}

// Закрытие popup окна при клике вне него
function closePopupOutside(event) {
    var popup = document.getElementById("popup");
    if (event.target !== popup && !popup.contains(event.target)) {
        closePopup();
    }
}
