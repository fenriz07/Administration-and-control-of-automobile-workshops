def db_config():
    return {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'click_control',
        'USER': 'servio',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
