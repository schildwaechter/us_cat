#!/usr/bin/python3
"""python script to enter us_cat in ibus components list -
makes it available in xfce keyboard selector"""

from lxml import etree

IBUS_FILENAME = '/usr/share/ibus/component/simple.xml'

CHANGES = 0

parser = etree.XMLParser(remove_blank_text=True)
IBUS = etree.parse(IBUS_FILENAME,parser)
root = IBUS.getroot()
if len(IBUS.xpath("/component/engines/engine/name[text()='xkb:us:us_cat']")) == 0:
    ENGINES = root.find('engines')
    new = etree.SubElement(ENGINES, 'engine')
    new.append(etree.fromstring("<name>xkb:us:us_cat</name>"))
    new.append(etree.fromstring("<language>en</language>"))
    new.append(etree.fromstring("<license>MIT</license>"))
    new.append(etree.fromstring("<author>Carsten Thiel</author>"))
    new.append(etree.fromstring("<layout>us_cat</layout>"))
    new.append(etree.fromstring("<longname>CaT's Custom Layout (US)</longname>"))
    new.append(etree.fromstring("<description>CaT's Custom Layout (US)</description>"))
    new.append(etree.fromstring("<icon>ibus-keyboard</icon>"))
    new.append(etree.fromstring("<rank>1</rank>"))
    CHANGES += 1

if len(IBUS.xpath("/component/engines/engine/name[text()='xkb:de:de_cat']")) == 0:
    ENGINES = root.find('engines')
    new = etree.SubElement(ENGINES, 'engine')
    new.append(etree.fromstring("<name>xkb:de:de_cat</name>"))
    new.append(etree.fromstring("<language>de</language>"))
    new.append(etree.fromstring("<license>MIT</license>"))
    new.append(etree.fromstring("<author>Carsten Thiel</author>"))
    new.append(etree.fromstring("<layout>de_cat</layout>"))
    new.append(etree.fromstring("<longname>CaT's Custom Layout (DE)</longname>"))
    new.append(etree.fromstring("<description>CaT's Custom Layout (DE)</description>"))
    new.append(etree.fromstring("<icon>ibus-keyboard</icon>"))
    new.append(etree.fromstring("<rank>1</rank>"))
    CHANGES += 1


if CHANGES >= 0:
    NEWIBUS = etree.tostring(root, pretty_print=True)
    with open(IBUS_FILENAME, "w") as ibus_component_xml:
        ibus_component_xml.write(NEWIBUS.decode('utf-8'))

