.. _sec_termin:

========
 Termin
========

Mit dem Artikeltyp »Termin‹ können Sie Veranstaltungen ankündigen. Ein Termin
enthält unter anderem Informationen über Ort, Anfang und Ende der
Veranstaltung, über einen Ansprechpartner oder über die Teilnehmer. Diese
Termininformationen haben eigene Eingabefelder im Bearbeitungsformular und
werden gesondert gespeichert, damit Plone sie direkt benutzen kann.

Wie die Seite verfügt auch der Termin über Felder für Titel, Beschreibung und
Haupttext. Letzterer wird im Termin als »Terminankündigung« bezeichnet.  Dort
haben Sie die Möglichkeit, einen Text mit Zwischenüberschriften, Bildern,
Tabellen und anderen Elementen einzugeben.

.. _fig_termin:

.. figure:: ../images/termin.*
   :width: 80%

   Anzeige eines Termins

Zu den strukturierten Angaben eines Termins mit eigenen Eingabefeldern in der
Bearbeitungsansicht gehören:

Terminort (Wo)
  Ort des Ereignisses, Treffpunkt

Terminanfang, Terminende (Wann)
  Zeitraum, in dem das Ereignis stattfindet

Terminankündigung
  Ausführliche Beschreibung der Veranstaltung 

Teilnehmer
  Liste von Personen, die an der Verantstaltung teilnehmen

Webadresse des Termins
  Internetadresse mit weiteren Informationen

Kontaktname
  Name des Ansprechpartners bei Rückfragen

Kontaktadresse
  E-Mail-Adresse des Ansprechpartners

Kontakttelefon
  Rufnummer des Ansprechpartners

Terminanfang und Terminende sind Pflichtfelder und müssen immer ausgefüllt
werden.

Plone wertet die zusätzlichen Felder gezielt aus, um eine einfache
Terminverwaltung anbieten zu können:

* Die strukturierten Angaben werden in der Anzeige des Termins übersichtlich in
  einer Tabelle dargestellt (siehe Abbildung :ref:`fig_termin`).

* Über den Eintrag »Termine« in der Hauptnavigation erreichen Sie eine
  Übersicht künftiger und vergangener Termine.

* Das Terminportlet (siehe Abbildung :ref:`fig_portlet-events`) unterrichtet
  Sie über die jeweils fünf nächsten Termine. Zu jedem Termin sehen Sie Titel,
  Ort, Anfangs und Enddatum. Wenn Sie den Mauszeiger über den Titel halten,
  wird der Beschreibungstext angezeigt.

* Plone trägt Termine außerdem ins Kalenderportlet ein (siehe Abbildung
  :ref:`fig_portlet-calendar`).  Der Titel des Portlets gibt an, welches Jahr
  und welcher Monat gerade angezeigt wird. Die Titelzeile enthält außerdem
  Verweise auf den vorherigen und nächsten Monat. Beim Aufruf einer
  Webseite, auf der sich das Kalenderportlet befindet, wird zunächst der
  aktuelle Monat angezeigt. Der aktuelle Tag ist mit einem Rahmen markiert.

  Ist für einen Tag ein Termin bekannt, so wird das Datum im Kalender
  hervorgehoben und dient als Verweis zu einer Liste aller Termine des
  betreffenden Tages. Wenn Sie den Mauszeiger über einen solchen Tag halten,
  sehen Sie seine Termine mit Anfangszeit, Endzeit und Titel.

* In der Anzeige und bei den Artikelaktionen eines Termins können Sie
  Kalenderdateien im iCal- und vCal-Format (iCalendar/vCalendar)
  herunterladen, um den Termin in das Kalenderprogramm auf Ihrem lokalen
  Rechner zu übernehmen.

.. _fig_portlet-events:

.. figure:: ../images/portlet-events.*
   :width: 40%

   Terminportlet

.. _fig_portlet-calendar:

.. figure:: ../images/portlet-calendar.*
   :width: 40%

   Kalenderportlet


Die Terminübersicht und das Kalenderportlet berücksichtigen per Voreinstellung
nur Termine im Revisionsstatus »veröffentlicht«.

Vergessen Sie bei der Eingabe der Webadresse für weitere Informationen zum
Termin nicht, dass eine Webadresse mit ``http://`` beginnen muss. Wenn Sie
diesen Teil der Adresse weglassen, erhalten Sie eine Fehlermeldung. Plone
speichert nur Adressen mit vollständigem URL-Schema, beispielsweise ``http``,
``https`` oder ``ftp``.

Plone achtet darauf, dass Ihre Datumsangaben für Anfang und Ende des Termins
gültig sind und der Anfangszeitpunkt nicht nach dem Ende liegt.

