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



## 开发



## 关于跨平台

理论上，`tkwebview`完全能够跨平台，但是我测试不了，所以只提供Windows平台的二进制链接库。所有的跨平台代码只需要在`webview`中编写，本库只提供统一封装。