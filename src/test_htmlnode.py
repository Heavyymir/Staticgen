import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):  
        node = HTMLNode()            
        try: 
            node.to_html()
            self.fail("Expected NotImplementedError")
        except NotImplementedError:
            pass
    
    def test_props_to_html(self):
        # Create nodes with different props
        node1 = HTMLNode(props={"href": "https://google.com"})
        node2 = HTMLNode(props={"href": "https://amazon.com"})
        node3 = HTMLNode(props={"id": "main", "class": "container"})
        
        # Test that props_to_html outputs the expected string for each node
        self.assertEqual(node1.props_to_html(), ' href="https://google.com"')
        self.assertEqual(node2.props_to_html(), ' href="https://amazon.com"')
        self.assertEqual(node3.props_to_html(), ' id="main" class="container"')

if __name__ == "__main__":
    unittest.main()
