from flask import Flask, request, render_template
from bebidas import Cerveza, Refresco, Te;

app = Flask(__name__,template_folder='html')

@app.route("/")
def Bebidas():
    return render_template("start_Bebidas.html")

@app.route("/Bebidas", methods=['POST'])
def mostrar_Bebidas():
 # Obtener la Bebida seleccionada por el usuario
    bebida= request.form["Bebida"]
    precio = request.form["precio"]
    if bebida == "Cerveza":
        tercera_var = request.form["tipo_cerveza"]
        Bebida_ingresada = Cerveza(bebida, precio, tercera_var)
    elif bebida == "Refresco":
        tercera_var = request.form["sabor"]
        Bebida_ingresada = Refresco(bebida, precio, tercera_var)
    elif bebida == "te":
        tercera_var = request.form["variedad"]
        Bebida_ingresada = Te(bebida, precio, tercera_var)
 # Renderizar la página de Bebidas con la Bebida seleccionada
    return render_template("Bebidas.html", Bebida=Bebida_ingresada)


if __name__ == '__main__':
   app.run(debug=True)