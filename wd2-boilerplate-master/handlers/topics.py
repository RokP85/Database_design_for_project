from handlers.base import BaseHandler
from google.appengine.api import users
from models.models import Topic

class TopicAdd(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    def post(self):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        title = self.request.get("title")
        text = self.request.get("text")

        new_topic = Topic(title=title, content=text, author_email=user.email())
        new_topic.put()  # put() saves the object in Datastore

        return self.write("Topic successfully created!")


class MainHandler(BaseHandler):
    def get(self):
        topic = Topic.query().fetch()
        params = {"topics": topic}

        return self.render_template("main.html", params=params)

class DetailsHandler(BaseHandler):
    def get(self, topic_id):
        detail = Topic.get_by_id(int(topic_id))
        params = {"details": detail}

        return self.render_template("topic_podrobnosti.html", params=params)


