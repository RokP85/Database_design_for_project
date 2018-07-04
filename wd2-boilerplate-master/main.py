#!/usr/bin/env python

import webapp2
from handlers.base import CookieAlertHandler
from handlers.topics import MainHandler, TopicAdd, DetailsHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic_podrobnosti/<topic_id:\d+>', DetailsHandler, name="main-page"),
], debug=True)
