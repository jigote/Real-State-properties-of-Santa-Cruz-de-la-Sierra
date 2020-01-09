//cuando la web page termine de cargar, conectar los web socket

document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect(location.protocol + '//' + document.domain + ':')
})

