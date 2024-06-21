from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
__BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': __BASE_DIR / 'db.sqlite3',
    }
}