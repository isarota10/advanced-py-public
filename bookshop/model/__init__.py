from bookshop.model.inmemory import InMemoryPythonDB


def get_model(type: str = "memory") -> InMemoryPythonDB:
    if type == "memory":
        return InMemoryPythonDB()
