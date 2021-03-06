.. _sec_konfiguration-regeln:

========
 Regeln
========

Mit Regeln können in Plone automatisch ablaufende, *ereignisgesteuerte*
Prozesse eingerichtet und konfiguriert werden. Ereignissteuerung bedeutet, dass
bestimmte Befehle und Prozesse nicht von einem Benutzer der Website direkt
ausgelöst werden, sondern durch ein Ereignis. Dabei ist es unerheblich, ob das
Ereignis durch die Aktivität eines Benutzers ausgelöst wurde oder Ergebnis von
automatisch ablaufenden Prozessen war. Was als Ereignis betrachtet wird, ist
Definitionssache. In unserem Fall kann dies zum Beispiel das Hinzufügen eines
neuen Artikels sein. Die Regeln in Plone legen fest,

1. was als Ereignis gilt

2. welche weiteren Bedingungen es gibt und

3. welche Prozesse das Ereignis auslösen soll.

Eine Regel besteht daher aus drei Elementen:

1. dem auslösenden Ereignis

2. einer oder mehreren Bedingungen

3. der Aktion, die ausgeführt wird, wenn das auslösende Ereignis eintritt und
   alle Bedingungen erfüllt sind.

.. todo:: evtl. eine Grafik einbinden, um das zu erklären?

.. todo:: Interface wurde überarbeitet.

Die Konfiguration findet auf zwei Ebenen statt. 

1. Die Formulierung der Regel erfolgt im Bereich :guilabel:`Regeln` der
   Website-Konfiguration (siehe Abbildung :ref:`fig_konfiguration-regeln`).

2. Die Zuweisung einer bereits formulierten Regel erfolgt auf Ordner-Ebene


Im Bereich :guilabel:`Regeln` der Website-Konfiguration finden Sie
zunächst die Option :guilabel:`Deaktiviere global`, die in der
Voreinstellung nicht ausgewählt ist. Möchte man grundsätzlich keine
automatisch ablaufenden Prozesse einrichten, kann man die Option
anwählen.


.. _fig_konfiguration-regeln:

.. figure:: ../images/konfiguration-regeln.*
   :width: 80%
   :alt: Konfigurationsbereich für Regeln

   Konfigurationsbereich für Regeln

Im Bereich :guilabel:`Regeln` sind zunächst keine Regeln vorformuliert
(siehe Abbildung :ref:`fig_konfiguration-regeln`). Die Liste »Regeln«
ist leer. Auf der Seite befindet sich nur der Button :guilabel:`Regel
hinzufügen`. 

Mit Hilfe des Auswahlmenüs :guilabel:`Zeige` ließe sich die Liste der
Regeln filtern. Per Voreinstellung werden alle Regeln aufgeführt. Die
Filtermöglichkeiten sind:

Alle Regeln
   Es werden ausnahmslos alle Regeln aufgelistet

Auslöser: Artikel wurde diesem Ordner hinzugefügt
   Es werden nur die Regeln aufgelistet, in denen das den Prozess anstoßende
   Ereignis das Hinzufügen eines Artikels im Ordner ist.

Auslöser: Artikel wurde verändert
   Es werden nur die Regeln aufgelistet, in denen das den Prozess anstoßende
   Ereignis die Veränderung eines Artikels ist. 

Auslöser: Artikel wurde in diesem Ordner gelöscht
   Es werden nur die Regeln aufgelistet, in denen das den Prozess anstoßende
   Ereignis das Löschen eines Artikels ist.

Auslöser: Status verändert
   Es werden nur die Regeln aufgelistet, in denen das den Prozess anstoßende
   Ereignis eine Statusänderung ist.

Aktiviert
   Es werden nur aktive Regeln aufgelistet.

Deaktiviert
   Es werden nur Regeln aufgelistet, die deaktiviert wurden.

Formulierung einer Regel
========================

Um eine neue Regel hinzuzufügen, betätigen Sie die Schaltfläche :guilabel:`Regel hinzufügen`. Sie werden zu einem Formular weitergeleitet, mit dem Sie die Regel bearbeiten können (siehe Abbildung :ref:`fig_konfiguration-regeln-regel-hinzufuegen`)


.. _fig_konfiguration-regeln-regel-hinzufuegen:

