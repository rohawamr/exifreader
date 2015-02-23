import exifread
from flask import Flask
exifreader = Flask(__name__)

@exifreader.route("/")
def exif_func():
    filepath = raw_input("Enter file name: \n")
    f = open(filepath, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f,details=False)
    print tags
    return tags

if __name__ == "__main__":
    exifreader.run()
