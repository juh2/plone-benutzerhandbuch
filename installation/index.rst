Voraussetzungen
===============

Das CMS Plone 4 benötigt Python_ in der Version 2.6_ und Zope_ in der Version
2.12_. Python ist eine objektorientierte Programmiersprache. Zope ist ein auf
Python basierender Webapplikationsserver. 

Plone wird mit Hilfe des :term:`Buildsystems <Buildsystem>` zc.buildout_
installiert. Mit Buildout lassen sich zum Beispiel plattformübergreifend
identisch konfigurierte Entwicklungs- und Produktivumgebungen installieren und
pflegen. Dabei übernimmt Buildout nicht nur die Installation der benötigten
Plone- und Zope-Pakete, sondern kann auch zur Installation anderer Komponenten
wie diverser Caching-Systeme, Loadbalancer oder Webserver genutzt werden.  

Buildout ist ein sehr leistungsfähiges System, das mit Hilfe von Skripts
konfiguriert wird. Wenn Sie mehr über Buildout erfahren möchten oder die
Absicht haben, für Plone Erweiterungen zu programmieren, sollten Sie das
Kapitel Entwicklungsumgebung_ im Plone-Entwicklerhandbuch_ konsultieren.

.. index:: Unified Installer

Für die Grundinstallation von Plone stehen Ihnen Installationspakete zur
Verfügung, die so genannten :term:`Unified Installer`, mit deren Hilfe Sie alle
benötigten Komponenten einfach und schnell installieren können. Auf der Website
des Plone-Projekts finden Sie die verfügbaren Installationspakete unter der
Adresse http://plone.org/products/plone

.. _ploneorg-download-optionen:

.. figure:: 
   ../images/ploneorg-download-optionen.*

   Die verfügbaren Installer für Plone 4

Wählen Sie einfach das für Ihr Betriebssystem passende Installationspaket aus
und laden Sie es herunter.

.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout

.. _Python: http://www.python.org

.. _2.6: http://python.org/download/releases/2.6.5/

.. _Zope: http://www.zope.de

.. _2.12: http://docs.zope.org/zope2/releases/2.12/index.html

.. _Entwicklungsumgebung: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/entwicklungsumgebung

.. _Plone-Entwicklerhandbuch: http://www.plone-entwicklerhandbuch.de