.. figure:: ../images/konfiguration-regeln-regel-hinzufuegen.*
   :width: 80%
   :alt: Hinzufügen einer Regeln

   Hinzufügen einer Regeln

In dem Formular können Sie neben einem Titel und einer Beschreibung Folgendes festlegen.

Auslösendes Ereignis
   Sie müssen ein Ereignis auswählen, das den automatisierten Prozess in Gang
   setzt. Zur Auswahl stehen:

   * Artikel wurde diesem Ordner hinzugefügt
   * Artikel wurde verändert
   * Artikel wurde im Ordner wurde gelöscht
   * Status verändert

Eingeschaltet
   Mit dieser Option können Sie Regeln aktivieren und deaktivieren.

Keine weiteren Regeln ausführen
   Wenn Sie diese Option aktivieren, dürfen nach dieser Regel keine weiteren
   Regeln mehr ausgeführt werden.

Speichern Sie Ihre Eingaben, um die Regel zu erzeugen. Sie werden in den Bereich :guilabel:`Regeln` der Website-Konfiguration zurückgeführt, wo nun die neu erzeugte Regel in der Liste auftaucht (siehe Abbildung :ref:`fig_konfiguration-regeln-regel-hinzugefuegt`). Damit ist die Einrichtung der Regel jedoch noch nicht abgeschlossen. Klicken Sie die neu erzeugte Regel an, um die weiteren Konfigurationsschritte zu erledigen.  

.. _fig_konfiguration-regeln-regel-hinzugefuegt:

.. figure:: ../images/konfiguration-regeln-regel-hinzugefuegt.*
   :width: 80%
   :alt: Die neu hinzugefügte Regeln

   Neu hinzugefügte Regel

Sie gelangen in das Bearbeitungsformular der neuen Regel (siehe
Abbildung :ref:`fig_konfiguration-regeln-regel-bearbeiten`) Sie können
dort zwar Titel und Beschreibung ändern, nicht aber den
Ereignisauslöser. 

.. _fig_konfiguration-regeln-regel-bearbeiten:

.. figure:: ../images/konfiguration-regeln-regel-bearbeiten.*
   :width: 80%
   :alt: Bearbeitung einer Regel
 
   Bearbeitung der neu hinzugefügten Regel

Im unteren Bereich des Formulars können Sie nun Bedingungen
hinzufügen, die erfüllt sein müssen, damit die Regel greift; und
schließlich können Sie die Aktionen bestimmen, die automatisch
ablaufen sollen, wenn alle Bedingungen erfüllt sind. 

Beginnen wir mit den Bedingungen. Wenn Sie eine Bedingung definieren
möchten, müssen Sie zunächst im Auswahlmenü :guilabel:`Bedingung
hinzufügen` einen Bereich auswählen, für den die Bedingung formuliert
werden soll. Folgende Bereiche stehen Ihnen zur Verfügung:

Artikeltyp
   Die Bedingung betrifft den Artikeltyp (siehe Abbildung
   :ref:`fig_bedingung-fuer-artikeltyp`).

   .. _fig_bedingung-fuer-artikeltyp:

   .. figure:: ../images/bedingung-fuer-artikeltyp.*
      :width: 80%
      :alt: Eine Artikeltypbedingung wird hinzugefügt

      Artikeltyp-Bedingung

   Sie können beliebig viele Artikeltypen auswählen. Die Bedingung
   gilt als erfüllt, wenn einer der ausgewählten Artikeltypen
   betroffen ist. Für unser Beispiel bedeutet dies: die Bedingung ist
   erfüllt, wenn einer der ausgewählten Artikeltypen in einem Ordner
   hinzugefügt wurde.

Dateiendung
   Die Bedingung bezieht sich auf die Dateiendung einer hochgeladenen
   Datei (siehe Abbildung :ref:`fig_bedingung-fuer-dateiendung`).

   .. _fig_bedingung-fuer-dateiendung:

   .. figure:: ../images/bedingung-fuer-dateiendung.*
      :width: 80%
      :alt: Eine Bedingung für die Dateiendung wird hinzugefügt

      Bedingung für Dateiendung

   In das Feld kann nur eine Dateiendung (zum Beispiel "exe")
   eingetragen werden. Die Bedingung gilt als erfüllt, wenn die Datei,
   um die es geht, diese Dateiendung hat. Für unser Beispiel bedeutet
   dies: die Bedingung ist erfüllt, wenn eine Datei mit der
   spezifischen Dateiendung in einem Ordner hinzugefügt wurde.

