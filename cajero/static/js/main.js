document.getElementById('formularioIngreso').addEventListener('submit', function(event) {
    event.preventDefault();
    const montoIngreso = document.getElementsByName('montoIngreso')[0].value;
    const cedula = document.getElementById('cedula').textContent;
    const data = { cedula: cedula, monto: montoIngreso };
    console.log(data);
    fetch('/ingresos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Actualizar el saldo mostrado en la página
        const { nuevoSaldo } = data; 
        console.log(data);
        document.getElementById('saldo').textContent = nuevoSaldo;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('formularioEgreso').addEventListener('submit', function(event) {
    event.preventDefault();
    const montoEgreso = document.getElementsByName('montoEgreso')[0].value;
    const cedula = document.getElementById('cedula').textContent;
    const data = { cedula: cedula, monto: montoEgreso };

    fetch('/egresos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {

        // Actualizar el saldo mostrado en la página
        document.getElementById('saldo').textContent = data.nuevoSaldo;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
