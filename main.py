from website import create_app #importo la funcion create_app del modulo website 

app = create_app()

if __name__ == '__main__': # si este archivo es el principal, o sea, no lo estamos importando
    app.run(debug=True) #corremos la aplicacion (en modo debug).
#no queremos que si este archivo es importado, se ejecute la aplicacion en segundo plano
#si corro este archivo en consola, el servidor va a estar andando, la pagina va a estar donde nos dice la terminal al ejecutar este archivo
