#!/usr/bin/python3
"""python script to enter us_cat in evdev rules -
makes it available in xfce keyboard selector"""

from lxml import etree

EVDEV_FILENAME = '/usr/share/X11/xkb/rules/evdev.xml'

CHANGES = 0

parser = etree.XMLParser(remove_blank_text=True)
EVDEV = etree.parse(EVDEV_FILENAME,parser)
if len(EVDEV.xpath("./layoutList/layout/configItem/name[text()='us_cat']")) == 0:
    EVDEV.xpath("./layoutList/layout/configItem/name[text()='us']"+
            "/../../..")[0].append(
            etree.fromstring(
                "<layout><configItem><name>us_cat</name><shortDescription>en</shortDescription>"+
                "<description>CaT's Custom Layout (US)</description><languageList><iso639Id>eng</iso639Id>"+
                "</languageList></configItem><variantList><variant><configItem><name>cat</name>"+
                "<description>CaT's Custom Layout (US)</description></configItem></variant></variantList></layout>"
                )
            )
    CHANGES += 1

if len(EVDEV.xpath("./layoutList/layout/configItem/name[text()='de_cat']")) == 0:
    EVDEV.xpath("./layoutList/layout/configItem/name[text()='de']"+
            "/../../..")[0].append(
            etree.fromstring(
                "<layout><configItem><name>de_cat</name><shortDescription>de</shortDescription>"+
                "<description>CaT's Custom Layout (DE)</description><languageList><iso639Id>ger</iso639Id>"+
                "</languageList></configItem><variantList><variant><configItem><name>cat</name>"+
                "<description>CaT's Custom Layout (DE)</description></configItem></variant></variantList></layout>"
                )
            )
    CHANGES += 1

if CHANGES >= 0:
    NEWEVDEV = etree.tostring(EVDEV, pretty_print=True)
    with open(EVDEV_FILENAME, "w") as evdev_xml:
        evdev_xml.write(NEWEVDEV.decode('utf-8'))

