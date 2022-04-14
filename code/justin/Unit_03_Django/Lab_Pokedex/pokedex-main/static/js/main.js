function GetCsrfToken() {
    let csrf_element = document.querySelector('[name=csrfmiddlewaretoken]');
    let csrf_token = 'TokenNotFound';
    if (csrf_element != null) {
        csrf_token = csrf_element.value;
    }
    return csrf_token;
}
const csrftoken = GetCsrfToken();

M.AutoInit();