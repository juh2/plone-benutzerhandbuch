Installation unter Linux
========================

Laden Sie von plone.org bzw. launchpad.net\ [#]_ das gepackte Archiv mit dem :term:`Unified Installer`
für Linux herunter und entpacken Sie das Archiv.::

    wget https://launchpad.net/plone/4.3/4.3/+download/Plone-4.3-UnifiedInstaller.tgz 

    tar -xvf Plone-4.3-UnifiedInstaller.tgz

Wechseln Sie anschließend in den entstandenden Ordner. [#]_ ::

    cd Plone-4.3-UnifiedInstaller

In der Datei :file:`README.txt`, die sich in dem Archiv befindet, stehen
Informationen darüber, welche Optionen Ihnen bei der Installation von Plone zur
Verfügung stehen. Diese sind kurzgefasst folgende:

* Installation als root
* Installation ohne Root-Rechte
* Stand-alone Installation
* ZEO Cluster Installation

Installation als root
---------------------

Bei dieser Installationsart wird Plone im Pfad :file:`/usr/local/Plone`
installiert. Außerdem wird ein Benutzer ›plone‹ mit eingeschränkten Rechten
erzeugt, unter dem Zope laufen wird. Plone muss dann entweder mit
:command:`sudo` oder als root gestartet werden.

Installation ohne Root-Rechte
-----------------------------

Sie können Plone unter Ihrem normalen Benutzerkonto
installieren. Plone wird dann in Ihrem Heimverzeichnis installiert
unter :file:`$HOME/Plone`. Sie müssen sich dann mit Ihrem
Benutzernamen anmelden, um Plone zu starten. Plone wird mit Ihren
Benutzerrechten laufen. Dies ist in der Regel für Produktivsysteme
nicht wünschenswert.

Stand-alone-Installation
------------------------

Bei einer Stand-alone-Installation wird eine einfache Zope-Instanz installiert.
Dies ist für Entwicklungszwecke und zum Ausprobieren ausreichend. 

Installieren Sie Plone mit folgendem Befehl bei einer root-Installation: ::

    sudo ./install.sh standalone

Oder ohne sudo, wenn Sie eine Installation in Ihrem Benutzerordner vornehmen möchten: ::

    ./install.sh standalone

ZEO-Cluster-Installation
------------------------

Bei einer ZEO-Cluster-Installation werden Vorkehrungen zum Loadbalancing
getroffen. Es werden ein ZEO-Server und zwei Zope-Clients installiert. Wählen Sie
diese Installationsart für Produktivsysteme. 

Auch hier können Sie die Installation als root mit :command:`sudo` oder unter
Ihrem eigenen Benutzernamen vornehmen. ::

    sudo ./install.sh zeo

Oder: ::

    ./install.sh zeo

In der Datei :file:`README.txt` finden Sie weitere Installationsoptionen.

Starten von Plone
-----------------

Bei einer systemweiten Installation (Root-Installation) starten Sie Plone mit dem Befehl: ::

    sudo /usr/local/Plone/zinstance/bin/plonectl start

Um Plone zu stoppen, benutzen Sie den Befehl: ::

    sudo /usr/local/Plone/zinstance/bin/plonectl stop

Um herauszufinden, ob Plone läuft, benutzen Sie den Befehl: ::

    sudo /usr/local/Plone/zinstance/bin/plonectl status

Bei einer Installation in Ihrem Benutzerordner ändern sich die Pfade entsprechend: ::

    $HOME/Plone/zinstance/bin/plonectl start

    $HOME/Plone/zinstance/bin/plonectl stop

    $HOME/Plone/zinstance/bin/plonectl status


Bei einer ZEO-Cluster-Installation lauten die Befehle: ::

    sudo /usr/local/Plone/zeocluster/bin/plonectl start

    sudo /usr/local/Plone/zeocluster/bin/plonectl stop

    sudo /usr/local/Plone/zeocluster/bin/plonectl status

Oder: ::

    $HOME/Plone/zeocluster/bin/plonectl start

    $HOME/Plone/zeocluster/bin/plonectl stop

    $HOME/Plone/zeocluster/bin/plonectl status


Nach dem Starten können Sie die Instanz in Ihrem Browser unter der Adresse
http://localhost:8080 aufrufen.


.. [#] Launchpad.net benutzte zur Zeit der Niederschrift ein 
   selbst-signiertes Zertifikat. :command:`wget` weigert sich in einem
   solchen Fall, eine Verbindung zu dem Server aufzunehmen. Rufen Sie
   :command:`wget` mit der Option :command:`--no-check-certificate`
   auf, um den Installer herunterzuladen.

.. [#] Bitte beachten Sie, dass das Beispiel von der Version 4.3
   ausgeht. Die Version 4.3 wird von der Plone Community laufend
   gepflegt. Es erscheinen kleinere Aktualisierungen, die die
   Bezeichnung 4.3.X tragen, wobei X eine Zahl ist, die fortlaufend
   erhöht wird. 4.3.4 ist die vierte Maintenance-Release nach
   4.3. Konsultieren Sie plone.org, um die aktuelle Version
   herunterzuladen.
