"""
Create a Fullscreen button on PyQt4 windows on OS X.
"""

import sys

if sys.platform.startswith("darwin"):
    import ctypes
    from ctypes import CFUNCTYPE, c_void_p, c_char_p, c_int
    import ctypes.util

    objc_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('objc'))
    id = c_void_p
    sel = c_void_p

    sel_registerName = CFUNCTYPE(sel, c_char_p)((b"sel_registerName", objc_lib))

    window_sel = sel_registerName(b"window")
    setCollectionBehavior_sel = sel_registerName(b"setCollectionBehavior:")
    NSWindowCollectionBehaviorFullScreenPrimary = 128

    send1 = CFUNCTYPE(id, id, sel)((b"objc_msgSend", objc_lib))
    send2 = CFUNCTYPE(None, id, sel, c_int)((b"objc_msgSend", objc_lib))

    def add_fullscreen_button(qtwin):
        """Create a full-screen button on qtwin.
        The window needs to be already shown.
        """
        view = qtwin.effectiveWinId()
        cocoawin = send1(view, window_sel)
        send2(cocoawin, setCollectionBehavior_sel, 
          NSWindowCollectionBehaviorFullScreenPrimary)
else:
    def add_fullscreen_button(qtwin):
        """If we were on OS X, would create a full-screen button on qtwin.
        But since we are not, simply do nothing.
        """
        pass
