DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "anupmond_profile",
            "USER": "anupmond_anup",
            "PASSWORD": "anup_2023",
            "PORT": "3306",
            "HOST": "localhost",
            "OPTIONS": {
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
                "charset": "utf8mb4",
                "use_unicode": True,
            },
        }
    }