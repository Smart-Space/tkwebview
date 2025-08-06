try:
    from .core import Webview
except:
    from core import Webview
from tkinter import Frame

class TkWebview(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, bg='black', **kwargs)
        self.update()
        self.webview = Webview(debug=False, window=self.winfo_id())
        self.bind('<Configure>', self.on_configure)
    
    def on_configure(self, event):
        self.webview.resize()
    
    def resolve(self, id, status, result):
        return self.webview.resolve(id, status, result)
    
    def bindjs(self, name, fn, is_async_return=False):
        return self.webview.bind(name, fn, is_async_return)
    
    def dispatch(self, fn):
        return self.webview.dispatch(fn)
    
    def unbindjs(self, name):
        return self.webview.unbind(name)
    
    def eval(self, js):
        return self.webview.eval(js)
    
    def navigate(self, url):
        return self.webview.navigate(url)
    
    def init(self, js):
        return self.webview.init(js)
    
    def set_html(self, html):
        return self.webview.set_html(html)
    
    def version(self):
        return self.webview.version()

    def reload(self):
        return self.webview.reload()
    
    def go_back(self):
        return self.webview.go_back()
    
    def go_forward(self):
        return self.webview.go_forward()
    
    def stop(self):
        return self.webview.stop()
