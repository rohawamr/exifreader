Enter file contents here
import sys
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json
import urlparse
import sys
import urllib
import datetime
import re

PORT_NUMBER = 80



def getExifData(filepath):
	f = open(filepath, 'rb')
        # Return Exif tags
        tags = exifread.process_file(f,details=False)
        print tags
        return tags


class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
  def do_GET(self):
    if self.path.startswith("/exifr"):
      o = urlparse.urlparse(self.path)
      getvars = urlparse.parse_qs(o.query)
      try:
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        a = getvars[path][0]
        self.wfile.write( json.dumps(getExifData(a) ) )
        return
      except:
        e = sys.exc_info()[0]
        self.send_error(404,'Error, provide a route parameters' + str(e) + str(getvars.keys()))
        return
    self.send_error(404,'Resource Not Found')

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
s
