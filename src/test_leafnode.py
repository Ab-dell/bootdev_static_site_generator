from leafnode import LeafNode
import unittest




class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.link.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.link.com">Click me!</a>')

    #it doesn't really render as a real img tag but we will leave it like this for now
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "i am an image", props={"src": "https://www.link.com", "rel": "i am a description"})
        self.assertEqual(node.to_html(), '<img src="https://www.link.com" rel="i am a description">i am an image</img>')

    def test_repr(self):
        leaf_node = LeafNode("a","some text", {"href":"a_link.com"})
        self.assertEqual(str(leaf_node), "HtmlNode(tag:a, value:some text, attributes:{'href': 'a_link.com'})")

    def test_repr(self):
        leaf_node = LeafNode("a","some text")
        self.assertEqual(str(leaf_node), "HtmlNode(tag:a, value:some text, attributes:None)")

    def test_props_to_html(self):
        leaf_node = LeafNode("a","some text", {"href":"a_link.com"})
        self.assertEqual(leaf_node.props_to_html(), f' href="a_link.com"')


if __name__ == "__main__":
    unittest.main()