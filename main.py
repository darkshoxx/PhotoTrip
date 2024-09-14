DATA_FOLDER = r"C:\Code\GithubRepos\Data\PhotoTrip\Lennox"

from PIL import Image, ExifTags
img = Image.open(DATA_FOLDER + r"\test.jpg")
exif = {ExifTags.TAGS[k]:v for k,v in img._getexif().items() if k in ExifTags.TAGS}
print(exif)
# Turns out, the pictures I took had no GPS info. Continue when I have those.