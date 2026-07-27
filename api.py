from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


# =========================
# DATABASE TEMPORANEO
# =========================

utenti = {

}


transazioni = []


# =========================
# HOME API
# =========================

@app.route("/")
def home():

    return "🏦 Sud Italy RP Bank API Online"



# =========================
# CREA UTENTE
# =========================

@app.route("/utente", methods=["POST"])
def crea_utente():

    dati = request.json

    user_id = str(dati["id"])
    nome = dati["nome"]


    if user_id not in utenti:

        utenti[user_id] = {

            "nome": nome,
            "saldo": 0

        }


    return jsonify({

        "successo": True,
        "utente": utenti[user_id]

    })



# =========================
# VEDI SALDO
# =========================

@app.route("/saldo/<user_id>")
def saldo(user_id):

    user_id = str(user_id)


    if user_id not in utenti:

        return jsonify({

            "errore": "Utente non trovato"

        })


    return jsonify({

        "nome": utenti[user_id]["nome"],
        "saldo": utenti[user_id]["saldo"]

    })



# =========================
# PAGAMENTO
# =========================

@app.route("/paga", methods=["POST"])
def paga():

    dati = request.json


    mittente = str(dati["da"])
    destinatario = str(dati["a"])
    importo = int(dati["importo"])



    if mittente not in utenti:

        return jsonify({

            "errore": "Mittente inesistente"

        })



    if destinatario not in utenti:

        return jsonify({

            "errore": "Destinatario inesistente"

        })



    if utenti[mittente]["saldo"] < importo:

        return jsonify({

            "errore": "Saldo insufficiente"

        })



    utenti[mittente]["saldo"] -= importo

    utenti[destinatario]["saldo"] += importo



    transazioni.append({

        "da": mittente,
        "a": destinatario,
        "importo": importo,
        "data": datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )

    })



    return jsonify({

        "successo": True,
        "messaggio": "Pagamento completato"

    })



# =========================
# TRANSAZIONI
# =========================

@app.route("/transazioni/<user_id>")
def get_transazioni(user_id):

    risultati = []


    for t in transazioni:

        if t["da"] == user_id or t["a"] == user_id:

            risultati.append(t)


    return jsonify(risultati)



# =========================
# AVVIO
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
          )
