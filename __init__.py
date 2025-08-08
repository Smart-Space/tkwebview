try:
    from .core import Webview
except:
    from core import Webview
from tkinter import Frame

class TkWebview(Frame):
    mode = 0# 0 in tkinter, 1 in native window
    def __init__(self, master=None, **kwargs):
        if master is None:
            self.webview = Webview(debug=False)
            width = kwargs.pop('width', 800)
            height = kwargs.pop('height', 600)
            self.webview.set_size(width, height)
            self.mode = 1
        else:
            Frame.__init__(self, master, bg='black', **kwargs)
            self.update()
            self.webview = Webview(debug=False, window=self.winfo_id())
            self.bind('<Configure>', self.on_configure)
            self.mode = 0
    
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
    
    def set_title(self, title):
        if self.mode == 1:
            self.webview.set_title(title)
    
    def destroy_webview(self):
        if self.mode == 1:
            self.webview.destroy()
        else:
            self.destroy()
    
    def get_window(self):
        if self.mode == 0:
            return self.winfo_id()
        else:
            return self.webview.get_window()
    
    def set_size(self, width, height):
        if self.mode == 0:
            self.config(width=width, height=height)
        else:
            self.webview.set_size(width, height)

    def reload(self):
        return self.webview.reload()
    
    def go_back(self):
        return self.webview.go_back()
    
    def go_forward(self):
        return self.webview.go_forward()
    
    def stop(self):
        return self.webview.stop()
