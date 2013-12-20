=====================
 Der Formular-Ordner
=====================

Um die Bedienung von PloneFormGen besser zu verstehen, sollte man sich ein
Formular, wie einen Setzkasten vorstellen, in dem man kleine Objekte – in
unserem Falle die einzelnen Formularfelder – beliebig hin- und herschieben und
anordnen kann. Technisch gesehen ist ein mit PloneFormGen erzeugtes Formular
ein Container, also ein Ordner, in dem beliebig viele Objekte (Formularfelder)
erzeugt, angeordnet und konfiguriert werden können.

Hinzufügen eines Formular-Ordners
=================================

Sobald PloneFormGen installiert wurde, finden Sie im Hinzufüge-Menü
den Eintrag :guilabel:`Formular-Ordner` (siehe Abbildung
:ref:`fig_hinzufuegemenue-formular-ordner`).

.. _fig_hinzufuegemenue-formular-ordner:

.. figure::
   ./images/hinzufuegemenue-formular-ordner.*
   :width: 60%
   :alt: Hinzufüge-Menü mit Eintrag »Formular-Ordner«

   Hinzufüge-Menü mit Eintrag »Formular-Ordner«

Wenn Sie diesen Eintrag auswählen, gelangen Sie zur
Bearbeitungsansicht eines Formular-Ordners (siehe Abbildung
:ref:`fig_formular-ordner-hinzufuegen`). 

.. _fig_formular-ordner-hinzufuegen:

.. figure::
   ./images/formular-ordner-hinzufuegen.*
   :width: 60%
   :alt: Die Bearbeitungsansicht, mit der ein Formular-Ordner
   	 hinzugefügt wird.

   Hinzufügen eines Formular-Ordners

Die Bearbeitungsansicht besteht aus den bekannten Teilformularen
»Kategorisierung«, »Datum«, »Urheber« und »Einstellungen«, die ebenso
aufgebaut sind wie bei den übrigen Artikeltypen von Plone. Das
zusätzliche Teilformular »Overrides« werden Sie so gut wie nie
benötigen. Da die Beschreibung seiner Funktion den Rahmen dieser
Dokumentation sprengen würde, wird auf eine Erklärung dieses
Teilformulars verzichtet.

Die für das Formular wesentlichen Eingaben erfolgen im Teilformular
»Standard«. Es enthält neben Eingabefeldern für »Titel« und
»Beschreibung« folgende Punkte:

Bezeichnung der Versand-Schaltfläche
   Sie können die Benennung des Absende-Buttons selbst
   bestimmen. Voreingestellt ist »Absenden«.

Abbruch-Schaltfläche anzeigen
   Wenn bereits Formularfelder ausgefüllt wurden, kann man die Eingabe
   mit diesem Button löschen. Wenn er betätigt wird, werden alle
   Formularfelder geleert.

Bezeichnung der Abbruch-Schaltfläche
   Sie können die Schaltfläche benennen. Voreingestellt ist »Eingaben
   löschen«.

Aktionsadapter
   Hier legen Sie fest, was mit den eingegebenen Formulardaten
   nach der :term:`Validierung` geschehen soll. Voreingestellt ist der
   Aktionsadapter :guilabel:`Mailer`, mit dem das ausgefüllte Formular
   per E-Mail verschickt wird. Sie können hier aber auch einen
   Daten-Speicher-Adapter auswählen (siehe Abschnitt
   :ref:`sec_daten-speicher-adapter`). 

Danke-Seite 
   Hier wählen Sie aus, welche Seite der Benutzer zu Gesicht bekommt, wenn er
   das Formular abgeschickt hat. Voreingestellt ist eine Seite »Thank you«, die
   automatisch erzeugt wird, wenn Sie einen Formular-Ordner hinzufügen (siehe
   Abschnitt :ref:`sec_danke-seite`). Falls weitere Seiten vorhanden sind,
   werden sie hier aufgelistet. Alternativ können Sie :guilabel:`Keins`
   auswählen, was zur Folge hat, dass lediglich die Feldwerte, also die
   Einträge, die der Benutzer vorgenommen hat, angezeigt werden.

