from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json
import sys
import cgi
from PIL import Image
from PIL.ExifTags import TAGS

PORT_NUMBER = 8090

# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/BaseHTTPServer/index.html

  
#This class will handles any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):

  def do_POST(self):
          # Parse the form data posted
          form = cgi.FieldStorage(
              fp=self.rfile, 
              headers=self.headers,
              environ={'REQUEST_METHOD':'POST',
                       'CONTENT_TYPE':self.headers['Content-Type'],
                       })

          # Begin the response
          self.send_response(200)
          self.end_headers()

          # Echo back information about what was posted in the form
          for field in form.keys():
              field_item = form[field]
              if field_item.filename:
                  # The field contains an uploaded file
                  #file_data = field_item.file.read()
                  im = Image.open(field_item.file)
                  imr=im.rotate(90).show().file.read
                  self.wfile.write(imr)
              else:
                  # Regular form value
                  self.wfile.write('\t%s=%s\n' % (field, form[field].value))
          return

if __name__ == "__main__":
  try:
	  #Create a web server and define the handler to manage the
	  #incoming request
	  server = HTTPServer(('', PORT_NUMBER), myHandler)
	  print 'Started httpserver on port ' , PORT_NUMBER

	  #Wait forever for incoming http requests
	  server.serve_forever()

  except KeyboardInterrupt:
	  print '^C received, shutting down the web server'
	  server.socket.close()
