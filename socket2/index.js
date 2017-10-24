var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
    res.sendfile('index.html');
});

io.on('connection', function(socket) {
   console.log('Novo usuário conectado!');

   socket.on('disconnect', function() {
       console.log("O usuário foi desconectado");
   });

   socket.on('sendMessage', function(message) {
       io.emit('sendMessage', 'Mensagem: ' + message);
   });
});

http.listen(3000, function(){
    console.log('listening on *:3000');
});