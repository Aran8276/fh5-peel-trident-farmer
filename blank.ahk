#Requires AutoHotkey 2.0+                                   ; ALWAYS require a version
DetectHiddenWindows, On

F12::
    IfWinExist, BlackScreen
    {
        WinClose, BlackScreen
        return
    }

    Gui, +LastFound +AlwaysOnTop -Caption +ToolWindow +E0x20
    Gui, Color, Black
    WinSet, Transparent, 255
    Gui, Show, x0 y0 w%A_ScreenWidth% h%A_ScreenHeight% NA, BlackScreen
return

Esc::ExitApp
