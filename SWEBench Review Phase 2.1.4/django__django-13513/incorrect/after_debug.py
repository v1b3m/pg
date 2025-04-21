@@ -396,10 +396,20 @@ class ExceptionReporter:

    def get_traceback_frames(self):
        def explicit_or_implicit_cause(exc_value):
            # Respect PEP 415 __suppress_context__ attribute
            try:
                explicit_cause = exc_value.__cause__
            except AttributeError:
                explicit_cause = None
            try:
                suppress_context = exc_value.__suppress_context__
            except AttributeError:
                suppress_context = False
            try:
                implicit_context = exc_value.__context__
            except AttributeError:
                implicit_context = None
            return explicit_cause or (None if suppress_context else implicit_context)

        # Get the exception and all its causes
        exceptions = []