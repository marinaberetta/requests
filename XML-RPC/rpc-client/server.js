var xmlrpc = require('xmlrpc')

var client = xmlrpc.createClient({ host: 'localhost', port: 9000, path: '/'})

client.methodCall('now', null, function (error, value) {
    var data = new Date(value);

    // Results of the method response
    console.log('Resposta do método NOW do Python: ' + data.toLocaleDateString("en-US", {day: 'numeric', month: 'numeric', year: 'numeric'}))
});

client.methodCall('ping', null, function (error, value) {
    // Results of the method response
    console.log('Resposta do método PING do Python: ' + value)
})

client.methodCall('sum', [{"a": 60, "b": 20}], function (error, value) {
    // Results of the method response
    console.log('Resposta do método sum do Python: ' + value)
})