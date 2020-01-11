//cuando la web page termine de cargar, conectar los web socket

document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect(location.protocol + '//' + document.domain + ':')

    //cuando se conecte, donfigurar botones
    socket.on('connect', () => {
        //cada boton debe emitir un evento de "submit vote"
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.vote;
                socket.emit('submit vote', {'selection':selection});
            }
        });
    });

    //cuando un nuevo voto es anunciado, añadir a la unordered list
    socket.on('announce vote', data => {
        const li = document.createElement('li');
        li.innerHTML = 'Vote recorded: ${data.selection}';
        document.querySelector('#votes').append(li);
    });
});


