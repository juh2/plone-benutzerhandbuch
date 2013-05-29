==================================
 Import und Export von Formularen
==================================

Formulare, die mit PloneFormGen erstellt wurden, lassen sich exportieren und an anderer Stelle importieren. Wer häufig ähnlich strukturierte Formulare erstellen muss, wird diese Funktion zu schätzen wissen. Man kann viel Zeit sparen, wenn man längere Formulare nicht komplett neu aufbauen muss, sondern importieren und anpassen kann.

Im Aktionsmenü eines Formular-Ordners finden Sie für den Im- und Export zwei Aktionen vor (siehe Abbildung :ref:`fig_import-export-aktion`).

.. _fig_import-export-aktion:

.. figure::
   ./images/import-export-aktion.*
   :width: 80%
   :alt: Aktionsmenü eines Formular-Ordners

   Aktionsmenü eines Formular-Ordners

Mit dem Eintrag :guilabel:`Export` können Sie das gesamte Formular exportieren. Plone erzeugt eine komprimiertes :term:`Tar`-Archiv, das Sie auf Ihrem lokalen Rechner abspeichern können (siehe Abbildung :ref:`fig_export-formular`).

.. _fig_export-formular:

.. figure::
   ./images/export-formular.*
   :width: 70%
   :alt: Speichern der Export-Datei

   Speichern der Export-Datei

Um ein Formular zu importieren, müssen Sie zunächst einen Formular-Ordner
anlegen. Betätigen Sie dann im Aktionsmenü des neuen Formular-Ordners den
Eintrag :guilabel:`Import`. Sie werden daraufhin aufgefordert, eine
Import-Datei zu bestimmen (siehe Abbildung :ref:`fig_import-formular`) Wählen
Sie ein vorher exportiertes Formular als Import-Datei aus und betätigen
Sie die Schaltfläche :guilabel:`Importieren`. 

.. _fig_import-formular:

.. figure::
   ./images/import-formular.*
   :width: 80%
   :alt: Import eines Formular-Ordners

   Import eines Formulars

Der gesamte Inhalt des exportierten Formulars wird in das neue Formular
geladen. Wenn Sie die Option :guilabel:`Bestehende Formularfelder entfernen?`
vor dem Importieren ausgewählt haben, werden die Beispielobjekte des neu
erzeugten Formular-Ordners gelöscht. 

Sie können nun die importierten Formular-Elemente anpassen.
