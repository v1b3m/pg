@@ -71,6 +71,27 @@ class CommandParser(ArgumentParser):
        else:
            raise CommandError("Error: %s" % message)

    def add_subparsers(self, **kwargs):
        """
        Override add_subparsers to propagate called_from_command_line and missing_args_message to subparsers.
        """
        # Use default parser_class of our type if not specified
        kwargs.setdefault('parser_class', type(self))
        subparsers_action = super().add_subparsers(**kwargs)
        # Monkey-patch its add_parser to inject our flags
        original_add_parser = subparsers_action.add_parser
        # Use self.called_from_command_line and self.missing_args_message
        def add_parser(name, **subkwargs):
            # Only set if not already specified in subkwargs
            if 'called_from_command_line' not in subkwargs:
                subkwargs['called_from_command_line'] = getattr(self, 'called_from_command_line', None)
            if 'missing_args_message' not in subkwargs:
                # Propagate missing_args_message of self, though likely user will supply missing_args_message for their own subparser if needed
                subkwargs['missing_args_message'] = getattr(self, 'missing_args_message', None)
            return original_add_parser(name, **subkwargs)
        subparsers_action.add_parser = add_parser
        return subparsers_action


def handle_default_options(options):
    """