
.. _sec_erweiterungen:


=============
Erweiterungen
=============

Plone ist in der Grundversion ein überaus leistungsfähiges System mit
zahlreiche einzigartigen Funktionen. Eine seiner größten Stärken ist aber seine
Erweiterbarkeit. 

Erweiterungen werden in Form von »Zusatzprodukten« im Konfigurationsmenü installiert (siehe Kapitel :ref:`sec_konfiguration-erweiterungen`). 

Auf der Homepage des Plone-Projekts_ finden Sie einen Katalog der verfügbaren Zusatzprodukte (englisch »Add-on Products«), der nach Kategorien und Versionen durchsuchbar ist. Bei der Auswahl eines Zusatzproduktes ist es wichtig, darauf zu achten, dass es mit der im Einsatz befindlichen Plone-Version kompatibel ist und mit der entsprechenden Version getestet wurde.

Auf plone.org_ finden Sie auch zu jedem Zusatzprodukt die entsprechende
Installationsanweisung. Die Installation erfolgt in der Regel immer über eine
Modifikation der Datei :file:`buildout.cfg` im Installationsverzeichnis. Wenn
Sie Plone mit Hilfe eines :term:`Unified Installers <Unified Installer>`
installiert haben, finden Sie in der Datei ausführliche Kommentare in Englisch.
Die Datei ist in mehrere Abschnitte unterteilt, die durch Bezeichnungen in
eckigen Klammern gekennzeichnet sind. Der erste Abschnitt lautet [buildout].
Dort finden Sie einen Unterabschnitt mit Namen »eggs«. Hier tragen Sie das
gewünschte Zusatzprodukt ein. Die Programmmodule, aus denen sich Plone aufbaut,
werden in so genannten :term:`Eggs <Egg>` verteilt. Das Egg für Plone ist in
dem Abschnitt »eggs« bereits eingetragen. ::

  
  [buildout]
  ...
  eggs =
    Plone

Wenn Sie nun beispielsweise PloneFormGen installieren möchten, tragen Sie das
Egg an dieser Stelle ein. Die Schreibweise muss dabei dem Format
:file:`Namensraum.Modulname` entsprechen. Der Namensraum von PloneFormGen ist
»Products« und der Modulname »PloneFormGen«. Der entsprechende Eintrag muss
also folgendermaßen lauten: ::

  [buildout]
  ...
  eggs =
    Plone
    Products.PloneFormGen

Speichern Sie die Datei und rufen Sie in der Kommandozeile das Programm :program:`buildout` auf. Unter Linux könnte der Aufruf so aussehen: ::

  cd $HOME/Plone/zinstance
  ./bin/buildout 
  
Buildout wird daraufhin das Egg :file:`Products.PloneFormGen` sowie weitere Eggs, von denen PloneFormGen abhängig ist, herunterladen und installieren

Erweiterungen, deren Name mit »Products« beginnt, werden automatisch im
Konfigurationsmenü von Plone zur Installation bereitgestellt, wenn sie in der
Datei :file:`buildout.cfg`, wie oben gezeigt, als Egg eingetragen wurden.

Der erste Teil des Namens wird als Namensraum bezeichnet. Erweiterungen aus dem Namensraum »Products« werden von Plone automatisch als installierbare Erweiterungen erkannt. Erweiterungen aus einem anderen Namensraum werden nicht erkannt. 

In der Datei :file:`buildout.cfg` muss deshalb noch vermerkt werden, dass das
Egg von Plone als installierbare Erweiterung eingelesen werden soll. Dazu zeigt
man :program:`buildout` an, dass das Egg eine ZCML-Datei mit
Konfigurationsanweisungen enthält. Das Produkt »PloneTrueGallery«, das
attraktive Funktionen für ein Fotoalbum bereitstellt, wird beispielsweise im
Namensraum »collective« vertrieben.  Mit diesem Namensraum werden Beiträge der
Plone-Community bezeichnet. Der entsprechende Zusatzeintrag in
:file:`buildout.cfg` lautet: ::

  [buildout]
  ...
  eggs =
    Plone
    collective.plonetruegallery

  zcml =
    collective.plonetruegallery

Produkte aus anderen Namensräumen als »Products« müssen also an zwei Stellen in
der Datei :file:`buildout.cfg` eingetragen werden. Nach dem Abspeichern rufen
Sie :program:`buildout` auf und finden das Zusatzprodukt anschließend im
Konfigurationsmenü im Bereich »Erweiterungen« vor, wo Sie es, wie in Kapitel
:ref:`sec_konfiguration-erweiterungen` beschrieben, in der Plone-Website
installieren können. 


.. _Plone-Projekts: http://plone.org/products

.. _plone.org: http://plone.org/products
