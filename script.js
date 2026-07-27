console.log("🏦 Sud Italy RP Bank caricata");


/*
    In futuro qui arriveranno
    i dati veri dal bot:

    - saldo
    - transazioni
    - utenti
    - lavori
*/


let utente = {

    nome: "Mario Rossi",

    contanti: 500,

    banca: 5000

};


document.getElementById("cash").innerHTML =
    utente.contanti + " €";


document.getElementById("bank").innerHTML =
    utente.banca + " €";
