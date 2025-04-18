class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Ritorna il database da utilizzare per la lettura (query)."""
        if model._meta.app_label == 'app2':
            return 'db2'
        return 'default'

    def db_for_write(self, model, **hints):
        """Ritorna il database da utilizzare per la scrittura (insert/update)."""
        if model._meta.app_label == 'app2':
            return 'db2'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Consente la relazione tra oggetti di diversi database."""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Decide se un'applicazione può migrarsi su un determinato database."""
        if db == 'db2':
            return app_label == 'app2'
        return db == 'default'
