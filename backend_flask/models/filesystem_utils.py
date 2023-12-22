# system imports
import os
import json
import pickle

################################ File Path
def check_filepath(filepath):
    """Checks if a filepath exists and creates it if necessary.

    Args:
    filepath: The path to the file to check and create.
    """

    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)


################################ JSON data
def read_json_file(filepath):
    """Reads a JSON file and returns its contents as a Python object.

    Args:
        filepath: The path to the JSON file to read.

    Returns:
        A Python object representing the contents of the JSON file.
    """

    with open(filepath, "r") as f:
        return json.load(f)

def write_json_file(filepath, data):
    """Writes a Python object to a JSON file.

    Args:
        filepath: The path to the JSON file to write.
        data: The Python object to write to the file.
    """

    check_filepath(filepath)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


################################ Pickle Data
def read_pkl_file(filepath):
    """Reads a pickle file and returns its contents as a Python object.

    Args:
        filepath: The path to the pickle file to read.

    Returns:
        A Python object representing the contents of the pickle file.
    """

    with open(filepath, "rb") as f:
        return pickle.load(f)

def write_pkl_file(filepath, data):
    """Writes a Python object to a pickle file.

    Args:
        filepath: The path to the pickle file to write.
        data: The Python object to write to the file.
    """
    
    check_filepath(filepath)
    with open(filepath, "wb") as f:
        pickle.dump(data, f)


################################ Text Files
def read_text_file(filepath):
    """Reads from a text file.

    Args:
        filepath: The path to the text file to read or write.

    Returns:
        The contents of the file, if using the "r" mode.
    """

    with open(filepath, "r") as f:
        return f.read()

def write_text_file(filepath, data=None):
    """writes to a text file.

    Args:
        filepath: The path to the text file to read or write.
        data: The data to write to the file

    Returns:
        None
    """

    check_filepath(filepath)
    with open(filepath, "w") as f:
        f.write(data)

def append_text_file(filepath, data=None):
    """appends to a text file.

    Args:
        filepath: The path to the text file to read or write.
        data: The data to append to the file

    Returns:
        None
    """

    check_filepath(filepath)
    with open(filepath, "a") as f:
        f.write(data)