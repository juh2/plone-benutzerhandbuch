.. _sec_konfiguration-email:

========
 E-Mail
========

Um wichtige Funktionen in Plone nutzen zu können, muss dem CMS ein
Ausgangsserver für E-Mails zur Verfügung stehen. Die Konfiguration des
E-Mail-Systems ist daher bei jeder Plone-Website notwendig, da es keine
Voreinstellung gibt (siehe Abbildung :ref:`fig_konfiguration-e-mail`).

.. _fig_konfiguration-e-mail:

.. figure::
   ../images/konfiguration-e-mail.*
   :width: 100%
   :alt: E-Mail-Konfiguration

   E-Mail-Konfiguration

SMTP-Server
   Dies ist der Ausgangsserver für E-Mails. In vielen Fällen können Sie hier
   »localhost« eintragen. Plone nutzt dann den auf dem Rechner installierten
   :term:`SMTP`-Server, um E-Mails zu versenden. Ansonsten können Sie auch
   einen entfernten SMTP-Server benutzen. Fragen Sie im Zweifelsfall Ihren
   Systemadministrator.

SMTP-Server-Port
   Der Standard-Port für E-Mail lautet »25«. Fragen Sie Ihren
   Systemadministrator nach dem richtigen Port.

ESMTP-Benutzername
   Falls Sie :term:`ESMTP` benutzen, benötigen Sie in der Regel einen
   Benutzernamen und ein Passwort, um den Mailausgangsserver nutzen zu können.
   Tragen Sie hier den Benutzernamen ein. 

ESMTP-Passwort
   Tragen Sie hier das Passwort für den oben angegebenen ESMTP-Benutzernamen
   ein.

Absendername der Website
   Plone verschickt in verschiedenen Situationen E-Mails. Tragen Sie hier einen
   sinnvollen Absendername ein, sodass der Empfänger weiß, woher die E-Mail
   kam. 

Absenderadresse der Website
   Tragen Sie hier eine gültige E-Mail-Adresse ein. Plone versendet E-Mails mit
   dieser Absenderadresse, sodass etwaige Antworten an diese E-Mail-Adresse
   zugestellt werden.
