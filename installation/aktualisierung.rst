====================================
 Aktualisierung (Upgrade) von Plone
====================================

Wenn eine neue Version von Plone herauskommt, stellt sich die Frage, ob man eine laufende Plone-Website aktualisieren soll. Die Plone-Community stellt für die Aktualisierung älterer Versionen, Upgrade-Skripts bereit, die eine Standard-Plone-Website – also eine Plone-Website ohne Erweiterungen und eigene Anpassungen – auf den aktuellen Stand bringen. Eine solche einfache Aktualisierung wird in diesem Kapitel beschrieben. 

Vorbereitung
============

.. warning:: Bevor Sie die hier beschriebenen Schritte durchführen, erstellen Sie bitte unbedingt ein Backup Ihrer Plone-Website. Es wird keine Gewähr für die Richtigkeit der hier beschriebenen Schritte gegeben. Sie nutzen die folgenden Hinweise auf eigene Verantwortung.

Aktuelle Version bestimmen
--------------------------

Öffnen Sie das Konfigurationsmenü Ihrer Plone-Website und schauen Sie nach, mit welcher Version Ihre Website zurzeit läuft (siehe dazu Kapitel :ref:`sec_konfiguration-menu`). Die im Konfigurationsmenü angegebene Plone-Version bezeichnen wir im Folgenden als Ausgangsversion und die neue Version als Zielversion. Durch einen Vergleich der Versionsnummern können Sie feststellen, ob es sich um einen kleineren (Minor) oder größeren (Major) Release-Schritt handelt. Wenn sich Ausgangs- und Zielversion nur an der dritten Stelle voneinander unterscheiden, handelt es sich um ein neues Minor-Release. Ein Beispiel wäre der Wechsel von 4.0.2 zu 4.0.3, der im Folgenden beschrieben wird.

Ein größerer Release-Schritt ist der Wechsel von 4.0.2 zu 4.1.0. Und ein Upgrade auf eine komplett neue Version liegt vor, wenn Sie beispielsweise von 3.3.5 auf 4.0.3 aktualisieren möchten.

Der Wechsel von einer Minor-Release zur nächsten sollte bei einer Standard-Plone-Website ohne Probleme möglich sein. 

Erweiterungen und Anpassungen überprüfen
----------------------------------------

Kontrollieren Sie alle installierten Erweiterungen (siehe dazu Kapitel
:ref:`sec_konfiguration-erweiterungen`). Denn sobald Erweiterungen ins Spiel
kommen, wird es schwieriger. Zunächst sollten Sie klären, ob für die von Ihnen
benutzten Erweiterungen aktuelle Versionen zur Verfügung stehen, die
nachweislich mit der Zielversion zusammenarbeiten. Das Gleiche gilt natürlich
auch für Anpassungen, die Sie selbst vorgenommen haben, und Erweiterungen, die
Sie selbst entwickelt haben. Auf der Website http://plone.org/products können
Sie nach Erweiterungen für spezielle Plone-Versionen suchen.  

Falls Sie für die von Ihnen genutzten Erweiterungen keine neuen Versionen finden, die mit der Zielversion Ihrer Plone-Instanz zusammenspielen, ist eine Aktualisierung nicht so ohne Weiteres möglich. Sie müssten entweder auf die Erweiterung verzichten – sie also vor der Aktualisierung deinstallieren – oder diese selbst so anpassen, dass sie mit der Zielversion von Plone zusammen funktioniert. Leider gab und gibt es Erweiterungen, die auch nach einer Deinstallation Spuren in Ihrer Instanz hinterlassen und eine einfache Aktualisierung verhindern. Deshalb sollten Sie jede Aktualisierung zunächst an einem Testsystem ausprobieren und niemals direkt ein Produktivsystem aktualisieren. Außerdem sollten Sie vorher ein Backup Ihres Systems erstellen. Konsultieren Sie in jedem Fall den offiziellen Upgrade-Guide_ für Plone!

.. _Upgrade-Guide: http://plone.org/documentation/manual/upgrade-guide 

Upgrade auf ein neues Minor-Releases
====================================

Im Folgenden wird eine Aktualisierung auf eine neues Minor-Release beschrieben. 

Stoppen Sie Ihre Plone-Instanz.

Öffnen Sie die Datei :file:`buildout.cfg` in einem Editor Ihrer Wahl und suchen Sie den Abschnitt ``extends``. Wenn Sie Plone mit Hilfe eines Installers installiert haben, sieht der Abschnitt ungefähr so aus: ::

  extends = 
      base.cfg
      versions.cfg
  #    http://dist.plone.org/release/4.0.2/versions.cfg

In dem Abschnitt ``extends`` werden die Definitionen der Datei
:file:`buildout.cfg` durch Definitionen aus den Dateien
:file:`base.cfg` und :file:`versions.cfg` erweitert. In der Datei
:file:`base.cfg` finden Sie Einstellungen, die über viele Versionen
hinweg gleich bleiben. In der Datei :file:`versions.cfg` werden die
Versionsnummern für die :term:`Python-Eggs <Egg>` festgelegt, die in
der gewünschten Version genutzt werden. Diese Datei wird vom
Installier mitgeliefert. Sie ist aber auch online über die angegebene
und auskommentierte Webadresse erreichbar.

