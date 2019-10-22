function setCookie(name, value, options = {}) {

  options = {
    path: '/',
    'max-age': 3600,
    expires: new Date(),
  };

  if (options.expires) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  })
}

function disableCheckboxes() {
  $('.check').each(function() {
    $(this).attr('disabled', true);
  });
  $('.save-btn').text('Очистить хранилище').click(() => {
    localStorage.clear();
    location.reload();
  });
}

function disableInput() {
  let cityName = `${getCookie('city').charAt(0).toUpperCase() + getCookie('city').slice(1).toLowerCase()}`;
  console.log(cityName);
  $('#cityInput').val(cityName);
  $('#cityInput').attr('disabled', true);
}
// Загрузка страницы
$(document).ready(function() {
  // Задание 1
  // Проверить запись города в куки, убрать поле ввода и показать город из куки
  if(getCookie('city')) {
    disableInput();
    $('.submit-btn').text('Сбросить куки').click(() => {
      deleteCookie('city');
      location.reload();
    });
  }
  // Задание 2
  // Смотрим по всем ключам в localStorage
  if (localStorage.key('checked')) disableCheckboxes();
  $.each(localStorage, function(key, value='checked') {
    if (localStorage.key(value)) {
      $(`#${key}`).attr(value, true);
    };
  });
});

$('#cityInput').on('keypress', function(event) {
if (event.keyCode === 13) {
  event.preventDefault();
  $('.submit-btn').click();
}
});
// Запись названия города в куки
$('.submit-btn').click(() => {
  setCookie('city', $('#cityInput').val());
  location.reload();
});
// Сохранить состояние чек-боксов в localStorage
$('.save-btn').click(() => {
  $('.check').each(function() {
    if ($(this).prop('checked')) {
      console.log(this.id);
      localStorage.setItem(this.id, 'checked');
    };
    disableCheckboxes();
  });
});
