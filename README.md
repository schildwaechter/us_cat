# us_cat - xkb layout

The `us_cat` Layout is a xkb keybord layout map intended for use
with a us keyboard for typing primarily English, but also German,
and Norwegian and some Slavic languages (Ex-YU) in Latin script and
diacritic characters for French.

![layout image](us_cat.png "The layout")

## Installation

Place the files in `/usr/share/X11/xkb/symbols/`
and use as layout `us_cat` with variant `cat`.

> **Note**: on upgrade delete `/var/lib/xkb/*.xkm` and manually re-apply the layout or reboot.

The python script `evdev_xml_entry.py` will directly modify your system's `evdev.xml`
and `ibus_xml_entry.py` does the same for your system's `ibus//simple.xml`
to show the layouts in the keyboard configuration GUIs. (Execute as root)

## other OSes

Versions for Windows and macOS are included in the respective folders.

## open questions

- repurpose `<CAPS>`?

