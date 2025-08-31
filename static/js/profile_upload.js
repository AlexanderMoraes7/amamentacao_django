// Espera o documento HTML ser completamente carregado antes de executar o script.
// Isso evita erros caso o script seja carregado antes dos elementos HTML.
document.addEventListener('DOMContentLoaded', function() {
    
    // Encontra o input de arquivo pelo seu ID.
    const photoInput = document.getElementById('id_path_image');
    
    // Encontra o formulário pelo seu ID.
    const photoForm = document.getElementById('photo-form');

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
});
