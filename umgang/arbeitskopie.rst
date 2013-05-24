.. _sec_arbeitskopien:

===============
 Arbeitskopien
===============

Arbeitskopien erlauben es, einen öffentlich sichtbaren Artikel zu
bearbeiten, ohne dass die gespeicherten Zwischenstände öffentlich
einsehbar sind. Bevor Sie anfangen, einen Artikel auf diese Weise zu
bearbeiten, erstellen Sie zunächst eine Arbeitskopie des Artikels. In
dieser Arbeitskopie nehmen Sie alle Änderungen vor. Anschließend
ersetzen Sie den Originalartikel durch die veränderte Arbeitskopie.

.. _sec_arbeitskopie-erstellen:

Arbeitskopie erstellen
======================

Wenn Sie mit einer vor der Öffentlichkeit versteckten Arbeitskopie eines
Artikels arbeiten wollen, betätigen Sie im Menü »Aktionen« den Eintrag
»Arbeitskopie erstellen« (siehe Abbildung :ref:`fig_arbeitskopie-erzeugen`).

.. _fig_arbeitskopie-erzeugen:

.. figure:: ../images/arbeitskopie-erzeugen.*
   :width: 60%

   Eine Arbeitskopie erstellen

Wenn es auf Ihrer Website persönliche Ordner für die Benutzer gibt,
werden Sie zu einer Seite weitergeleitet, auf der Sie entscheiden
können, ob die Arbeitskopie in Ihrem persönlichen Ordner
(:guilabel:`Heimordner`) oder im gleichen Ordner wie das Original
(:guilabel:`Übergeordneter Ordner`) erstellt werden soll (siehe
Abbildung :ref:`fig_arbeitskopie-wohin`). Wenn es keine persönlichen
Ordner gibt, wird die Arbeitskopie ohne Nachfrage im übergeordneten
Ordner erzeugt.

.. _fig_arbeitskopie-wohin:

.. figure:: ../images/arbeitskopie-wohin.*
   :width: 100%

   Auswahl des Ortes für eine Arbeitskopie

Beide Möglichkeiten haben Vorteile: Erstellen Sie die Arbeitskopie an
der gleichen Stelle wie das Original also im übergeordneten Ordner,
wenn Sie mit anderen Benutzern zusammen daran arbeiten
wollen. Anderenfalls kann es sinnvoll sein, Arbeitskopien in Ihrem
Ordner zu erstellen, um sie nicht mit den Originalen zu vermischen
oder um den Überblick über Ihre Arbeitskopien zu behalten. Denken Sie
auch daran, dass Arbeitskopien in veröffentlichten Ordnern durchaus
öffentlich einsehbar und sogar in der Navigation erscheinen
können, falls ihr Revisionsstatus das zulässt. Entscheiden Sie anhand
solcher Überlegungen von Fall zu Fall, was sinnvoller ist.

Eine Arbeitskopie hat zwar den gleichen Arbeitsablauf wie der
Originalartikel, aber ihre Statusänderungen sind nicht an die des
Originals gebunden. Sie können eine Arbeitskopie in einem
veröffentlichten Ordner beispielsweise jederzeit in den Status
»privat« versetzen, um sie vor der Öffentlichkeit zu verbergen. Dabei
bleibt der Status des Originals unberührt. 

Der Status einer neu erstellten Arbeitskopie ist der Anfangsstatus des
jeweiligen Arbeitsablaufs, unabhängig davon, in welchem Status sich
das Original gerade befindet.

Sobald die Arbeitskopie erstellt ist, können Sie sie in gewohnter
Weise bearbeiten.

.. _fig_statusmeldung-arbeitskopie:

.. figure:: ../images/statusmeldung-arbeitskopie.*
   :width: 100%

   Statusmeldung beim Aufruf einer Arbeitskopie

Beim Aufruf einer Arbeitskopie erhalten Sie eine Statusmeldung (siehe
Abbildung :ref:`fig_statusmeldung-arbeitskopie`), die Sie darauf
hinweist, dass Sie eine Arbeitskopie betrachten. Die Meldung enthält
einen Verweis auf das Original, den Benutzernamen desjenigen, der die
Arbeitskopie erstellt hat und einen Verweis auf die Anzeige der
Veränderungen, die diese Arbeitskopie im Vergleich zum Original
enthält.

Wenn Sie einen Artikel aufrufen, den Sie bearbeiten dürfen und von dem
es eine Arbeitskopie gibt, werden Sie mit einer Statusmeldung über die
existierende Arbeitskopie informiert. Wird die Arbeitskopie gerade von
einem anderen Benutzer bearbeitet, dann erhalten Sie zusätzlich den
Hinweis, dass der Artikel für die Bearbeitung gesperrt wurde (siehe
Abbildung :ref:`fig_statusmeldung-arbeitskopie-gesperrt`).

.. todo:: Neuer Screenshot und Übersetzung geradeziehen

.. _fig_statusmeldung-arbeitskopie-gesperrt:

.. figure:: ../images/statusmeldung-gesperrt-arbeitskopie.*
   :width: 100%

   Statusmeldung wegen gesperrter Arbeitskopie

