.. index:: Bild (Artikeltyp) 

.. _sec_bild:

======
 Bild
======

Der Artikeltyp »Bild« dient dazu, Fotos und :term:`Bitmap-Grafiken
<Bitmap-Grafik>` in einer Website zu verwalten und – wie die anderen Artikel –
mit Metadaten zu versehen. Die Bilder können als Illustration in den Haupttext
anderer Artikel eingebunden werden. Eine Ausnahme bilden die Titelbilder von
Nachrichten, die in der Bearbeitungsansicht der Nachricht direkt hochgeladen
werden müssen. Diese Bilder können nicht in anderen Artikeln verwendet
werden.

Die Anzeige eines Bildes besteht aus dem Bild zusammen mit dem
Titel, der Beschreibung und einer Größenangabe (siehe
Abbildung :ref:`fig_bild`).

.. _fig_bild:

.. figure:: 
   ../images/bild.*
   :width: 80%
   :alt: Screenshot der Anzeige eines Bildes

   Anzeige eines Bildes

.. index:: Vollbilddarstellung

Das Bild selbst ist dabei ein Verweis auf seine Vollbilddarstellung, die nur
das Bild in voller Auflösung und einen Verweis zurück zur Anzeigeansicht
enthält. Sie können also zwischen der Anzeige und der Vollbilddarstellung hin-
und herspringen. Sie gelangen auch über den Verweis :guilabel:`Zeige Bild in
voller Größe...` zur Vollbilddarstellung.

Die Bearbeitungsansicht eines Bildes enthält neben den allgemeinen
Feldern wie Titel und Beschreibung ein Formularfeld, mit dem Sie eine
Bilddatei von Ihrem Rechner hochladen können. 

Plone speichert hochgeladene Bilder in diversen Größen, sodass Sie Bilder, die
Sie in einen Text einfügen möchten, nicht selbst verkleinern müssen. Folgende
Größen stehen in der Standardkonfiguration zur Verfügung:  

* 768px (large)

* 400px (preview)

* 200px (mini)

* 128px (thumb)

* 64px (tile)

* 32px (icon)

* 16px (listing)

Die Größe bezieht sich dabei immer auf die längere Seite des Bildes. Die
einzelnen Bilder werden unter jeweils eigenen URLs abgelegt und können einzeln
aufgerufen und angezeigt werden. Wenn ein Bild unter dem Namen :file:`bild`
hochgeladen wurde, lauten die einzelnen URLs zum Beispiel folgendermaßen.  ::

  http://localhost:8080/Plone/bild/image_large
  http://localhost:8080/Plone/bild/image_preview
  http://localhost:8080/Plone/bild/image_mini

Das Originalbild ist unter :file:`image_view_fullscreen` erreichbar. ::

  http://localhost:8080/Plone/bild/image_view_fullscreen

.. index:: Bild bearbeiten 

Plone verfügt über einige grundlegende Bildbearbeitungsfunktionen wie Drehen
und Spiegeln. Die Bedienelemente befinden sich in der Ansicht
:guilabel:`Transformieren`.  Wählen Sie dort die gewünschte Transformation aus
dem Auswahlmenü :guilabel:`Methode auswählen` aus und betätigen Sie die
Schaltfläche :guilabel:`Ausführen` (siehe Abbildung
:ref:`fig_bild-transformieren`).

.. _fig_bild-transformieren:

.. figure:: 
   ../images/bild-transformieren.*
   :width: 100%

   Transformationsansicht eines Bildes

Folgende Änderungen kann Plone an Bildern durchführen:

* horizontal und vertikal spiegeln
* im und gegen den Uhrzeigersinn um 90° drehen
* um 180° drehen