Kommentieren Sie die Zeile mit der lokalen Datei :file:`versions.cfg` aus und entfernen Sie das Kommentarzeichen in der folgenden Zeile und ändern Sie die Versionsnummer. In unserem Beispiel wollen wir von 4.0.2 auf 4.0.3 aktualisieren. ::

  extends = 
      base.cfg
  #    versions.cfg
      http://dist.plone.org/release/4.0.3/versions.cfg

Speichern Sie die Änderung und rufen Sie :program:`buildout` auf. ::

  ./bin/buildout

Es erscheinen diverse Meldungen, die Ihnen anzeigen, dass neue Versionen der verschiedenen Python-Eggs aus dem Netz geladen und installiert werden. Darunter befindet sich auch eine Meldung, dass das neue Egg für Plone 4.0.3 installiert wird. ::

  Getting distribution for 'Plone==4.0.3'.

Wenn :program:`buildout` erfolgreich durchgelaufen ist, haben Sie Ihre Installation aktualisiert. Das heißt, es sind nun sämtliche Eggs für die Zielversion installiert. Nun müssen Sie nur noch das Upgrade-Skript innerhalb Ihrer Plone-Instanz laufen lassen, damit auch Ihre Plone-Website selbst aktualisiert wird. Starten Sie dazu Ihre Plone-Instanz. ::

  ./bin/instance start

Rufen Sie Ihre Instanz im Browser zum Beispiel unter der Url ``http://localhost:8080`` auf. Sie sehen dort den Hinweis, dass Ihre Plone-Instanz aktualisiert werden muss (siehe Abbildung :ref:`fig_aktualisierung-1`).

.. _fig_aktualisierung-1:

.. figure::
   ../images/aktualisierung-1.*
   :width: 100%
   :alt: Startbildschirm mit dem Hinweis zur Aktualisierung

   Startbildschirm mit dem Hinweis zur Aktualisierung

Um Ihre Plone-Website auf die aktuelle Version zu bringen, betätigen Sie die Schaltfläche :guilabel:`Aktualisieren...`. Sie gelangen dadurch zu der Aktualisierungsseite für die jeweilige Plone-Website (siehe Abbildung :ref:`fig_aktualisierung-2`)

.. _fig_aktualisierung-2:

.. figure::
   ../images/aktualisierung-2.*
   :width: 80%
   :alt: Aktualisierungsbildschirm

   Aktualisierungsbildschirm

Die Seite ist folgendermaßen aufgebaut:

Ganz oben finden Sie einen Link zu der Website, die aktualisiert werden soll. Darunter finden Sie einen Verweis zum oben erwähnten Upgrade-Guide_. 

Darunter, im Bereich :guilabel:`Aktualisierung`, werden Sie noch einmal darauf hingewiesen, ein Backup Ihrer Plone-Website zu erstellen. Dies ist spätestens jetzt empfehlenswert. Bis zu diesem Punkt haben Sie noch keine Änderung an Ihrer Datenbank und damit an Ihrer laufenden Plone-Website vorgenommen. Sie könnten die Aktualisierung noch rückgängig machen, indem Sie in der Datei :file:`buildout.cfg` die Änderungen rückgängig machen und :program:`buildout` erneut aufrufen. Nach der Aktualisierung der Datenbank ist dies nicht mehr möglich. 

Unterhalb der Warnung wird angegeben, welche Konfiguration zurzeit aktiv ist, und welche Konfiguration als letzte zur Verfügung steht. Um zur letzten Konfiguration zu gelangen, sind :guilabel:`Aktualisierungsschritte` notwendig, die darunter aufgelistet sind. Bei einem Minor-Release wie in unserem Beispiel sind dies nur wenige, beim Wechsel auf eine neue Major-Release können es sehr viel mehr Aktualisierungsschritte sein. Es wird beschrieben, was in dem jeweiligen Schritt verändert wird. 

Wenn Sie Ihre Website aktualisieren wollen, betätigen Sie die Schaltfläche :guilabel:`Aktualisierung`. Es empfiehlt sich zunächst einen Probelauf zu machen, ohne die Datenbank zu verändern. Markieren Sie dazu das Kästchen :guilabel:`Probelauf` und klicken Sie auf :guilabel:`Aktualisierung`. 

Wenn Sie einen Probelauf machen, gelangen Sie automatisch zu dieser Seite zurück. Unterhalb der Schaltfläche :guilabel:`Aktualisierung` erscheint der :guilabel:`Aktualisierungsreport` (siehe Abbildung :ref:`fig_aktualisierung-3`). 

.. _fig_aktualisierung-3:

.. figure::
   ../images/aktualisierung-3.*
   :width: 80%
   :alt: Der Aktualisierungsreport nach einem Probelauf 

   Aktualisierungsreport nach Probelauf 

Wenn Sie die Website tatsächlich aktualisieren, gelangen Sie zum Startbildschirm zurück, auf dem Sie die Bestätigung finden, dass Ihre Website nun aktuell ist (siehe Abbildung :ref:`fig_aktualisierung-4`). 

.. _fig_aktualisierung-4:

.. figure::
   ../images/aktualisierung-4.*
   :width: 80%
   :alt: Startbildschirm mit der Meldung, dass die Website aktuell ist

   Startbildschirm mit Erfolgsmeldung
