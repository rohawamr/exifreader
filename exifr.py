import exifread
from flask import Flask
exifr = Flask(__name__)

@exifr.route("/")
def exif_func():
    filepath = raw_input("Enter file name: \n")
    f = open(filepath, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f,details=False)
    print tags
    return "Hello world..!!"

if __name__ == "__main__":
    exifr.run()
