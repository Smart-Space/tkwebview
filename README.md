# tkwebview

tkinter的webview视图。

## 简介

在此之前，我在Windows平台上实现了[Smart-Space/tkwebview2](https://github.com/Smart-Space/tkwebview2)，但是为了使用WebView2，需要`pywebview`和`pythonnet`，而且有大量的底层操作包含在库源码中。

显然，直接使用c/c++封装给python使用会更简单。感谢[webview/webview](https://github.com/webview/webview)和[HIllya51/webviewpy](https://github.com/HIllya51/webviewpy)，让这个想法成为可能。

> [!IMPORTANT]
>
> `tkwebview`当前不包含事件回调，但是拥有了十分重要的javascript调用python代码的功能。此外，因为经过封装，`tkwebview`难以操作原始的web控件，但也因此非常简单易用。

> [!WARNING]
>
> 虽然webview是跨平台的，但是原始的`set_size`无法满足嵌入状态下的尺寸修改，需要实现新的函数，并且为了方便，我单独维护了一个基于webview的c++库[Smart-Space/webview](https://github.com/Smart-Space/webview)，这个库的核心部件截止于[HIllya51/webviewpy@e81bd17](https://github.com/HIllya51/webviewpy/commit/e81bd17023623345f3ae801dcf4afde033b16fe0)，如果没有严重错误，不会更新。
>
> 由于条件限制，本仓库只能提供的Windows平台的二进制链接库（32位链接库未经过测试）。

## 开始使用

```cmd
pip install tkwebview
```

示例程序见：`../tkwebview/test.py`

### 主要方法/函数

#### TkWebview(master, \*\*kwargs)

tkwebview的核心类，本质上是一个Frame，可以和Frame布局。

#### tkwebview.bindjs(name, fn, is_async_return=False)

绑定名为`name`的JS函数，指向`fn`。在JavaScript中，使用`window.name`调用。

在同步模式中，`fn`只需要接收JS函数传递来的参数，返回结果即可。

异步模式中，`fn`至少会收到一个`returner`函数（第一个参数位），异步处理得到结果后，通过`returner(result)`返回结果。

#### tkwebview.dispatch(fn)

子线程中调度代码在主线程/GUI上运行（我也没看懂）。

#### tkwebview.unbindjs(name)

解除绑定名为`name`的JS函数。

#### tkwebview.eval(js)

执行JS代码。

#### tkwebview.navigate(url)

导航到`url`。

> [!NOTE]
>
> url需要以协议开头，包括http, https, file...

#### tkwebview.init(js)

在开头注入JS代码，比任何内容都要前。

#### tkwebview.set_html(html)

设置html代码。

#### tkwebview.version(html)

返回`webview/webview`的版本。

> [!CAUTION]
>
> Windows平台下，不知原因，tkinter界面中，WebView2具有最高级渲染优先级，一旦获得焦点，除非立刻整个窗口，否则其它控件无法获取焦点。解决方法是为所有控件绑定`<Button-1>`使用`event.widget.focus_force()`强制获取焦点。如果有控件还需要额外绑定`<Button-1>`事件，使用`add`参数。

## 开发

### 第一步

下载[Smart-Space/webview](https://github.com/Smart-Space/webview)，编译需要的版本，得到动态链接库。

> 我只实现了Windows平台下的`webview_resize`。

### 第二布

下载本仓库代码，将动态链接库放置在`.tkwebview/platform`下正确的位置（见`./tkwebview/core.py`）。

## 关于跨平台

理论上，`tkwebview`完全能够跨平台，但是我测试不了，所以只提供Windows平台的二进制链接库。所有的跨平台代码只需要在`webview`中编写，本库只提供统一封装。