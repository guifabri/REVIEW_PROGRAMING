let nombres = [["3134262","Adrián Uribe"], ["15957531","Erick Scala"], ["31329488","Melani Velázquez"]];
console.log(nombres);

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
    alert("Se ha guardado");
    listado_Estudiantes();
}

function buscarEstudiante(){
    let cedula = document.getElementById("buscar-ci").value;
    let encontrado = false;
    nombres.forEach(nombre=> {
        if (nombre[0]==cedula) {
            alert("Se ha encontrado el estudiante");
            encontrado = true;
        }
    });
    if(encontrado == false){
        alert("Estudiante no encontrado");
    }
}

function eliminarEstudiante(){
    let eliminar_ci = document.getElementById("eliminar-ci").value;
    let eliminado;
    if(eliminar_ci==""){
        eliminado = nombres.pop();
    } else {
        let index = nombres.findIndex(est => est[0]==eliminar_ci);
        if(index!=-1){
            eliminado = nombres[index];
            nombres.splice(index, 1);
        } else {
            alert("Estudiante no encontrado");
            return;
        }
    }
    alert(`Se ha eliminado a ${eliminado[0]} ${eliminado[1]}`);
    listado_Estudiantes();
}

// Guardar la lista en localStorage
// Función para guardar la lista en un archivo .txt
function guardarEnArchivo() {
    const contenido = JSON.stringify(nombres, null, 2); // Convierte la lista a JSON
    const blob = new Blob([contenido], { type: 'text/plain' });
    const enlace = document.createElement('a');
    enlace.href = URL.createObjectURL(blob);
    enlace.download = 'lista_estudiantes.txt';
    enlace.click();
    alert("Lista guardada en archivo");
}

// Función para cargar la lista desde un archivo .txt
function cargarDesdeArchivo() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.txt';
    input.onchange = function(event) {
        const archivo = event.target.files[0];
        const lector = new FileReader();
        lector.onload = function(e) {
            nombres = JSON.parse(e.target.result); // Convierte el contenido del archivo a un array
            alert("Lista cargada desde el archivo");
            listado_Estudiantes(); // Muestra el listado actualizado
        };
        lector.readAsText(archivo);
    };
    input.click();
}
