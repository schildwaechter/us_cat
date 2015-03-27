#!/usr/bin/python3
"""python script to enter us_cat in evdev rules -
makes it available in xfce keyboard selector"""

from lxml import etree

EVDEV_FILENAME = '/usr/share/X11/xkb/rules/evdev.xml'

CHANGES = 0

parser = etree.XMLParser(remove_blank_text=True)
EVDEV = etree.parse(EVDEV_FILENAME,parser)
if len(EVDEV.xpath("./layoutList/layout/configItem/name[text()='us']"+
    "/../../variantList/variant/configItem/name[text()='cat']")) == 0:
    EVDEV.xpath("./layoutList/layout/configItem/name[text()='us']"+
            "/../../variantList")[0].append(
            etree.fromstring(
                "<variant><configItem><name>cat</name><description>"+
                "USA - CaT Custom Layout</description></configItem></variant>"
                )
            )
    CHANGES += 1

if len(EVDEV.xpath("./layoutList/layout/configItem/name[text()='de']"+
    "/../../variantList/variant/configItem/name[text()='cat']")) == 0:
    EVDEV.xpath("./layoutList/layout/configItem/name[text()='de']"+
            "/../../variantList")[0].append(
            etree.fromstring(
                "<variant><configItem><name>cat</name><description>"+
                "DE - CaT Custom Layout</description></configItem></variant>"
                )
            )
    CHANGES += 1

if CHANGES >= 0:
    NEWEVDEV = etree.tostring(EVDEV, pretty_print=True)
    with open(EVDEV_FILENAME, "w") as evdev_xml:
        evdev_xml.write(NEWEVDEV.decode('utf-8'))

