import os

ACCESSIBLE_SHIFT_KEYSTROKE=1
ACCESSIBLE_CONTROL_KEYSTROKE=2
ACCESSIBLE_META_KEYSTROKE=4
ACCESSIBLE_ALT_KEYSTROKE=8
ACCESSIBLE_ALT_GRAPH_KEYSTROKE=16
ACCESSIBLE_BUTTON1_KEYSTROKE=32
ACCESSIBLE_BUTTON2_KEYSTROKE=64
ACCESSIBLE_BUTTON3_KEYSTROKE=128
MAX_STRING_SIZE = 1024
MAX_KEY_BINDINGS = 50
MAX_RELATION_TARGETS = 25
MAX_RELATIONS = 5
MAX_ACTION_INFO = 256
MAX_ACTIONS_TO_DO = 32
MAX_HYPERLINKS = 64
MAX_ICON_INFO = 256
MAX_VISIBLE_CHILDREN = 256
SHORT_STRING_SIZE = 256
TIMEOUT = 30

BRIDGE_DLL = r"C:\Program Files (x86)\Java\jdk8\jre\bin\WindowsAccessBridge-32.dll"

#: The path to the user's .accessibility.properties file, used
#: to enable JAB.
A11Y_PROPS_PATH = os.path.expanduser(r"~\.accessibility.properties")
#: The content of ".accessibility.properties" when JAB is enabled.
A11Y_PROPS_CONTENT = (
    "assistive_technologies=com.sun.java.accessibility.AccessBridge\n"
    "screen_magnifier_present=true\n"
)
