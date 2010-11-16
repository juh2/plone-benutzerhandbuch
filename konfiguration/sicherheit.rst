.. _sec_konfiguration-sicherheit:

============
 Sicherheit
============

In den Sicherheitseinstellungen (Abbildung:
:ref:`fig_konfiguration-sicherheitseinstellungen`) können Sie verschiedene
Punkte konfigurieren, die Auswirkungen auf die Sicherheit einer Plone-Website
haben. Plone ist nach der Installation so eingestellt, dass die höchste
Sicherheitsstufe aktiv ist. Das bedeutet, dass Sie die Sicherheit einer
Plone-Website reduzieren, wenn Sie hier Änderungen vornehmen.

.. _fig_konfiguration-sicherheitseinstellungen:

.. figure::
   ../images/konfiguration-sicherheitseinstellungen.*
   :width: 100%
   :alt: Das Formular zur Konfiguration diverser Punkte

   Sicherheitseinstellungen

Folgende Optionen können Sie aktivieren:

Selbstregistrierung
    Wenn Sie anonymen Besuchern Ihrer Website erlauben, sich selbst auf der
    Website zu registrieren, müssen Sie die angelegten Konten regelmäßig
    kontrollieren, da immer wieder versucht wird, mit Hilfe von automatisierten
    Skripten Konten auf Websites anzulegen und diese Konten anschließend zum
    Beispiel für Spam zu missbrauchen. 

Registrierung ohne Prüfung der E-Mail-Adresse
    Wenn bei der Registrierung eines Benutzers auf die Prüfung der
    E-Mail-Adresse verzichtet wird, kann man mit Hilfe von automatisierten
    Skripten sehr viel leichter ein Benutzerkonto einrichten und dieses dann
    missbrauchen. Aktivieren Sie diese Option nur dann, wenn Sie wissen, was
    Sie tun.  

Persönlicher Benutzerordner
    Wenn Sie für Ihre Benutzer persönliche Benutzerordner anlegen, können die
    Benutzer in diesen Ordner schalten und walten, wie Sie möchten, was auch
    den Missbrauch einschließt. Sorgen Sie daher dafür, dass der Inhalt der
    persönlichen Benutzerordner regelmäßig kontrolliert wird und dass Inhalte
    nicht automatisch für alle Besucher der Website sichtbar sind. 

Verfasserzeile öffentlich anzeigen
    Die Verfasserzeile wird in der Regel nur angemeldeten Benutzern angezeigt.
    Wird Sie jedem Besucher der Website angezeigt, kann auch jeder Besucher
    Informationen über den Verfasser auf seiner persönlichen Seite abrufen, da
    sich in der Verfasserzeile ein Verweis zu dieser Seite befindet. Dies ist
    nicht immer wünschenswert. 

Benutze E-Mail-Adresse als Anmeldename
    Die Benutzung einer E-Mail-Adresse statt eines Benutzernamens ist auf
    vielen Websites mittlerweile gang und gäbe. Dabei wird oft vergessen, dass
    bei der Anmeldung über `http` Benutzername und Passwort im Klartext an den
    Server gesendet werden. Jeder, der Zugriff auf den Übertragungsweg hat, kann
    diese Informationen abfangen. Falls Sie E-Mail-Adressen statt der
    Benutzernamen für die Anmeldung benutzen, werden gültige E-Mail-Adressen
    übertragen, die für Spamversender interessant sein können. 

