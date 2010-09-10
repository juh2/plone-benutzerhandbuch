.. _sec_konfiguration-handhabung-bilder:

========================
 Handhabung von Bildern
========================


Wenn man Bilder in eine Plone-Website hochlädt, werden sie in verschiedenen
Größen gespeichert. Sie können daher auch in verschiedenen Größen dargestellt
werden. In diesem Bereich der Konfiguration können Sie die einzelnen Größen
festlegen (siehe Abbildung :ref:`fig_konfiguration-handhabung-bilder`). 

.. _fig_konfiguration-handhabung-bilder:

.. figure:: 
   ../images/konfiguration-handhabung-bilder.*
   :width: 100%
   :alt: Festlegung, in welchen Größen Bilder in Plone gespeichert werden

   Einstellung der Bildgrößen

Tabelle :ref:`tab_bildgroessen` listet die voreingestellten Größen auf.

.. _tab_bildgroessen:

.. table:: Bildgrößen

    =========== ===========
    Bezeichnung Breite:Höhe
    =========== ===========
    large       768:768
    preview     400:400
    mini        200:200
    thumb       128:128
    tile        64:64
    icon        32:32
    listing     16:16
    =========== ===========

Sie können die Größen ändern, indem Sie die entsprechenden Zahlen in der Liste überschreiben.

Wenn Sie eine Größe entfernen möchten, markieren Sie den entsprechenden Eintrag in der Liste und betätigen Sie die Schaltfläche :guilabel:`Ausgewählte Einträge entfernen`. 

Wenn Sie eine Bildgröße hinzufügen möchten, erweitern Sie die Liste um einen Eintrag, indem Sie auf :guilabel:`Erlaubte Bildgröße hinzufügen` klicken.

Beim Abspeichern eines Bildes in den verschiedenen Größen werden die Seitenverhältnisse beibehalten, wobei jeweils die längere Seite auf den entsprechenden Wert gebracht wird. 
