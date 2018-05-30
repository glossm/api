import os

from django.utils.deconstruct import deconstructible
from django.utils.timezone import now

# Maximum length of instance ID in the filename
MAX_ID_LENGTH = 6


@deconstructible
class RenamedPath:
    def __init__(self, path, instance_type=''):
        self.path = path
        self.instance_type = instance_type

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1].lower()
        timestamp = now().timestamp()
        id_str = str(instance.id).zfill(MAX_ID_LENGTH)
        filename = f'{self.instance_type}_{id_str}_{timestamp}.{ext}'
        return os.path.join(self.path, filename)
