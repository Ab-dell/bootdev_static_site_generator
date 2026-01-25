import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_equal_url_optional_argument(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node1, node2)

    def test_not_equal(self):
        node1 = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_with_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "this is a url")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a bold html node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold html node")
    
    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is an italic html node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic html node")

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a code html node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code html node")

    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a link", TextType.LINK, "test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href":f"test.com"})
        self.assertEqual(html_node.props_to_html(), ' href="test.com"')

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is an image description", TextType.IMAGES, "lot_of_images.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"lot_of_images.com", "alt":"This is an image description"})
        self.assertEqual(html_node.props_to_html(), ' src="lot_of_images.com" alt="This is an image description"')

    



if __name__ == "__main__":
    unittest.main()
