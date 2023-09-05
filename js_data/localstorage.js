it.only('expectation', function (client) {
    client.url('lanhuapp.com').execute(function(data) {
        try {
            // statements
            localStorage.iseedeadpeople = 1
            console.log('local', localStorage)
        } catch(e) {
            // statements
            console.log(e);
        }
        return true;
    }, [], function(result) {
    });
    client.pause(0);
});