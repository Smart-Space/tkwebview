from tkinter import Tk, Entry
from __init__ import TkWebview as Webview
import ctypes
from threading import Thread
from time import sleep
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)/100
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def get_url(event):
    # 需要以协议(https, http, file等)开头
    url=e.get()
    web.navigate(url)

def count(req):
    global count_num
    count_num += req
    return str(count_num)

def compute(returner, num1, num2):
    def _(_1, _2):
        sleep(1)
        returner(_1 * _2)
    Thread(
        target=_,
        args=(num1, num2),
    ).start()

a=Tk()
a.tk.call('tk', 'scaling', ScaleFactor)
a.geometry('800x400')

e=Entry(a,font='微软雅黑 18', relief='solid')
e.pack(fill='x', padx=10, pady=5)
e.bind('<Return>', get_url)

html="""
<div>
  <button id=\"increment\">+</button>
  <button id=\"decrement\">−</button>
  <span>Counter: <span id=\"counterResult\">0</span></span>
</div>
<hr />
<div>
  <button id=\"compute\">Compute</button>
  <span>Result: <span id=\"computeResult\">(not started)</span></span>
</div>
<script type=\"module\">
  const getElements = ids => Object.assign({}, ...ids.map(
    id => ({ [id]: document.getElementById(id) })));
  const ui = getElements([
    \"increment\", \"decrement\", \"counterResult\", \"compute\",
    \"computeResult\"
  ]);
  ui.increment.addEventListener(\"click\", async () => {
    ui.counterResult.textContent = await window.count(1);
  });
  ui.decrement.addEventListener(\"click\", async () => {
    ui.counterResult.textContent = await window.count(-1);
  });
  ui.compute.addEventListener(\"click\", async () => {
    ui.compute.disabled = true;
    ui.computeResult.textContent = \"(pending)\";
    ui.computeResult.textContent = await window.compute(6, 7);
    ui.compute.disabled = false;
  });
</script>"""

count_num = 0

web=Webview(a)
web.pack(fill='both', expand=True)
# web.navigate('https://www.baidu.com/')
web.set_html(html)
web.bindjs('count', count)
web.bindjs('compute', compute, is_async_return=True)

a.bind_all("<Button-1>", lambda e: e.widget.focus_force())
# 如果某个控件同样需要<Button-1>，可自行改写或者使用add参数添加

a.bind("<Alt-Left>", lambda e: web.go_back())
a.bind("<Alt-Right>", lambda e: web.go_forward())
a.bind("<F5>", lambda e: web.reload())
a.bind("<Escape>", lambda e: web.stop())

a.mainloop()
