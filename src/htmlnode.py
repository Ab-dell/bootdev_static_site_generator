


class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HtmlNode(tag:{self.tag}, value:{self.value}, children:{self.children}, attributes:{self.props})"


    def to_html(self):
        raise NotImplementedError("to_html methode not implemented yet")
    

    def props_to_html(self):
        if self.props == None:
            return ""
        
        formated_string = f""
        for prop in self.props:
            formated_string += f' {prop}="{self.props[prop]}"'

        return formated_string
    


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def props_to_html(self):
        return super().props_to_html()


    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have values")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HtmlNode(tag:{self.tag}, value:{self.value}, attributes:{self.props})"


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have tags")
        
        if self.children == None:
            raise ValueError("All parent tags must have children")
        
        children_string = ""
        for child in self.children:
            children_string += f"{child.to_html()}"

        
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"