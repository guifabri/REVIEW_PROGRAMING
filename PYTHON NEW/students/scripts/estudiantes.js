let nombres = [["3134262","Adrián Uribe"], ["15957531","Erick Scala"], ["31329488","Melani Velázquez"]]
console.log(nombres)

function mostrar_agregar_estudiante(){
    let add = document.getElementById("add_student");
    add.style.display = "block";
    let buscar = document.getElementById("search_student");
    buscar.style.display = "none";
    let eliminar = document.getElementById("delete_student");
    eliminar.style.display = "none";
}

function mostrar_Buscar_estudiante(){
    let add = document.getElementById("add_student");
    add.style.display = "none";
    let buscar = document.getElementById("search_student");
    buscar.style.display = "block";
    let eliminar = document.getElementById("delete_student");
    eliminar.style.display = "none";
}
function mostrar_Eliminar_estudiante(){
    let add = document.getElementById("add_student");
    add.style.display = "none";
    let buscar = document.getElementById("search_student");
    buscar.style.display = "none";
    let eliminar = document.getElementById("delete_student");
    eliminar.style.display = "block";
}

function listado_Estudiantes(){
    let listado = document.getElementById("listado");
    listado.innerHTML = "";
    nombres.forEach(nombre => {
        let item = document.createElement("p");
        item.textContent = ` C.I. ${nombre[0]}, ${nombre[1]}.`;
        listado.appendChild(item);
    })
}
function agregarEstudiante() {
    let cedula = document.getElementById("ci").value;
    let nombre = document.getElementById("nombre").value;
    nombres.push([cedula,nombre]);
    alert("se ha guardado");
    listado_estudiantes();
}
function buscarEstudiante(){
    let cedula = document.getElementById("buscar-ci").value;
    let encontrado = false;
    nombres.forEach(nombre=> {
        if (nombre[0]==cedula) {
            alert("se ha encontrado el estudiante");
            encontrado = true;
        }
    });
    if(encontrado == false){
        alert("Estudiante no encontrado");
    }

}
function eliminarEstudiante(){
    alert("se ha eliminado el estudiante");
}
