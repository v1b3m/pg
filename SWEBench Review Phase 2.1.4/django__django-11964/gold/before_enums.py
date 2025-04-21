
class Choices(enum.Enum, metaclass=ChoicesMeta):
    """Class for creating enumerated choices."""
    pass


class IntegerChoices(int, Choices):