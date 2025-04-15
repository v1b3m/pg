                User.objects.filter(avatar__desc='missing').delete(),
                (0, {'delete.User': 0})
            )