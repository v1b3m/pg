        if settings_dict['USER']:
            kwargs['user'] = settings_dict['USER']
        if settings_dict['NAME']:
            kwargs['db'] = settings_dict['NAME']
        if settings_dict['PASSWORD']:
            kwargs['passwd'] = settings_dict['PASSWORD']
        if settings_dict['HOST'].startswith('/'):
            kwargs['unix_socket'] = settings_dict['HOST']
        elif settings_dict['HOST']:
                        ', '.join("'%s'" % s for s in sorted(self.isolation_levels))
                    ))
        self.isolation_level = isolation_level
        kwargs.update(options)
        return kwargs
