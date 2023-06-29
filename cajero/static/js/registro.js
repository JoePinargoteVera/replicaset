// registro.js

function registrarCliente() {
  // Obtener los valores de los campos de entrada
  const nombre = document.getElementById('nombre').value;
  const cedula = document.getElementById('cedula').value;
  const clave = document.getElementById('clave').value;
  const saldo = document.getElementById('saldo').value;

  // Crear un objeto con los datos del cliente
  const data = {
    nombre,
    cedula,
    clave,
    saldo
  };

  // Realizar la solicitud POST al servidor
  fetch('/clientes', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(responseData => {
      // Mostrar la respuesta del servidor
      console.log(responseData);

      // Actualizar la interfaz con los datos del cliente registrado
      const clienteRegistrado = responseData;
      const clienteInfo = document.getElementById('cliente-info');

      const urlRedireccion = `/login`;

      // Redirigir al usuario a la URL construida
      window.location.href = urlRedireccion;
    })
    .catch(error => {
      console.error('Error al registrar el cliente:', error);
    });
}
