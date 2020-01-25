from datetime import datetime

class BlogPost(object):
    date = datetime(2019, 1, 1, 12, 0, 0)
    tag = ['test', 'python', 'hello world']
    title = "Hello World!"
    content = """
                This is a test, hello world!
            """

    def __init__(self, title, content=None):
        self.title = title
        if content:
            self.content = content


class DescText(object):
    text = None
    def __init__(self, text):
        self.text = text


DESC_TEXT_INDEX = DescText(
    """
    Welcome to JDCS!
    """
    )
DESC_TEXT_BLOG = DescText(
    """
    Below are a list of blog entries.
    """
    )
DESC_TEXT_GALLERY = DescText(
    """
    This gallery contains some of my favourite photos - the post processing is mostly done via GIMP.
    """
    )
DESC_TEXT_DATA = DescText(
    """
    This page contains a number of data APIs I've build based on my personal interests
    """
    )
DESC_TEXT_ABOUT = DescText(
    """
    This site was was built (by me!) primarily for learning and playing with various technologies.
    """
    )

BLOG_POSTS = [
    BlogPost('Post 1', content='Here is the first post'),
    BlogPost('Post 2', content='Here is another post!'),
    BlogPost('Post 3', content='Third time lucky post!!!')
    ]