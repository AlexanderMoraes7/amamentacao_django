from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from django.db.models.fields.files import ImageFieldFile # Importe isso


# --- LÓGICA PARA EDITAR O NOME DA IMAGEM E EVIDAR NOMES DUPLICADOS
def user_directory_path(instance, filename):
    return 'profiles/user_{0}_{1}'.format(instance.user.id, filename)

class Photo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    path_image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

# --- LÓGICA DE EXCLUSÃO DE ARQUIVOS ---
# Signal para deletar o arquivo quando o objeto Photo é deletado
@receiver(pre_delete, sender=Photo)
def photo_delete(sender, instance : Photo, **kwargs):
    path_image: ImageFieldFile = instance.path_image # Dica de tipo para a variável
    # se ele tiver um arquivo associado será deletado
    if path_image:
        if os.path.isfile(instance.path_image.path):
            os.remove(instance.path_image.path)

# Signal para deletar o arquivo ANTIGO quando um NOVO é enviado
@receiver(pre_save, sender=Photo)
def photo_update(sender, instance : Photo, **kwargs):
    # Se o objeto não tem um PK, significa que ele está sendo criado pela primeira vez.
    # Nesse caso, não há arquivo antigo para deletar, então saímos da função.
    if not instance.pk:
        return False
    try:
        # Busca o objeto antigo no banco de dados
        old_photo = sender.objects.get(pk=instance.pk).path_image
    except sender.DoesNotExist:
        # Se por algum motivo o objeto antigo não existir, sai da função.
        return False

    # Compara o arquivo antigo com o novo
    new_photo = instance.path_image
    if not old_photo == new_photo:
        # Se o arquivo antigo existe e é diferente do novo, deleta o antigo.
        if old_photo and os.path.isfile(old_photo.path):
            os.remove(old_photo.path)