Status
   Die Bedingung bezieht sich auf einen Status im Arbeitsablauf (siehe
   Abbildung :ref:`fig_bedingung-fuer-status`).

   .. _fig_bedingung-fuer-status:

   .. figure:: ../images/bedingung-fuer-status.*
      :width: 80%
      :alt: Eine Statusbedingung wird hinzugefügt

      Statusbedingung

   Die Bedingung kann nur im Zusammenhang einer Regel benutzt werden,
   bei der das auslösende Ereignis eine Änderung des Status (Workflow
   state changed) ist. Die Bedingung gilt als erfüllt, wenn der neue
   Status derjenige ist, der in der Bedingung festgelegt wurde. 

Gruppe des Benutzers
   Die Bedingung bezieht sich auf die Gruppe eines Benutzers.

   .. _fig_bedingung-fuer-gruppe:

   .. figure:: ../images/bedingung-fuer-gruppe.*
      :width: 80%
      :alt: Eine Bedingung für die Gruppe wird hinzugefügt

      Bedingung für die Gruppe


Funktion des Benutzers
   Die Bedingung bezieht sich auf die :term:`Rolle` oder Funktion des
   Benutzers.

   .. _fig_bedingung-fuer-funktion:

   .. figure:: ../images/bedingung-fuer-funktion.*
      :width: 80%
      :alt: Eine Bedingung für die Funktion wird hinzugefügt
 
      Bedingung für die Funktion

TALES-Ausdruck
    Mit dieser Option können Sie eine Bedingung über einen
    TALES-Ausdruck festlegen.

    .. _fig_bedingung-tales:
    
    .. figure:: ../images/konfiguration-regeln-tales-bedingung.*
       :width: 80%
       :alt: Eingabemaske für TALES-Ausdruck

       TALES-Ausdruck als Bedingung

Nachdem Sie eine Bedingung hinzugefügt und Ihre Eingabe gespeichert
haben, kehren Sie zum Bearbeitungsformular der Regel zurück (siehe
Abbildung
:ref:`fig_konfiguration-regeln-artikeltyp-bedingung-hinzugefuegt`). Dort
finden Sie in der Liste der Bedingungen, die von Ihnen neu
hinzugefügte Bedingung vor.
  
.. _fig_konfiguration-regeln-artikeltyp-bedingung-hinzugefuegt:

.. figure:: ../images/konfiguration-regeln-artikeltyp-bedingung-hinzugefuegt.*
   :width: 80%
   :alt: Hinzugefügte Artikeltyp-Bedingung

   Hinzugefügte Artikeltyp-Bedingung

Nun muss noch die Aktion definiert werden, die durch das Ereignis
unter den definierten Bedingungen ausgelöst werden soll. Dazu finden
Sie ganz unten im Formular das Auswahlmenü :guilabel:`Aktion
hinzufügen`. Es enthält folgende Optionen:

Protokoll
   Mit Hilfe der Aktion Protokoll wird das Ereignis unter den gesetzten
   Bedingungen in einer Datei protokolliert. Bei der Konfiguration
   eines Protokolls (siehe Abbildung
   :ref:`fig_konfiguration-regeln-logger-bearbeiten`) können Sie die
   Bezeichnung des Protokolleintrags (Protokollname) und die 
   :term:`Protokollebene` festlegen. Die Einträge selbst
   werden in die Datei :file:`$INSTANCE/var/log/instance.log`
   geschrieben. Die nummerischen Werte für die Protokollebenen ersehen Sie aus Tabelle :ref:`tab_protokollebenen`.

   .. _tab_protokollebenen:

   .. table:: Protokollebenen
   
      +----------+------+
      | Ebene    | Wert |
      +----------+------+
      | CRITICAL | 50   |
      +----------+------+
      | ERROR    | 40   |
      +----------+------+
      | WARNING  | 30   |
      +----------+------+
      | INFO     | 20   |
      +----------+------+
      | DEBUG    | 10   |
      +----------+------+
      | NOTSET   | 0    |
      +----------+------+


   .. _fig_konfiguration-regeln-logger-bearbeiten:

   .. figure:: ../images/konfiguration-regeln-logger-bearbeiten.*
      :width: 80%
      :alt: Bearbeitungsformular für Protokolldatei

      Protokollierung eines Ereignisses

