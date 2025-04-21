                APPLE = 1, 'Apple'
                PINEAPPLE = 1, 'Pineapple'


class Separator(bytes, models.Choices):
    FS = b'\x1c', 'File Separator'