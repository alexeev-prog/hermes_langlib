class Singleton(type):
    """
    A metaclass that implements the Singleton pattern.

    This metaclass ensures that a class has only one instance, and provides a
    global point of access to it.
    """

    _instances = {}  # noqa: RUF012

    def __call__(cls: object, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
