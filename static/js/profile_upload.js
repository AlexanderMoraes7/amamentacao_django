document.addEventListener('DOMContentLoaded', function() {
    
    // Encontra o input de arquivo pelo seu ID.
    const photoInput = document.getElementById('id_path_image');
    const photoForm = document.getElementById('photo-form');
    const editButton = document.getElementById('edit-button');
    const saveButton = document.getElementById('save-button'); 
    
    // Pega todos os campos de input e textarea dentro dos .form-group
    const formFields = document.querySelectorAll('.form-group input, .form-group textarea');
    
    // Verifica se ambos os elementos (input e form) realmente existem na página para evitar erros no console.
    if (photoInput && photoForm) {
        
        // Adiciona um "ouvinte de eventos" ao input que vai disparar uma função sempre que o valor do input mudar
        // (ou seja, quando o usuário selecionar um arquivo).
        photoInput.addEventListener('change', function() {
            
            // Quando o evento 'change' ocorrer enviará o formulário.
            console.log('Arquivo selecionado. Enviando formulário...');
            photoForm.submit();
        });
    }
    

    // Função para colocar os campos em modo de leitura
    function setFieldsReadOnly(isReadOnly) {
        formFields.forEach(field => {
            field.readOnly = isReadOnly;
        });
    }

    // Inicia a página com os campos bloqueados
    setFieldsReadOnly(true);

    // Quando o botão "Editar" for clicado
    editButton.addEventListener('click', function() {
        // Libera os campos para edição
        setFieldsReadOnly(false);
        
        // Esconde o botão "Editar" e mostra o "Salvar"
        editButton.classList.add('hidden');
        saveButton.classList.remove('hidden');

        // Coloca o foco no primeiro campo (username)
        if (formFields.length > 0) {
            formFields[0].focus();
        }
    });
});
