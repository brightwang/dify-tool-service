# stolen from: https://github.com/FND/markdown-checklist/blob/master/markdown_checklist/extension.py
import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor


def makeExtension(configs=None):
    if configs is None:
        return TextboxExtension()
    else:
        return TextboxExtension(configs=configs)


class TextboxExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            "list_class": ["textbox", "class name to add to the list element"],
            "render_item": [render_item, "custom function to render items"]
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        list_class = self.getConfig("list_class")
        renderer = self.getConfig("render_item")
        postprocessor = TextboxPostprocessor(list_class, renderer, md)
        md.postprocessors.add("textbox", postprocessor, ">raw_html")


class TextboxPostprocessor(Postprocessor):
    """
    adds textbox class to list element
    """

    # item_pattern = re.compile(r"^<li>\(([ Xx])\)(.*)</li>$", re.MULTILINE)
    list_pattern = re.compile(r"(<ul>\n<li>[Rr]:=)")
    item_pattern = re.compile(r"^<li>([Rr]:=)(.*)</li>$", re.MULTILINE)

    def __init__(self, list_class, render_item, *args, **kwargs):
        self.list_class = list_class
        self.render_item = render_item
        super().__init__(*args, **kwargs)

    def run(self, html):
        html = re.sub(self.list_pattern, self._convert_list, html)
        return re.sub(self.item_pattern, self._convert_item, html)

    def _convert_list(self, match):
        return match.group(1).replace("<ul>", f"<ul class=\"{self.list_class}\">")

    def _convert_item(self, match):
        state, caption = match.groups()
        return self.render_item(caption, state != " ")


def render_item(caption: str, value):
    # the correct answer next to another false one are saved in an attribute such as meta-data written backwards.
    correct = caption.strip()[::-1]
    fake = "".join([c + 's' for c in correct])
    return f"<li>" \
           f"<input type=\"text\" data-content=\"{correct}\" data-question=\"{fake}\" " \
           f"placeholder=\"Enter the correct answer.\" class=\"form-control\" />"
