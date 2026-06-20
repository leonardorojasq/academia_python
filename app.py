from flask import redirect, url_for
from app import create_app

app = create_app()


#print(app.url_map)


# @app.route("/docs")
# def docs():

#     rutas = []

#     for rule in app.url_map.iter_rules():

#         rutas.append({
#             "ruta": str(rule),
#             "endpoint": rule.endpoint,
#             "metodos": list(rule.methods)
#         })

#     return rutas

@app.route("/", methods=["GET"])
def home():
    return redirect(url_for("admin.dashboard"))

if __name__ == "__main__":

    app.run(debug=True)