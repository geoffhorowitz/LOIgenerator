# system imports
import cv2

# local imports
from filesystem_utils import check_filepath

################################ Load/Save Images
def load_image(filepath):
    """Loads an image from a file.

    Args:
    filepath: The path to the image file to load.

    Returns:
    A NumPy array representing the image.
    """

    return cv2.imread(filepath)

def save_image(filepath, image):
    """Saves an image to a file.

    Args:
    filepath: The path to the image file to save.
    image: A NumPy array representing the image.
    """

    check_filepath(filepath)
    cv2.imwrite(filepath, image)