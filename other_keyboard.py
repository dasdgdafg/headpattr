# mostly copied from https://stackoverflow.com/questions/13289777/how-can-i-send-keyboard-commands-hold-release-simultanous-with-a-python-script

import ctypes
from ctypes import wintypes
import time
user32 = ctypes.WinDLL('user32', use_last_error=True)
INPUT_KEYBOARD = 1
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
MAPVK_VK_TO_VSC = 0
# msdn.microsoft.com/en-us/library/dd375731
wintypes.ULONG_PTR = wintypes.WPARAM
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))
    
class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))
    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)
            
class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))
    
class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))
    
LPINPUT = ctypes.POINTER(INPUT)

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    
def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def PressAndRelease(key):
    PressKey(toKeyCode(key))
    time.sleep(0.05)
    ReleaseKey(toKeyCode(key))

def toKeyCode(c):
    return keyCodeMap[c]

keyCodeMap = {
    'backspace'         : 0x08,
    'tab'               : 0x09,
    'enter'             : 0x0D,
    'shift'             : 0x10,
    'ctrl'              : 0x11,
    'alt'               : 0x12,
    'esc'               : 0x1B,
    'space'             : 0x20,
    'pageup'            : 0x21,
    'pagedown'          : 0x22,
    'end'               : 0x23,
    'home'              : 0x24,
    'left'              : 0x25,
    'up'                : 0x26,
    'right'             : 0x27,
    'down'              : 0x28,
    'ins'               : 0x2D,
    'del'               : 0x2E,
    '0'                 : 0x30,
    '1'                 : 0x31,
    '2'                 : 0x32,
    '3'                 : 0x33,
    '4'                 : 0x34,
    '5'                 : 0x35,
    '6'                 : 0x36,
    '7'                 : 0x37,
    '8'                 : 0x38,
    '9'                 : 0x39,
    'a'                 : 0x41,
    'b'                 : 0x42,
    'c'                 : 0x43,
    'd'                 : 0x44,
    'e'                 : 0x45,
    'f'                 : 0x46,
    'g'                 : 0x47,
    'h'                 : 0x48,
    'i'                 : 0x49,
    'j'                 : 0x4A,
    'k'                 : 0x4B,
    'l'                 : 0x4C,
    'm'                 : 0x4D,
    'n'                 : 0x4E,
    'o'                 : 0x4F,
    'p'                 : 0x50,
    'q'                 : 0x51,
    'r'                 : 0x52,
    's'                 : 0x53,
    't'                 : 0x54,
    'u'                 : 0x55,
    'v'                 : 0x56,
    'w'                 : 0x57,
    'x'                 : 0x58,
    'y'                 : 0x59,
    'z'                 : 0x5A,
    'n0'                : 0x60,
    'n1'                : 0x61,
    'n2'                : 0x62,
    'n3'                : 0x63,
    'n4'                : 0x64,
    'n5'                : 0x65,
    'n6'                : 0x66,
    'n7'                : 0x67,
    'n8'                : 0x68,
    'n9'                : 0x69,
    '*'                 : 0x6A,
    '+'                 : 0x6B,
    '-'                 : 0x6D,
    '.'                 : 0x6E,
    '/'                 : 0x6F,
    'f1'                : 0x70,
    'f2'                : 0x71,
    'f3'                : 0x72,
    'f4'                : 0x73,
    'f5'                : 0x74,
    'f6'                : 0x75,
    'f7'                : 0x76,
    'f8'                : 0x77,
    'f9'                : 0x78,
    'f10'               : 0x79,
    'f11'               : 0x7A,
    'f12'               : 0x7B,
    'f13'               : 0x7C,
    'f14'               : 0x7D,
    'f15'               : 0x7E,
    'f16'               : 0x7F,
    'f17'               : 0x80,
    'f18'               : 0x81,
    'f19'               : 0x82,
    'f20'               : 0x83,
    'f21'               : 0x84,
    'f22'               : 0x85,
    'f23'               : 0x86,
    'f24'               : 0x87,
}

