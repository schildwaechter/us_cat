#!/usr/bin/python
from lxml import etree
from sys import stdout

doc = etree.parse('/usr/share/X11/xkb/rules/evdev.xml')
if len(doc.xpath("./layoutList/layout/configItem/name[text()='us']/../../variantList/variant/configItem/name[text()='cat']")) == 0:
    doc.xpath("./layoutList/layout/configItem/name[text()='us']/../../variantList")[0].append( etree.fromstring("<variant><configItem><name>cat</name><description>USA - CaT Custom Layout</description></configItem></variant>"))

doc.write(stdout,pretty_print=True)