Force SSL connection
   Wenn diese Option angewählt wurde, werden die Formulardaten verschlüsselt
   über :term:`SSL` an die Website übertragen, falls SSL für die Website
   konfiguriert wurde. Fragen Sie bei Bedarf Ihren Systemadministrator.

Vorwort des Formulars
   In diesem Feld können Sie eine Einleitung zum Formular
   formulieren. Ihnen stehen alle Funktionen des Texteditors dabei zur
   Verfügung.

Formular Epilog
   In diesem Textfeld (siehe Abbildung :ref:`fig_formular-epilog`)
   können Sie eine Schlussbemerkung eintragen, die unterhalb des
   Absende-Buttons angezeigt wird.

.. _fig_formular-epilog:

.. figure::
   ./images/formular-epilog.*
   :width: 80%
   :alt: Das Formularfeld ganz unten auf der Bearbeitungsansicht eines
   	 Formular-Ordners.

   Formularfeld für Epilog

Nach dem Speichern der Angaben gelangen Sie zur Anzeige des neu
erzeugten Formulars (siehe Abbildung
:ref:`fig_umfrage-eingabeformular`). Sie sehen ein Formular, dass dem
Kontaktformular von Plone ähnelt, das unter anderem in Kapitel
:ref:`sec_gui-siteaktionen` erwähnt wird. 

.. _fig_umfrage-eingabeformular:

.. figure::
   ./images/umfrage-eingabeformular.*
   :width: 80%
   :alt: Ansicht des Formulars 

   Beispielformular

Das neu erstellte Formular enthält Formularfelder für eine
E-Mail-Adresse, ein Betreff und einen Kommentar. Diese Felder wurden
beim Anlegen des Formular-Ordners automatisch erzeugt. Bei dem
Formular handelt es sich im Grunde um ein Beispielformular, und der
erzeugte Formular-Ordner ist auch nicht leer, wie man es erwarten
sollte, sondern enthält eine Reihe von Objekten (siehe Abbildung
:ref:`fig_formular-ordner-inhalt`)

.. _fig_formular-ordner-inhalt:

.. figure::
   ./images/formular-ordner-inhalt.*
   :width: 80%
   :alt: Inhaltsansicht des Formular-Ordners mit automatisch erzeugten
    	 Objekten

   Inhalt eines neu erzeugten Formular-Ordners

Sie haben also nach der Erzeugung eines Formular-Ordners ein voll
funktionsfähiges Beispielformular, das Sie nun anpassen können. So
können Sie weitere Objekte in dem Formular-Ordner
hinzufügen. Abbildung :ref:`fig_hinzufuege-menue-formular-objekte` zeigt,
welche Objekte dabei zur Auswahl stehen.

.. _fig_hinzufuege-menue-formular-objekte:

.. figure:: ./images/hinzufuege-menue-formular-objekte.*
   :width: 80%
   :alt: Das Hinzufüge-Menü in einem Formular-Ordner mit zahlreichen
         Einträgen

   Hinzufüge-Menü in einem Formular-Ordner

Reihenfolge der Formularfelder ändern
=====================================

Die Reihenfolge der Formularfelder können Sie ändern, indem Sie in der
Inhaltsansicht des Ordners, die Reihenfolge der Objekte verändern. Wie
das geht, wird in Kapitel :ref:`sec_inhaltsansicht-ordner`
erklärt. Wenn Sie beispielsweise in dem Beispielformular die Stellung
der Objekte »Your E-Mail Address« und »Subject« vertauschen (siehe
Abbildung :ref:`fig_reihenfolge-geaendert`) werden auch die
entsprechenden Formularfelder in der Anzeige (siehe Abbildung
:ref:`fig_reihenfolge-geaendert-anzeige`) umsortiert.

.. _fig_reihenfolge-geaendert:

.. figure::
   ./images/reihenfolge-geaendert.*
   :width: 70%
   :alt: Inhaltsansicht mit geänderter Reihenfolge

   Geänderte Reihenfolge in der Inhaltsansicht

.. _fig_reihenfolge-geaendert-anzeige:

.. figure::
   ./images/reihenfolge-geaendert-anzeige.*
   :width: 70%
   :alt: Anzeige mit geänderter Reihenfolge

   Geänderte Reihenfolge im Formular


