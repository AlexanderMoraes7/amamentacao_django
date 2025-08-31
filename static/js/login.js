function show_password() {
    // Encontra o campo de senha e o ícone do olho pelos seus IDs.
    const passwordInput = document.getElementById('id_password');
    const eyeIcon = document.getElementById('eye');

    if (passwordInput && eyeIcon) {
        // Se o campo é do tipo 'password', muda para 'text' e troca o ícone.
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            eyeIcon.className = 'fa-solid fa-eye';
        } else {
            // Senão, volta para 'password' e restaura o ícone original.
            passwordInput.type = 'password';
            eyeIcon.className = 'fa-solid fa-eye-slash';
        }
    }
}

// Adiciona um "ouvinte" para garantir que o código só rode depois que a página carregar.
document.addEventListener('DOMContentLoaded', function() {
    // Encontra o ícone do olho.
    const eyeIcon = document.getElementById('eye');

    // Se o ícone existir, adiciona o evento de clique nele.
    if (eyeIcon) {
        eyeIcon.addEventListener('click', show_password);
    }
});
