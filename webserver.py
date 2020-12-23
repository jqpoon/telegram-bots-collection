import asyncio
import tornado


class FileHandler(tornado.web.StaticFileHandler):
    def initialize(self, **kwargs):
        super(FileHandler, self).initialize(**kwargs)

    def set_extra_headers(self, path=None):
        # Ignore 'path'.
        self.set_header("Content-Disposition",
                        'attachment; filename="hello world"')


def startWebserver():
    print("Starting webserver!")
    asyncio.set_event_loop(asyncio.new_event_loop())
    app = tornado.web.Application([
        ("/img/(.*)", FileHandler, {"path": "img"})
    ])

    app.listen(8080)
    print("Listening on port 8080")

    tornado.ioloop.IOLoop.instance().start()
