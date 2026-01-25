import unittest
from htmlnode import HtmlNode




class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        html_node = HtmlNode("a","some text", None, {"href":"a_link.com"})
        self.assertEqual(str(html_node), "HtmlNode(tag:a, value:some text, children:None, attributes:{'href': 'a_link.com'})")

    def test_repr_without_props(self):
        html_node = HtmlNode("a","some text", None)
        self.assertEqual(str(html_node), "HtmlNode(tag:a, value:some text, children:None, attributes:None)")
    
    def test_repr_without_any_arguments(self):
        html_node = HtmlNode()
        self.assertEqual(str(html_node), "HtmlNode(tag:None, value:None, children:None, attributes:None)")

    def test_props_to_html(self):
        html_node = HtmlNode("a","some text", None, {"href":"a_link.com"})
        self.assertEqual(html_node.props_to_html(), f' href="a_link.com"')

    def test_props_to_html_with_multiple_prop(self):
        html_node = HtmlNode("a","some text", None, {"href":"a_link.com", "alt":"just a test"})
        self.assertEqual(html_node.props_to_html(), f' href="a_link.com" alt="just a test"')

    def test_props_to_html_without_props(self):
        html_node = HtmlNode()
        self.assertEqual(html_node.props_to_html(), "")




if __name__ == "__main__":
    unittest.main()
