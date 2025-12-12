let createModalInstance = null;
let editModalInstance = null;

document.addEventListener('DOMContentLoaded', function() {
  const createEl = document.getElementById('createModal');
  if (createEl) createModalInstance = bootstrap.Modal.getOrCreateInstance(createEl);

  const editEl = document.getElementById('editModal');
  if (editEl) editModalInstance = bootstrap.Modal.getOrCreateInstance(editEl);

  const successToastEl = document.getElementById('successToast');
  const errorToastEl = document.getElementById('errorToast');

  window._successToast = successToastEl ? new bootstrap.Toast(successToastEl) : null;
  window._errorToast = errorToastEl ? new bootstrap.Toast(errorToastEl) : null;
});

function showToast(message, isError = false) {
  if (isError) {
    const errEl = document.getElementById('errorMessage');
    if (errEl) errEl.innerText = message;
    if (window._errorToast) window._errorToast.show();
  } else {
    const msgEl = document.getElementById('toastMessage');
    if (msgEl) msgEl.innerText = message;
    if (window._successToast) window._successToast.show();
  }
}

async function createNote() {
  const nombre = document.getElementById('createNombre').value.trim();
  const descripcion = document.getElementById('createDescripcion').value.trim();
  const imagen = document.getElementById('createImagen').value.trim();
  const estado = document.getElementById('createEstado').value;
  
  if (!nombre || !descripcion || !estado) {
    showToast('Por favor completa todos los campos requeridos', true);
    return;
  }

  const payload = {
    name: nombre,
    description: descripcion,
    image: imagen,
    state: estado,
  };

  try {
    const res = await fetch('/notes/api/create/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error('Error creando nota');

    showToast('¡Nota creada exitosamente!');
    if (createModalInstance) createModalInstance.hide();
    
    document.getElementById('createNombre').value = '';
    document.getElementById('createDescripcion').value = '';
    document.getElementById('createImagen').value = '';
    document.getElementById('createEstado').value = 'pendiente';

    setTimeout(() => location.reload(), 700);
  } catch (err) {
    showToast(err.message || 'Error creando nota', true);
  }
}

async function openEditModal(notaId) {
  try {
    const res = await fetch(`/notes/api/get_nota_by_id/${notaId}/`);
    if (!res.ok) throw new Error('Error obteniendo detalles de la nota');
    
    const note = await res.json();

    document.getElementById('editNoteId').value = note.id;
    document.getElementById('editNombre').value = note.nombre;
    document.getElementById('editDescripcion').value = note.descripcion;
    document.getElementById('editImagen').value = note.imagen;
    document.getElementById('editImagePreview').src = note.imagen;
    document.getElementById('editEstado').value = note.estado;
    
    editModalInstance.show();

  } catch(e) {
    showToast(e.message || 'Error obteniendo detalles de la nota', true);
  }
}

function updateImagePreview() {
  const imageUrl = document.getElementById('editImagen').value;
  const preview = document.getElementById('editImagePreview');
  if (imageUrl) {
    preview.src = imageUrl;
  }
}

async function updateNote() {
  const noteId = document.getElementById('editNoteId').value;
  const nombre = document.getElementById('editNombre').value.trim();
  const descripcion = document.getElementById('editDescripcion').value.trim();
  const imagen = document.getElementById('editImagen').value.trim();
  const estado = document.getElementById('editEstado').value;

  if (!nombre || !descripcion) {
    showToast('Por favor completa todos los campos requeridos', true);
    return;
  }

  const payload = {
    name: nombre,
    description: descripcion,
    image: imagen,
    state: estado
  };

  try {
    const res = await fetch(`/notes/api/update/${noteId}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error('Error actualizando la nota');

    showToast('¡Nota actualizada exitosamente!');
    editModalInstance.hide();
    setTimeout(() => location.reload(), 700);

  } catch (error) {
    showToast(error.message || 'Error actualizando nota', true);
  }
}

async function deleteNoteDirectly(event, noteId) {
  event.stopPropagation();

  if (!confirm('¿Estás seguro que deseas eliminar esta nota?')) {
    return;
  }

  try {
    const res = await fetch(`/notes/api/delete/${noteId}/`, {
      method: 'DELETE'
    });

    if (!res.ok) throw new Error('Error eliminando la nota');

    showToast('¡Nota eliminada exitosamente!');
    setTimeout(() => location.reload(), 500);

  } catch (error) {
    showToast(error.message || 'Error eliminando nota', true);
  }
}