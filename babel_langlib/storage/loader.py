from babel_langlib.storage.storage import Config


def get_file_extension(filename: str):
	return str(filename).split('.')[-1]
