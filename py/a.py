class Router(object):
    def allow_migrate(self, db, model):
        if db == "default":
            return True
        return False
