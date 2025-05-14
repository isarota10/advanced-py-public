from bookshop.model.inmemory import InMemoryPythonDB


def get_model(type: str = "memory"):
    return InMemoryPythonDB()
