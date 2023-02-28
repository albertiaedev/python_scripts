from PIL import Image
import rembg

img = Image.open('') # Insert the name + extension of your selected image between quotes

removed = rembg.remove(img) # Use this method to remove the background of your selected image

print(removed) # Show in screen the image after the background has been removed
