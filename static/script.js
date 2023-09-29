// Função para obter e exibir a hora de São Paulo
function getCurrentTime() {
    // Use uma requisição AJAX para buscar a hora da API
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo', true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            // Analisa a resposta JSON
            const response = JSON.parse(xhr.responseText);

            // Extrai a data e hora da resposta
            const datetime = response.datetime;

            // Exibe a hora no elemento 'current-time'
            const currentTimeElement = document.getElementById('current-time');
            currentTimeElement.textContent = `Hora atual em São Paulo: ${datetime}`;
        }
    };

    xhr.send();
}

// Chame a função para obter a hora quando a página carregar
window.onload = function () {
    getCurrentTime();
};
