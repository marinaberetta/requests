var socket = io();

console.log("oi!");

$('form').on('submit', function(e){
    socket.emit('sendMessage', $('#m').val());
    $('#m').val('');

    e.preventDefault();
});

socket.on('sendMessage', function(message) {
    $('#mensagens').append($('<li>').text(message));
});