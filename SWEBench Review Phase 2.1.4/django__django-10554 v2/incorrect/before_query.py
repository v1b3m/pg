@@ -333,6 +333,9 @@ class Query(BaseExpression):
            del obj.base_table
        except AttributeError:
            pass
        return obj

    def chain(self, klass=None):