Benutzer benachrichtigen
   Mit dieser Aktion wird dem Benutzer eine Statusmeldung
   angezeigt. Sie können im Bearbeitungsformular (siehe Abbildung
   :ref:`fig_konfiguration-regeln-notify-user-bearbeiten`) eine
   Nachricht eingeben und den Typ der Statusmeldung (info, warning
   oder error) festlegen. 

   .. _fig_konfiguration-regeln-notify-user-bearbeiten:

   .. figure:: ../images/konfiguration-regeln-notify-user-bearbeiten.*
      :width: 80%
      :alt: Einrichtung einer Benutzerbenachrichtigung

      Einrichtung einer Benutzerbenachrichtung

Kopieren in Ordner
   Diese Aktion kopiert einen Artikel in einen bestimmten Ordner. Sie können im
   Bearbeitungsformular (siehe Abbildung
   :ref:`fig_konfiguration-regeln-copy-to-folder`) den Ordner, in den der
   Artikel kopiert werden soll, auswählen.

   .. _fig_konfiguration-regeln-copy-to-folder:

   .. figure:: ../images/konfiguration-regeln-copy-to-folder.*
      :width: 80%
      :alt: Einrichtung der Aktion »Kopieren in Ordner«

      Einrichtung der Aktion »Kopieren in Ordner«

   Sie können einen Ordner festlegen, indem Sie den
   entsprechenden Radiobutton anklicken und die Schaltfläche
   :guilabel:`Aktualisieren` betätigen. Der Ordner wird in einem neuen
   Formularfeld mit dem Namen :guilabel:`Momentane Auswahl` angezeigt.  

   Das Formular bietet Ordner im Wurzelverzeichnis von Plone als
   Zielordner an. Sie können Ordner über die integrierte Suchfunktion
   suchen. Alternativ können Sie in einen der aufgeführten Ordner
   wechseln, indem Sie die nebenstehende Schaltfläche
   :guilabel:`Durchsuchen` anklicken. In übergeordnete Artikel
   wechseln Sie entsprechend mit der Schaltfläche
   :guilabel:`Übergeordneter Artikel`.

   Sichern Sie zum Abschluss Ihre Eingaben.

In Ordner verschieben
   Diese Aktion verschiebt einen Artikel in einen definierten
   Ordner. Das Bearbeitungsformular ist ebenso aufgebaut wie das
   Formular für die Aktion »Kopieren in Ordner«.

Artikel löschen
   Mit dieser Aktion wird der Artikel gelöscht. Es gibt keine Konfigurationsmöglichkeiten.

Statuswechsel Arbeitsablauf
   Mit dieser Aktion wird ein Statuswechsel durchgeführt. Im
   Bearbeitungsformular (siehe Abbildung
   :ref:`fig_konfiguration-regeln-workflow-transition`) können Sie mit
   dem Auswahlmenü :guilabel:`Statuswechsel` den Status auswählen, in
   den der Artikel versetzt werden soll.

   .. _fig_konfiguration-regeln-workflow-transition:

   .. figure:: ../images/konfiguration-regeln-workflow-transition.*   
      :width: 80%
      :alt: Einrichtung einer Statusänderung

      Arbeitsablaufaktion

