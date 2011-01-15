.. _sec_benutz-registr:

=======================
 Benutzer registrieren
=======================

Die Registrierung eines neuen Benutzers kann durch den Administrator oder den
Benutzer selbst erfolgen. Letzteres ist nur möglich, wenn die Website
entsprechend konfiguriert ist.

.. _sec_registr-durch-den:

Registrierung durch den Administrator
=====================================

Wenn Ihr Administrator für Sie einen Benutzerzugang eingerichtet hat,
erhalten Sie eine Aktivierungs-E-Mail mit einem Link zu einer Seite,
auf der Sie ein Passwort für Ihren Zugang wählen können. Auf dieser
Seite befindet sich ein Formular mit drei Eingabefeldern (siehe
Abbildung :ref:`fig_passwort-setzen`):

Mein Benutzername ist
  Ihr Benutzername ist bereits eingetragen. Sie
  sollten ihn nicht ändern.

Neues Passwort
  Geben Sie in dieses Feld das Passwort ein, das Sie
  benutzen wollen. Es muss mindestens fünf Zeichen lang sein.

Passwort wiederholen
  Da das Passwort nicht angezeigt wird, müssen Sie
  hier das gleiche Passwort erneut eingeben, um ein versehentliches Vertippen
  auszuschließen.

.. _fig_passwort-setzen:

.. figure::
   ../images/passwort-setzen.*
   :width: 80%
   :alt: Das Formular zum Setzen eines neuen Passwortes

   Formular zum Setzen des Passworts

Der Link zu dieser Seite ist 7 Tage lang gültig. Nach Ablauf dieser Zeit ist
eine neue Registrierung notwendig.

Durch die Wahl eines eigenen Passworts wird sichergestellt, dass
niemand außer Ihnen selbst, nicht einmal der Administrator, Ihr
Passwort kennt.

.. _sec_registr-durch-den-1:

Registrierung durch den Benutzer selbst
=======================================

Wenn sich Benutzer auf Ihrer Website selbst registrieren dürfen,
finden Sie im Benutzermenü den Verweis :guilabel:`Registrieren`, der
Sie zum Registrierungsformular führt. Alternativ können Sie auch dem
Verweis »Neuer Benutzer?« im Anmeldeportlet (siehe Abbildung
:ref:`fig_portlet-login`) oder im Anmeldeformular (siehe Abbildung
:ref:`fig_anmeldeformular`) folgen, um dorthin zu gelangen.

Das Registrierungsformular ist folgendermaßen aufgebaut:

Vor- und Nachname
  Geben Sie hier Ihren vollen Namen ein.

Benutzername
  Wählen Sie einen kurzen und prägnanten Benutzernamen. Mit
  diesem Namen melden Sie sich künftig an der Website an. Falls dieses
  Feld fehlt, ist die Website so konfiguriert worden, dass beim
  Anmelden statt des Benutzernamens die E-Mail-Adresse benutzt wird. 

E-Mail
  Geben Sie eine gültige E-Mail-Adresse ein. An diese Adresse
  sendet Plone unter anderem eine Aktivierungs-E-Mail, wenn Sie Ihr Passwort
  vergessen sollten. Je nach Konfiguration benötigen Sie die
  E-Mail-Adresse auch bei der Anmeldung.

Betätigen Sie nach der Eingabe die Schaltfläche :guilabel:`Registrieren`.

Falls das Registrierungsformular nur diese drei Formularfelder
enthält, müssen Sie die Registrierung in einem zweiten Schritt
abschließen. Sie erhalten eine Aktivierungs-E-Mail mit einem Link zu
der Seite, auf der Sie ein Passwort eingeben können.

Anderenfalls enthält das Registrierungsformular zwei weitere Felder, wo Sie
ein Passwort für Ihren Benutzerzugang eingeben können:

Passwort
  Geben Sie hier das gewünschte Passwort ein.

Passwort bestätigen
  Geben Sie das Passwort erneut ein, um ein Vertippen
  auszuschließen.

Betätigen Sie zum Abschluss die Schaltfläche :guilabel:`Registrieren`. 

.. _fig_willkommen-anmelden:

.. figure:: ../images/willkommen-anmelden.*

   Bestätigung der Registrierung

Nachdem Sie registriert sind, erhalten Sie die in Abbildung
:ref:`fig_willkommen-anmelden` gezeigte Begrüßungsnachricht. Wenn Sie
dort die Schaltfläche »Anmelden« betätigen, werden Sie automatisch
angemeldet (siehe Abbildung :ref:`fig_anmeldebestaetigung`:).

.. todo:: Übersetzung geändert, neuen Screenshots einfügen

.. _fig_anmeldebestaetigung:

.. figure::
   ../images/anmeldebestaetigung.*
   :width: 80%
   :alt: Anmeldebestätigung mit Hinweis auf das Benutzermenü

   Anmeldebestätigung mit Hinweis auf das Benutzermenü

.. _sec_passwort-vergessen:

Passwort vergessen?
===================

Wenn Sie Ihr Passwort vergessen haben, können Sie sich eine neue
Aktivierungs-E-Mail zusenden lassen. Folgen Sie dem Verweis
:guilabel:`Passwort vergessen?` im Anmeldeportlet oder dem Verweis
unter der Überschrift »Passwort vergessen?« im Anmeldeformular. Diese
Verweise führen Sie zu einem Formular (siehe Abbildung
:ref:`fig_passwort-vergessen-formular`), auf dem Sie Ihren
Benutzernamen oder Ihre E-Mail-Adresse eingeben und anschließend die
Schaltfläche :guilabel:`E-Mail anfordern` betätigen müssen. Sie erhalten
daraufhin eine E-Mail, die ähnlich aufgebaut ist wie die
Aktivierungs-E-Mail. Auch sie enthält einen Verweis zu einer Seite,
auf der Sie ein neues Passwort eingeben können.

.. _fig_passwort-vergessen-formular:

.. figure:: ../images/passwort-vergessen-formular.*
   :width: 80%
   :alt: Formular zur Eingabe des Benutzernamens

   Passwort vergessen