.. _sec_orig-durch-arbe:

Original durch Arbeitskopie ersetzen
====================================

Wenn Sie in der Arbeitskopie Ihre Änderungen durchgeführt haben und die
geänderte Fassung nun verwenden möchten, ersetzen Sie das Original durch die
Arbeitskopie. Dafür enthält das Aktionsmenü der Arbeitskopie den Eintrag
»Original durch Arbeitskopie ersetzen« (siehe
Abbildung :ref:`fig_original-durch-arbeitskopie-ersetzen`).

.. _fig_original-durch-arbeitskopie-ersetzen:

.. figure:: ../images/original-durch-arbeitskopie-ersetzen.*
   :width: 60%

   Aktionsmenü mit Einträgen für Arbeitskopien

Bei diesem Vorgang wird das Original mit der Arbeitskopie
überschrieben und die Arbeitskopie selbst gelöscht. Sie werden zu
einer Seite weitergeleitet, auf der Sie eine Änderungsnotiz eingeben
können (siehe Abbildung :ref:`fig_arbeitskopie-checkin-msg`).

.. Screenshot enthält noch falsche Übersetzung

.. _fig_arbeitskopie-checkin-msg:

.. figure:: ../images/arbeitskopie-checkin-msg.*
   :width: 100%

   Original durch eine Arbeitskopie ersetzen

Diese Eingabe erfüllt den gleichen Zweck wie die Änderungsnotiz in der
Bearbeitungsansicht. Sie erscheint in der tabellarischen Auflistung
früherer Versionen eines Artikels (siehe dazu
Abschnitt :ref:`sec_versionierung`).

Beachten Sie jedoch, dass Sie das Original nur dann durch die
Arbeitskopie ersetzen können, wenn Sie es immer noch bearbeiten
dürfen. Das kann beispielsweise dann nicht der Fall sein, wenn sich
der Status des Originals in der Zwischenzeit geändert hat. Sie können
die Arbeitskopie daher auch zur Veröffentlichung einreichen. Dann
ersetzt ein Redakteur das Original durch die Arbeitskopie.

Wenn Sie eine Arbeitskopie nicht nutzen wollen, können Sie sie über den
Eintrag :guilabel:`Arbeitskopie verwerfen` im Aktionsmenü wieder
löschen. Um ein versehentliches Verwerfen zu verhindern, fragt Plone
nach, ob die Arbeitskopie tatsächlich verworfen werden soll (siehe
Abbildung :ref:`fig_arbeitskopie-verwerfen`)

.. _fig_arbeitskopie-verwerfen:

.. figure:: 
   ../images/arbeitskopie-verwerfen.*
   :width: 100%

   Nachfrage, ob Arbeitskopie verworfen werden soll

Zugriffsberechtigungen und Arbeitsabläufe
=========================================

Damit man mit Hilfe von Arbeitskopien Inhalte pflegen kann, müssen bestimmte
Voraussetzungen bei den Freigabeeinstellungen und den Arbeitsabläufen
erfüllt sein.

+--------------------------------------+----------------------------------------------------------------------+
| Arbeitsschritt                       | Einstellung in Ansicht ›Freigabe‹                                    |
+======================================+======================================================================+
| Arbeitskopie erstellen               | »Kann hinzufügen« im übergeordneten Ordner                           |
+--------------------------------------+----------------------------------------------------------------------+
| Arbeitskopie bearbeiten              | »Kann bearbeiten« im übergeordneten Ornder oder in der Arbeitskopie  |
+--------------------------------------+----------------------------------------------------------------------+
| Arbeitskopie verwerfen               | »Kann bearbeiten« im übergeordneten Ordner oder in der Arbeitskopie  | 
+--------------------------------------+----------------------------------------------------------------------+
| Original durch Arbeitskopie ersetzen | »Kann bearbeiten« im übergeordneten Ordner                           |
+--------------------------------------+----------------------------------------------------------------------+

Wenn also Autoren die Möglichkeit haben sollen, Inhalte in
Arbeitskopien zu erstellen, das Original aber nicht durch die
Arbeitskopie ersetzen sollen, darf man ihnen in der Freigabe des
übergeordneten Ordners nicht die Bearbeitungsfunktion (Kann
bearbeiten) zuweisen, sondern lediglich das Recht, Artikel – in diesem
Fall die Arbeitskopie – hinzuzufügen (Kann hinzufügen).

Sollen mehrere Personen die Arbeitskopie bearbeiten, sollten Sie ihnen
nur in der Freigabe der Arbeitskopie selbst die Funktion »Kann
bearbeiten« zuweisen, nicht im übergeordneten Ordner.

Beachten Sie, dass derjenige, der das (veröffentlichte) Original durch
die (private) Arbeitskopie ersetzen kann, dadurch auch die Inhalte,
die in der Arbeitskopie privat waren, veröffentlichen kann. Wenn das
Original durch die Arbeitskopie ersetzt wird, übernimmt das veränderte
Original den Status des ursprünglichen Originals. War das
ursprüngliche Original veröffentlicht, wird auch das veränderte
Original veröffentlicht sein.

