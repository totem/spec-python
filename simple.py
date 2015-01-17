import argparse
import os
import SimpleHTTPServer
import SocketServer

parser = argparse.ArgumentParser()

parser.add_argument(
    '-p', '--port', default=8080, help='port to serve on')
parser.add_argument(
    '-d', '--directory', default='/', help='directory to server from')

args = parser.parse_args()

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", args.port), Handler)

os.chdir(args.directory)

print("serving at port %d from %s" % (args.port, args.directory))
httpd.serve_forever()
