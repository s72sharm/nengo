import swi
import os.path
import json

class NengoGui(swi.SimpleWebInterface):
    def swi_ace(self, *path):
        """Serve the contents of the ace directory"""
        
        p = os.path.join('ace', *path)
        # TODO: confirm this only allows us to read things inside the ace
        #       directory
        with open(p) as f:
            js = f.read()
        return ('text/javascript', js)
        
    def swi_d3_min_js(self):
        with open('d3.min.js') as f:
            js = f.read()
        return ('text/javascript', js)
    

    def swi_favicon_ico(self):
        with open('favicon.ico','rb') as f:
            icon = f.read()
        return ('image/ico', icon)
        
    def swi(self):
        with open('index.html') as f:
            html = f.read()
        return html
        
    def swi_graph_json(self):
        nodes = [
            dict(label='a'),
            dict(label='b'),
            ]
        links = [
            dict(source=0, target=1),
            ]
        return json.dumps(dict(nodes=nodes, links=links))
        

if __name__=='__main__':
    swi.start(NengoGui, 8080)
    #swi.browser(8080)
