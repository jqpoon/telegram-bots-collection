import asyncio
import tornado

def start_webserver():
    print("Starting webserver!")
    asyncio.set_event_loop(asyncio.new_event_loop())
    app = tornado.web.Application([
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"})
    ])

    app.listen(8080)
    print("Listening on port 8080")

    tornado.ioloop.IOLoop.instance().start()