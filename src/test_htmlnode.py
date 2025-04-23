import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HTMLNode("<a>", "Click me", None, props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(node.children, None)
        self.assertEqual(node.tag, "<a>")
        self.assertEqual(node.value, "Click me")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = LeafNode("a", "Click Me!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click Me!</a>')

    def test_leaf_no_value(self):
        node = LeafNode("a", "")
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()