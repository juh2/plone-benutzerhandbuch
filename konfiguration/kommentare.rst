.. _sec_kommentierungseinstellungen:

============
 Kommentare
============

Die Kommentarfunktion lässt sich detailliert konfigurieren. Im
Konfigurationsmenü von Plone befindet sich ein Eintrag mit dem Namen
:guilabel:`Kommentare`. Über diesen Link gelangt man in das
Konfigurationsmenü für die Kommentarfunktion (siehe Abb.:
:ref:`fig_konfiguration-kommentare`). 


.. _fig_konfiguration-kommentare:

.. figure::
   ../images/konfiguration-kommentare.*
   :alt: Das Konfigurationsmenü für die Kommentarfunktion

   Das Konfigurationsmenü für die Kommentarfunktion

Folgende Optionen können eingestellt werden:

Kommentierungsfunktion generell einschalten
    Wenn hier ein Häkchen gesetzt ist, wird die Kommentierungsfunktion
    aktiviert. Wenn Kommentare generell nicht erwünscht sind,
    entfernen Sie das Häkchen. Die übrigen Optionen sind daraufhin
    nicht zugänglich.

Anonyme Kommentare
   Da Plone sehr differenziert als öffentliches Internetportal sowie
   als teilweise öffentliches oder geschlossenes Intranet betrieben
   werden kann, gibt es die Möglichkeit nicht angemeldeten Benutzern
   das Kommentieren zu erlauben.

Enable comment moderation
   Wenn man anonyme Kommentare erlaubt, ist es oftmals empfehlenswert,
   diese vor einer Veröffentlichung von einem Moderator sichten und
   freigeben lassen. Wenn dies der Fall ist, aktivieren Sie diese
   Option.

Text transformationen
   Eine Textauszeichnung (Formatierung) ist bei Kommentaren in der
   Regel nicht nötig. In der Voreinstellung wird daher die Texteingabe
   in reinen Text umgewandelt. Wenn Kommentare umfangreich formatiert werden
   sollen, können Sie den Benutzern die Eingabe von Markdown
   ermöglichen. Die dritte Eintellungsmöglichkeit ist »Intelligent
   text«. Bei dieser Option werden URLs und E-Mail-Adresse in Links
   konvertiert. Alle anderen Eingaben werden in reinen Text
   umgewandelt.

Captcha
   Um zu verhindern, dass durch Skripte automatisiert Kommentare
   erzeugt werden, können Captchs genutzt werden. Dazu müssen die
   angegebenen Erweiterungen installiert werden. Ansonsten kann hier
   keine Auswahl erfolgen.

Zeige das Portrait des Kommentators
   Wenn ein registrierter Benutzer kommentiert, erscheint sein
   Porträtfoto im Kommentar, wenn diese Option aktiviert ist.

Email-Benachrichtigungen für Moderatoren aktivieren
   Wenn diese Option aktiviert ist, erhält der Moderator eine E-Mail,
   wenn ein neuer Kommentar zu kontrollieren ist. Standardmäßig wird
   die E-Mail an die Adresse versendet, die in der E-Mail-Konfiguration
   angegeben wurde. Im Feld darunter kann eine alternative
   E-Mail-Adresse angegeben werden.

Moderator Email Address
   Hier kann eine E-Mail-Adresse angegeben werden, an die die
   Benachrichtigungen geschickt werden.

E-Mail-Benachrichtigungen für Benutzer aktivieren
   Diese Option ist standardmäßig aktiviert. Leider funktioniert sie
   wegen eines Bugs nicht. In einer zukünftigen Version von Plone
   könnte dieser Bug beseitigt sein. Wenn diese Option aktiviert ist,
   kann sich der Benutzer über weitere Kommentare zu einem Artikel per
   E-Mail informieren lassen. 
