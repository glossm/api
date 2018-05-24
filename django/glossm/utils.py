import os

from django.utils.timezone import now

# Maximum length of instance ID in the filename
MAX_ID_LENGTH = 6


def get_renamed_path(path, instance_type=''):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1].lower()
        timestamp = now().timestamp()
        id_str = str(instance.id).zfill(MAX_ID_LENGTH)
        filename = f'{instance_type}_{id_str}_{timestamp}.{ext}'
        return os.path.join(path, filename)

    return wrapper
