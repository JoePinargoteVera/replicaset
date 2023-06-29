from flask import Flask, request, jsonify, abort, render_template
from models import db, Cliente, Ingreso, Egreso


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://grupo5:grupo5@grupo5.irpvnoz.mongodb.net/?retryWrites=true&w=majority',
    'db': 'bank'
}

db.init_app(app)


@app.route('/')
def inicio():
    return render_template('login.html')

# Ruta para registrar un cliente


@app.route('/clientes', methods=['POST'])
def registrar_cliente():
    data = request.get_json()
    nombre = data.get('nombre')
    cedula = data.get('cedula')
    clave = data.get('clave')
    saldo = data.get('saldo')

    cliente = Cliente(nombre=nombre, cedula=cedula, clave=int(clave), saldo=int(saldo))
    cliente.save()

    return jsonify({
        'nombre': nombre,
        'cedula': cedula,
        'saldo': saldo, 
        'message': 'Cliente registrado correctamente'})

# Ruta para buscar un cliente por su cédula


@app.route('/clientes/<cedula>', methods=['GET'])
def buscar_cliente(cedula):
    cliente = Cliente.objects(cedula=cedula).first()

    if cliente:
        return jsonify({
            'nombre': cliente.nombre,
            'cedula': cliente.cedula,
            'saldo': cliente.saldo
        })
    else:
        return jsonify({'message': 'Cliente no encontrado'})

# Ruta para actualizar el saldo de un cliente


@app.route('/clientes/<cedula>', methods=['PUT'])
def actualizar_saldo(cedula):
    data = request.get_json()
    nuevo_saldo = data.get('saldo')

    cliente = Cliente.objects(cedula=cedula).first()

    if cliente:
        cliente.saldo = nuevo_saldo
        cliente.save()

        return jsonify({'message': 'Saldo actualizado correctamente'})
    else:
        return jsonify({'message': 'Cliente no encontrado'})

# Ruta para registrar un ingreso


@app.route('/ingresos', methods=['POST'])
def registrar_ingreso():
    data = request.get_json()
    cedula = data.get('cedula')
    monto = data.get('monto')

    cliente = Cliente.objects(cedula=cedula).first()

    if cliente:
        ingreso = Ingreso(cliente=cliente, monto=monto)
        ingreso.save()
        monto_int = int(monto)
        cliente.saldo += monto_int
        nuevoSaldo = cliente.saldo
        cliente.save()

        return jsonify({'nuevoSaldo': nuevoSaldo})
    else:
        return jsonify({'message': 'Cliente no encontrado'})

# Ruta para registrar un egreso


@app.route('/egresos', methods=['POST'])
def registrar_egreso():
    data = request.get_json()
    cedula = data.get('cedula')
    monto = data.get('monto')

    cliente = Cliente.objects(cedula=cedula).first()

    if cliente:
        egreso = Egreso(cliente=cliente, monto=monto)
        egreso.save()

        monto_int = int(monto)
        cliente.saldo -= monto_int
        nuevoSaldo = cliente.saldo
        cliente.save()
        return jsonify({'nuevoSaldo': nuevoSaldo})
    else:
        return jsonify({'message': 'Cliente no encontrado'})

# Ruta para validar el cliente


@app.route('/clientes/validar', methods=['POST'])
def validar_cliente():
    data = request.get_json()
    cedula = data.get('cedula')
    clave = data.get('clave')

    try:
        cliente = Cliente.objects.get(cedula=cedula, clave=clave)
    except Cliente.DoesNotExist:
        # El cliente no existe
        abort(404, 'El cliente no existe o las credenciales son incorrectas.')

    return jsonify({
        # '_id':cliente._id,
        'nombre': cliente.nombre,
        'cedula': cliente.cedula,
        'saldo': cliente.saldo
    })

@app.route('/home')
def home():
    nombre = request.args.get('nombre')
    cedula = request.args.get('cedula')
    saldo = request.args.get('saldo')

    # Aquí puedes utilizar los valores como desees
    # Por ejemplo, puedes pasarlos al template para mostrarlos en la página

    return render_template('home.html', nombre=nombre, cedula=cedula, saldo=saldo)

@app.route('/ingreso', methods=['GET'])
def ingreso():
    return render_template('ingreso.html')

if __name__ == '__main__':
    app.run()
