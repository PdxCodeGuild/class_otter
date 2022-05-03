function FindIndexByID(itemList, itemID) {
    for (let i = 0; i < itemList.length; i++) {
        if (itemList[i].id == itemID) {
            return i;
        }
    }

    return -1;
}

function FindIndexByAttribute(itemList, attributeName, itemAttribute) {
    for (let i = 0; i < itemList.length; i++) {
        if (itemList[i][attributeName] == itemAttribute) {
            return i;
        }
    }

    return -1;
}

function FindIndexByValue(itemList, itemValue) {
    for (let i = 0; i < itemList.length; i++) {
        if (itemList[i] == itemValue) {
            return i;
        }
    }

    return -1;
}

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