let nombres = [["3134262","Adrián Uribe"], ["15957531","Erick Scala"], ["31329488","Melani Velázquez"]]
console.log(nombres)

function agregar_estudiante(){
    let add = document.getElementById("add_student");
    add.style.display = "block";
    let buscar = document.getElementById("search_student");
    buscar.style.display = "none";
    let eliminar = document.getElementById("delete_student");
    eliminar.style.display = "none";
}

function buscar_estudiante(){
    let add = document.getElementById("add_student");
    add.style.display = "none";
    let buscar = document.getElementById("search_student");
    buscar.style.display = "block";
    let eliminar = document.getElementById("delete_student");
    eliminar.style.display = "none";
}
function eliminar_estudiante(){
    let add = document.getElementById("add_student");
    add.style.display = "none";
    let buscar = document.getElementById("search_student");
    buscar.style.display = "none";
    let eliminar = document.getElementById("delete_student");
    eliminar.style.display = "block";
}

function listado_estudiantes(){
    alert("listado");
    let listado = document.getElementById("listado_estudiantes");
    listado.innerHTML = "";
    alert("listado");
}