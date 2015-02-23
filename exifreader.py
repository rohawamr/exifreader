import exifread
import json
# Open image file for reading (binary mode)

filepath = raw_input("Enter file name\n")
f = open(filepath, 'rb')

# Return Exif tags
tags = exifread.process_file(f,details=False)

print json.dumps(dict(tags))
