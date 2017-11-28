import tornado.httpserver
import tornado.ioloop
import tornado.web

class getToken(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")

application = tornado.web.Application([
    (r'/', getToken),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application, ssl_options={
        "certfile": "<Path to your SSL certificate>",
        "keyfile": "/<Path to your Key>",
    })
    http_server.listen(443)
    tornado.ioloop.IOLoop.instance().start()
