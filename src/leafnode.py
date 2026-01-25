from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def props_to_html(self):
        return super().props_to_html()


    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have values")
        
        if self.tag == None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HtmlNode(tag:{self.tag}, value:{self.value}, attributes:{self.props})"