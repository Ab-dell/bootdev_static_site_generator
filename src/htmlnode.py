




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