E-Mail senden
   Mit dieser Aktion wird eine E-Mail versendet. Im
   Bearbeitungsformular (siehe Abbildung
   :ref:`fig_konfiguration-regeln-email-aktion-bearbeiten` können Sie
   Betreff, Absender, Empfänger und die Nachricht eingeben. Dabei
   können Variablen wie zum Beispiel »${title} und »${url}« für 
   Titel und URL des Artikels verwendet werden. Die Variablen werden in der
   versendeten E-Mail durch die jeweils aktuellen Angaben ersetzt.

   .. _fig_konfiguration-regeln-email-aktion-bearbeiten:
   
   .. figure::
      ../images/konfiguration-regeln-email-aktion-bearbeiten.*
      :width: 80%
      :alt: Einrichtung der E-Mail-Aktion

      Einrichtung der E-Mail-Aktion

   Sie können neben den Variablen »${title}« und »${url}« noch weitere
   Variablen eingeben. Die möglichen Variablen sind unterhalb des
   Bearbeitungsformulars aufgelistet (siehe Abbildung
   :ref:`fig_konfiguration-regeln-e-mail-ersetzungen`)

   .. _fig_konfiguration-regeln-e-mail-ersetzungen:

   .. figure:: ../images/konfiguration-regeln-e-mail-ersetzungen.*
      :width: 50%
      :alt: Alle möglichen Variablen, die in eine E-Mail-Aktion eingefügt werden können.

      Auflistung der Variablen

   Wenn derjenige, der die Aktion ausgeführt hat, keine E-Mail bekommen soll,
   markieren Sie die Option :guilabel:`Ausführenden nicht benachrichtigen`. 

Nach dem Hinzufügen einer Aktion, wird diese im Bearbeitungsformular
der Regel aufgelistet (siehe Abbildung
:ref:`fig_konfiguration-regeln-email-aktion-hinzugefuegt`). 

.. _fig_konfiguration-regeln-email-aktion-hinzugefuegt:

.. figure:: ../images/konfiguration-regeln-email-aktion-hinzugefuegt.*
   :width: 80%
   :alt: Fertig konfigurierte Regel

   Fertig konfigurierte Regel

Zuweisung einer Regel
=====================

Ist eine Regel in der Website-Konfiguration formuliert worden, kann
sie überall auf der Website einem Ordner zugewiesen werden. Die
Zuweisung erfolgt mit Hilfe der Ansicht »Regeln«, die nur für Ordner
vorhanden ist. 

Wenn Sie einen Ordner aufrufen und in die Ansicht »Regeln« wechseln,
ist dort zunächst noch keine Regel aufgeführt (siehe Abbildung
:ref:`fig_regel-in-ordner-hinzufuegen`).

Im Auswahlmenü :guilabel:`Regel hier zuweisen` können Sie eine der
formulierten Regeln auswählen und durch Betätigung der Schaltfläche
:guilabel:`Hinzufügen` dem Ordner zuweisen. 

.. _fig_regel-in-ordner-hinzufuegen:

.. figure::
   ../images/regel-in-ordner-hinzufuegen.*
   :width: 80%
   :alt: Hinzufügen einer Regel in einem Ordner

   Hinzufügen einer Regel in einem Ordner


Nach dem Hinzufügen der Regel wird diese in der Ansicht »Regeln«
aufgeführt (siehe Abbildung :ref:`fig_regel-im-ordner-hinzugefuegt`). 

.. _fig_regel-im-ordner-hinzugefuegt:

.. figure::
   ../images/regel-im-ordner-hinzugefuegt.*
   :alt: Auflistung der Regeln eines Ordners

   Auflistung der Regeln eines Ordners

Die Ansicht enthält verschiedene Schaltflächen. 

Aktivieren
   Aktiviert die markierte Regel. 

Deaktivieren
   Deaktiviert die markierte Regel.

Einstellungen für Unterordner übernehmen
   Bewirkt, dass die markierte Regel auch in Unterordnern gültig ist.

Einstellungen nur für diesen Ordner übernehmen
   Bewirkt, dass die markierte Regel nur im aktuellen Ordner angewendet wird.

Entfernen
   Entfernt die markierte Regel aus der Liste.

Sie müssen vor Betätigung einer dieser Schaltflächen die Regeln
markieren, auf die die Aktion angewendet werden soll.

Anzeige der verknüpften Regeln
==============================

Damit Sie in der Website-Konfiguration den Überblick behalten und stets wissen,
welche Regel in welchen Ordnern angewendet wird, werden die entsprechenden
Ordner im Bearbeitungsformular der Regel ganz unten im Bereich »Verknüpfungen«
aufgelistet (siehe Abbildung
:ref:`fig_konfiguration-regeln-verknuepfte-regeln`). Durch einen Klick auf den
Namen eines Ordners können Sie direkt in den Ordner wechseln.

.. _fig_konfiguration-regeln-verknuepfte-regeln:

.. figure::
   ../images/konfiguration-regeln-verknuepfte-regeln.*
   :alt: Auflistung, in welchen Ordnern die Regel verwendet wird

   Auflistung, in welchen Ordnern die Regel verwendet wird
