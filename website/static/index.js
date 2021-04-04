function deleteNote(noteId) {
  //hacemos request a la ruta delete-note, con metodo POST, en el cuerpo la id de la nota a borrar y una vez hecho eso, refrescamos la pagina / (home) 
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
