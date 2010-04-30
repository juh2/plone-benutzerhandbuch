.. _sec_admin:

==============================
 Hinweise für Administratoren
==============================

Dieser Anhang soll Ihnen Hinweise geben, welche Einstellungen an einer frisch
aufgesetzten Plone-Website vorzunehmen sind, um alle im Buch beschriebenen
Funktionen verfügbar zu machen. Er ist jedoch keineswegs
als umfassende Anleitung für die Administration einer Website gedacht.

Sie finden sowohl die Quellen von Plone als auch fertige Pakete und
Installationsroutinen für verschiedene Betriebssysteme unter
\url{http://plone.org/products/plone/}. Eine Installationsanleitung liegt der
Software bei.

Die folgenden Einstellungen sind für die gesamte Website vorzunehmen und nicht
mit persönlichen Einstellungen einzelner Benutzer zu verwechseln. Als
Administrator erreichen Sie die Plone-Konfiguration über einen Verweis rechts
oben auf jeder Seite.

.. _sec_email-konfig:

E-Mail konfigurieren
====================

Als Erstes müssen Sie die E-Mail-Einstellungen Ihrer Website konfigurieren. Es
muss sichergestellt sein, dass aus der Website heraus E-Mails verschickt
werden können.

* Wählen Sie im Konfigurationsmenü den Eintrag »E-Mail«.
* Tragen Sie einen SMTP-Server mit den entsprechenden
  Konfigurationsparametern ein. Wenden Sie sich bei Fragen an Ihren
  Systemadministrator.
* Füllen Sie das Formular »E-Mail-Absender« aus.


.. _sec_tutoriums-ordner:

Tutoriumsordner »Veranstaltungen«
=================================

Damit die Benutzer auf Ihrer Website das Tutorium nachvollziehen können,
müssen Sie einen Ordner mit dem Namen »Veranstaltungen« anlegen.

* Erzeugen Sie auf der obersten Ebene Ihrer Plone-Website den Ordner
  »Veranstaltungen«.
* Öffnen Sie die Artikelansicht »Zugriff«.
* Übertragen Sie der Gruppe »Angemeldete Besucher« die Funktionen »Kann
  hinzufügen«, »Kann bearbeiten« und »Kann ansehen«.
* Legen Sie im Ordner »Veranstaltungen« gegebenenfalls Ordner für einzelne
  Seminare an, so dass beispielsweise jeder Teilnehmer einer Schulung einen
  eigenen Arbeitsbereich erhält. Im Buch wird als Beispiel ein Kochseminar
  verwendet.


Alle angemeldeten Benutzer können nun in diesem Ordner Artikel einsehen,
hinzufügen und bearbeiten.  

.. _sec_benutzer-redakteur:

Benutzer mit Redakteursfunktion
===============================

Beim Durcharbeiten des Tutoriums müssen die Benutzer in die Rolle eines
Redakteurs schlüpfen. Erzeugen Sie deshalb auf Ihrer Website einen Benutzer,
der diese Rechte besitzt. 


* Gehen Sie in das Konfigurationsmenü und wählen Sie dort den Eintrag
  »Benutzer und Gruppen« aus. 
* Betätigen Sie die Schaltfläche »Neuen Benutzer hinzufügen«.
* Füllen Sie das Registrierungsformular aus.
* Übertragen Sie anschließend diesem Benutzer im Tutoriumsordner die
  Funktion »Kann veröffentlichen«.


Kurznamen
=========

Die Bearbeitungsansicht von Artikeln hat zunächst kein Eingabefeld für den
Kurznamen. Damit Ihre Nutzer Kurznamen bearbeiten können, nehmen Sie folgende
Einstellung vor:

* Wählen Sie im Konfigurationsmenü den Punkt »Website«.
* Kreuzen Sie dort das Feld »Zeige Kurznamen der Artikel?« an, und
  speichern Sie das Formular.


.. _sec_selbstregistrierung:

Selbstregistrierung
===================

Per Voreinstellung können sich die Besucher einer Plone-Website nicht selbständig
registrieren. Falls gewünscht, muss die Selbstregistrierung eingeschaltet
werden:

* Wählen Sie im Konfigurationsmenü den Eintrag »Sicherheit«.
* Kreuzen Sie das Feld »Selbstregistrierung« an und speichern Sie das
  Formular.


Persönliche Ordner
==================

Per Voreinstellung werden keine persönlichen Ordner für registrierte Benutzer
der Website angelegt. Gegebenenfalls müssen Sie persönliche Ordner erst
einschalten:

* Wählen Sie im Konfigurationsmenü den Eintrag »Sicherheit«.
* Kreuzen Sie das Feld »Persönliche Benutzerordner« an und speichern Sie
  das Formular.


Gruppenarbeitsplätze
====================

Die Gruppenarbeitsplätze müssen erst aktiviert werden. Wenn Sie das tun,
richtet Plone den Gruppenbereich ein und erzeugt danach
selbständig Ordner für neu angelegte Gruppen. Gehen Sie dazu wie folgt vor:

* Wechseln Sie in das ZMI (die Zope-Management-Oberfläche).
* Wählen Sie aus dem Inhalt des Wurzelordners das Werkzeug
  ``portal_groups``.
* Betätigen Sie die Schaltfläche »Turn workspace creation on« (»Schalte
  die Erzeugung von Arbeitsplätzen ein«).

Lesezeichen
===========

Um Lesezeichen benutzen zu können, müssen Sie zwei Einstellungen an Ihrer
Website vornehmen: Zum einen brauchen Ihre Nutzer persönliche Ordner, in denen
ihre Lesezeichen abgelegt werden. Siehe dazu weiter oben in diesem Abschnitt.
Zum anderen müssen Sie die Artikelaktion »Lesezeichen hinzufügen« einschalten:

* Wechseln Sie in das ZMI (die Zope-Management-Oberfläche).
* Wählen Sie aus dem Inhalt des Wurzelordners das Werkzeug
  ``portal_actions``, darin den Unterordner
  ``document_actions`` und in diesem wiederum die Aktion
  ``addtofavorites`` (zu Lesezeichen hinzufügen).
* Kreuzen Sie das Feld »Visible« (»sichtbar«) an, und speichern Sie
  das Formular.


Wenn Sie darüber hinaus Ihren registrierten Benutzern das Lesezeichenportlet
zur Verfügung stellen möchten, legen Sie es wie folgt an:

* Wechseln Sie zur Startseite Ihrer Website.
* Folgen Sie dem Verweis »Portleteinstellungen« in der linken oder der
  rechten Seitenspalte.
* Wählen Sie aus dem Auswahlmenü ganz oben in der betreffenden Spalte den
  Eintrag »Klassisches Portlet«. Ist in Ihrem Browser Javascript
  ausgeschaltet, müssen Sie noch die Schaltfläche »Einstellungen speichern« am
  unteren Ende der gleichen Spalte betätigen.
* Sie gelangen nun zum Konfigurationsformular für das neue Portlet. Geben
  Sie dort als Vorlage \objectpath{portlet_favorites} und als Makro »portlet«
  an. Speichern Sie das Formular.
* Sie gelangen nun zurück zur Portletverwaltung, wo Sie die Portlets in
  den Seitenspalten umordnen und löschen können.


Syndizierung
============

Für Kollektionen ist die Syndizierung bereits eingeschaltet. Um die
Syndizierungseinstellungen bei Kollektionen ändern zu können und die
Syndizierung bei Ordnern einzuschalten, muss die Artikelansicht »Syndizierung«
sichtbar gemacht werden.

* Wechseln Sie in das ZMI (Zope Management Interface).
* Wählen Sie das Werkzeug ``portal_actions``, darin den
  Unterordner ``object`` und in diesem wiederum die Aktion
  ``syndication`` (Syndizierung).
* Kreuzen Sie das Feld »Visible« (»sichtbar«) an, und speichern Sie
  das Formular.

Wiki-Verweise
=============

Wenn Sie Ihren Benutzern die Verwendung von Wiki-Verweisen ermöglichen wollen,
gehen Sie folgendermaßen vor:

* Wählen Sie im Konfigurationsmenü den Eintrag »Textauszeichnung«.
* Wechseln Sie zum Formular »Wiki-Verhalten«.
* Kreuzen Sie die aufgeführten Artikeltypen an und speichern Sie das Formular.
