from textnode import TextType, TextNode
class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		if self.props == None:
			return ""
		props_html = ""
		for prop in self.props:
			props_html += f' {prop}="{self.props[prop]}"'
		return props_html

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None or self.value == "":
			raise ValueError()
		if self.tag is None or self.tag == "":
			return self.value

		return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None or self.tag == "":
			raise ValueError()
		if self.children is None:
			raise ValueError()
		html = ""
		for child in self.children:
			html += child.to_html()
		return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"

def text_node_to_html_node(text_node):
	match text_node.text_type:
		case TextType.TEXT:
			return LeafNode(None, text_node.text)
		case TextType.BOLD:
			return LeafNode("b", text_node.text)
		case TextType.ITALIC:
			return LeafNode("i", text_node.text)
		case TextType.CODE:
			return LeafNode("code", text_node.text)
		case TextType.LINK:
			url_prop = {
				href: text_node.url,
			}
			return LeafNode("a", text_node.text, url_prop)
		case TextType.IMAGE:
			image_prop = {
				src: text_node.url,
				alt: text_node.text,
			}
			return LeafNode("img", "", image_prop)
		case _:
			raise ValueError(f"{text_node.text_type}: is not a valid text type")