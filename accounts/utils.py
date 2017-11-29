import uuid
import os

def get_file_path(instance, filename):
    """ Возвращает уникальный путь для загрузки аватара """
    
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/avatars', filename)
