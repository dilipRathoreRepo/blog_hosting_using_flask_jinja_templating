from flask import Flask, render_template
import requests
from post import Post


URL = "https://api.npoint.io/5abcca6f4e39b4955965"

all_posts_objects = []
response = requests.get(URL)
all_posts = response.json()
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts_objects)


@app.route("/blog/<int:num>")
def show_posts(num):
    for blog in all_posts_objects:
        if blog.id == num:
            return render_template("post.html", post=blog)


if __name__ == "__main__":
    app.run(debug=True)
