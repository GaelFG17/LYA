function buscarSolucionBFS() {
    var estadoInicial = document.getElementById('estadoInicial').value;
    var solucion = document.getElementById('solucion').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/buscar', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Convertir la respuesta JSON a un objeto JavaScript
            var response = JSON.parse(xhr.responseText);
            // Actualizar el contenido de la página con el resultado recibido
            document.getElementById('resultado').innerHTML = '<h1>Resultado de la búsqueda:</h1><ul>';
            response.resultado.forEach(function(item) {
                document.getElementById('resultado').innerHTML += '<li>' + item + '</li>';
            });
            document.getElementById('resultado').innerHTML += '</ul>';
        }
    };
    xhr.send("estado_inicial=" + estadoInicial + "&solucion=" + solucion);
}

function buscarVuelos() {
    var estadoInicial = document.getElementById('estadoInicial').value;
    var solucion = document.getElementById('solucion').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/vuelos', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Convertir la respuesta JSON a un objeto JavaScript
            var response = JSON.parse(xhr.responseText);
            // Actualizar el contenido de la página con el resultado recibido
            document.getElementById('resultado').innerHTML = '<h1>Resultado de la búsqueda:</h1><ul>';
            response.resultado.forEach(function(item) {
                document.getElementById('resultado').innerHTML += '<li>' + item + '</li>';
            });
            document.getElementById('resultado').innerHTML += '</ul>';
        }
    };
    xhr.send("estado_inicial=" + estadoInicial + "&solucion=" + solucion);
}

function buscarDFS() {
    var estadoInicial = document.getElementById('estadoInicial').value;
    var solucion = document.getElementById('solucion').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/DFS', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Convertir la respuesta JSON a un objeto JavaScript
            var response = JSON.parse(xhr.responseText);
            // Actualizar el contenido de la página con el resultado recibido
            document.getElementById('resultado').innerHTML = '<h1>Resultado de la búsqueda:</h1><ul>';
            response.resultado.forEach(function(item) {
                document.getElementById('resultado').innerHTML += '<li>' + item + '</li>';
            });
            document.getElementById('resultado').innerHTML += '</ul>';
        }
    };
    xhr.send("estado_inicial=" + estadoInicial + "&solucion=" + solucion);
}

function buscarDFSI() {
    var estadoInicial = document.getElementById('estadoInicial').value;
    var solucion = document.getElementById('solucion').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/DFSI', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Convertir la respuesta JSON a un objeto JavaScript
            var response = JSON.parse(xhr.responseText);
            // Actualizar el contenido de la página con el resultado recibido
            document.getElementById('resultado').innerHTML = '<h1>Resultado de la búsqueda:</h1><ul>';
            response.resultado.forEach(function(item) {
                document.getElementById('resultado').innerHTML += '<li>' + item + '</li>';
            });
            document.getElementById('resultado').innerHTML += '</ul>';
        }
    };
    xhr.send("estado_inicial=" + estadoInicial + "&solucion=" + solucion);
}

function buscarDFSR() {
    var estadoInicial = document.getElementById('estadoInicial').value;
    var solucion = document.getElementById('solucion').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/DFSR', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Convertir la respuesta JSON a un objeto JavaScript
            var response = JSON.parse(xhr.responseText);
            // Actualizar el contenido de la página con el resultado recibido
            document.getElementById('resultado').innerHTML = '<h1>Resultado de la búsqueda:</h1><ul>';
            response.resultado.forEach(function(item) {
                document.getElementById('resultado').innerHTML += '<li>' + item + '</li>';
            });
            document.getElementById('resultado').innerHTML += '</ul>';
        }
    };
    xhr.send("estado_inicial=" + estadoInicial + "&solucion=" + solucion);
}

function buscarDK() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/DK', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Convertir la respuesta JSON a un objeto JavaScript
            var response = JSON.parse(xhr.responseText);
            // Actualizar el contenido de la página con el resultado recibido
            document.getElementById('resultado').innerHTML = '<h1>Resultado de la búsqueda:</h1><p>' + response.resultado + '</p>';
        }
    };
    xhr.send();
}