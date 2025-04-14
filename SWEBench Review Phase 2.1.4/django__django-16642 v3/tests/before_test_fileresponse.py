        """
        test_tuples = (
            (".tar.gz", "application/gzip"),
            (".tar.bz2", "application/x-bzip"),
            (".tar.xz", "application/x-xz"),
        )
        for extension, mimetype in test_tuples:
            with self.subTest(ext=extension):