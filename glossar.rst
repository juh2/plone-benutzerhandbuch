.. _glossary:

=======
Glossar
=======

.. glossary::
   :sorted:

   Plone
      Plone ist ein webbasiertes in Python programmiertes
      Content-Management-System, das unter den GNU Public License
      (GPL) vertrieben wird. 

   Artikel
      Die Inhalte in Plone können sehr unterschiedlichen Charakter
      haben. Es kann sich dabei um Texte und Bilder, aber auch um
      Termine, Dateien und Links handeln. Durch Erweiterungen sind
      noch viele andere Arten von Inhalten denkbar. Alle Artikel werden
      als einzelne Objekte in der Datenbank
      gespeichert. Man kann sich die Inhaltsobjekte wie Artikel in
      einem Kaufhaus vorstellen.    
   
   Artikeltypen 
      Die Struktur eines Artikels wird durch seinen Typ bestimmt. Der
      Artikeltyp ist so aufgebaut, dass er eine bestimmte Information
      besonders gut transportieren kann. In einem Termin kann man
      beispielsweise ein Datum und eine Uhrzeit in einem eigenen Feld
      speichern. Alle Artikeltypen in Plone sind von einem
      einheitlichen Schema (Archetypes) abgeleitet. So haben
      beispielsweise alle Artikel einen Titel, eine Beschreibung sowie
      den gleichen Satz an Metadaten zur Verfügung.

   Ansicht
      Um einen Artikel in Plone anzuzeigen oder zu bearbeiten, muss
      man ihn in eine Anzeige- oder Bearbeitungsmaske laden. Diese
      Masken werden in Plone als Ansichten bezeichnet. Die Ansichten
      können sehr unterschiedlich aussehen, je nachdem zu welchem
      Zweck sie dienen.

   Benutzer
      Jeder, der eine Website ansteuert, die mit Plone betrieben wird,
      ist ein Benutzer. Um zu verhindern, dass jeder Benutzer auf alle
      Artikel und Funktionen in Plone zugreifen kann, ist es nötig,
      berechtigte Personen von nicht berechtigten zu
      unterscheiden. Dafür werden Benutzer in Plone registriert,
      sodass sie sich anmelden und gegenüber dem System durch ihren
      Benutzernamen und ihr Passwort ausweisen können. 

   Bitmap-Grafik
      Eine Bitmap-Grafik auch Rastergrafik oder Pixelgrafik genannt,
      besteht aus einer rasterförmigen Anordnung von Bildpunkten
      (Pixeln), denen jeweils eine Farbe zugeordnet ist. Scanner oder
      Digitalkameras erzeugen Bitmap-Grafiken. Bekannte Formate sind
      GIF, JPEG, PNG oder TIFF. Die Bildgröße wird in Pixeln
      gemessen. Rastergrafiken lassen sich nicht beliebig vergrößert
      darstellen, ohne das irgendwann das Pixelmuster mit bloßem Augen
      zu erkennen ist. 

   Buildsystem
      Ein Buildsystem ist ein Programm, durch das ein fertiges
      Anwendungsprogramm automatisch erzeugt wird. 

   Buildout
      Buildout (genauer zc.buildout) ist ein python-basiertes
      Buildsystem, mit dem Webanwendungen automatisch installiert
      werden. Buildout wird von einem Konfigurationsskript
      gesteuert. Komplexe Anweisungen sind in Rezepten (recipes)
      zusammengefasst. Buildout lädt die benötigten Softwarepakete aus
      dem Internet herunter und installiert und konfiguriert sie auf
      dem Server. Mit Buildout lassen sich nicht nur die
      Softwarepakete installieren, aus denen Plone besteht. Buildout
      kann auch Webserver, Load-Balancer und Cachingsysteme
      konfigurieren.

      Der Vorteil von Buildout liegt in der Reproduzierbarkeit
      komplexer Installationen auf beliebigen Rechnern. Mit Hilfe
      kaskadierender Konfigurationsskripte kann man ein und dieselbe
      Anwendung automatisiert als Testsystem, Entwicklungsumgebung oder
      Produktivsystem konfigurieren. 

   Markdown
      Markdown ist eine vereinfachte Markup-Sprache. (siehe
      Restructured Text)

   Restructured Text 
      Restructured Text ist eine vereinfachte
      Markup-Sprache. Restructured Text macht es möglich, in einer
      reinen Textdatei, Texte inhaltlich zu gliedern und
      auszuzeichnen, ohne dafür eine komplizierte Markup wie HTML zu
      benutzen. Der mit Restructured Text strukturierte Text wird
      anschließend von Plone verarbeitet und voll formatiert in HTML
      dargestellt.

   S5
      S5 ist ein Präsentationsystem, das auf XHTML und CSS basiert und
      damit vom Hersteller und Betriebssystem unabhängig
      ist. S5-Präsentationen laufen im Browser ab.

   Zope-Management-Interface 
      Das Zope-Management-Interface (ZMI) ist
      die Bedienungsoberfläche für die Zope-2-Applikationsserver. Das
      ZMI ermöglicht die Programmierung von Webanwendungen
      »throught-the-web« unter Python. Da Plone auf dem
      Applikationsserver aufsetzt, kann Plone teilweise über das ZMI
      konfiguriert werden. 

   ZMI
      (siehe Zope-Management-Interface)

   ZODB
      Die Zope Object Database (ZODB) ist eine transaktionale
      Objektdatenbank zur persistenten Speicherung von
      Python-Objekten. Sie entspricht dem ACID-Standard.

   Paster 
      Paster ist ein Skript mit dem sich Plone installieren lässt. Es
      ist außerdem ein Werkzeug für Entwickler, mit dem man die
      Ordnerstruktur von Python-Modulpaketen und Python-Eggs erzeugen
      kann. Dabei werden alle Ordner und Dateien erzeugt, die
      standardmäßig vorhanden sein müssen. Der Entwickler kann sich
      dann auf die Implementierung der gewünschten Funktion
      konzentrieren.

   kanonische Sprache
      Mit der kanonischen Sprache wird in LinguaPlone die Grundsprache bezeichnet,
      die als Grundlage für alle Übersetzungen dient.

   sprachunabhängig
      Plone kann Artikel abhängig von der Sprache, in der sie
      geschrieben sind, behandeln. Dies kann beispielsweise dazu führen, dass
      Artikel in Englisch nur angezeigt werden, wenn der Benutzer die
      englische Version der Website betrachtet. Artikel, die von
      dieser Sprachwahl nicht betroffen sein sollen, müssen als
      sprachunabhängig gekennzeichnet werden.

   Tooltip
      Ein Tooltip ist ein kleines Popup-Fenster, in dem Hilfetexte zu
      Links und Bedienungselementen erscheinen.  

   Widget
      Ein Widget ist ein Element einer grafischen
      Benutzeroberfläche. Dies kann beispielsweise ein
      Bedienungsknopf, ein Auswahlmenü oder ein Eingabefeld sein. 

   Validator
      Ein Validator prüft, ob eine Formulareingabe ein bestimmtes
      Format besitzt und beispielsweise formal eine gültige
      E-Mail-Adresse darstellt.

   Validierung
      Als Validierung wird ein Prozess bezeichnet, in dem geprüft
      wird, ob eine Eingabe bestimmte formale Bedingungen
      erfüllt. Damit werden ungültige Eingaben verhindert. Mit Hilfe
      einer Validierung kann auch die Eingabe von Schadcode verhindert
      werden, sodass man die Validierung als Teil des
      Sicherheitssystems einer Website begreifen kann.   

   SSL
      Secure Sockets Layer (SSL), ist ein Verschlüsselungsprotokoll
      zur sicheren Datenübertragung im Internet.

   Öffentlicher Schlüssel 
      Unter einem öffentlichen Schlüssel versteht
      man in der Kryptologie einen Teilschlüssel eines asymmetrischen
      Kryptosystems, der vom Schlüsselinhaber veröffentlicht wird. Er
      bildet damit das Gegenstück zum privaten Schlüssel, der nur dem
      Schlüsselinhaber bekannt ist. Die Verschlüsselung mit
      öffentlichen Schlüsseln bietet (gegenüber der symmetrischen
      Verschlüsselung) den Vorteil, dass der auszutauschende Schlüssel
      nicht über einen sicheren Kanal übertragen werden muss, sondern
      öffentlich ist. Zur Übertragung des Schlüssels kann man sich
      daher eines Verbunds von Schlüsselservern bedienen, auf die
      jeder seine öffentlichen Schlüssel hochladen kann und von denen
      jeder den Schlüssel der Person abrufen kann, mit der er
      kommunizieren möchte. (Quelle:
      http://de.wikipedia.org/wiki/Öffentlicher_Schlüssel)

   Keyring
      Der Schlüsselring, in dem man seine eigenen und die öffentlichen
      Schlüssel anderer Personen sammelt.

   Egg
      Python-Eggs sind versionierte Modulpakete, die in Form eines
      Verzeichnisses oder in gezippter Form vorliegen können und
      Metainformationen (zum Beispiel Abhängigkeiten) enthalten. Da
      sie versioniert sind, können mehrere Versionen des gleichen
      Pakets auf einem Rechner installiert sein. Die gewünschte
      Version wird dann zur Laufzeit des Programms importiert. 

   SMTP
      Das Simple Mail Transfer Protocol (SMTP, zu deutsch etwa
      Einfaches E-Mail-Sendeverfahren) ist ein Protokoll, das zum
      Austausch von E-Mails in Computernetzen dient. Es wird dabei
      vorrangig zum Einspeisen und zum Weiterleiten von E-Mails
      verwendet. (Quelle: http://de.wikipedia.org/wiki/SMTP)

   ESMTP
      Extended SMTP (ESMTP) ermöglicht die Erweiterung des
      SMTP-Protokolls zum Beispiel um eine Authentifizierung oder eine
      Verschlüsselung.

   Theme
      Ein Theme ist ein installierbares Design für Plone. 

   HTML-Tag
      Die Hypertext Markup Language (HTML,
      dt. Hypertext-Auszeichnungssprache) ist eine textbasierte
      Auszeichnungssprache zur Strukturierung von Inhalten wie Texten,
      Bildern und Hyperlinks in Dokumenten. HTML-Dokumente sind die
      Grundlage des World Wide Web und werden von einem Webbrowser
      dargestellt. Neben den vom Browser angezeigten Inhalten einer
      Webseite enthält HTML zusätzliche Angaben in Form von
      Metainformationen. Die Elemente der Auszeichnungssprache werden
      als Tags bezeichnet. (Quelle: http://de.wikipedia.org/wiki/HTML-Tag)

   XHTML 
      Der W3C-Standard ›Extensible HyperText Markup Language‹
      (erweiterbare HTML; Abkürzung: XHTML) ist eine textbasierte
      Auszeichnungssprache zur Strukturierung und semantischen
      Auszeichnung von Texten, Bildern und Hyperlinks in
      Dokumenten. Es ist eine Neuformulierung von HTML 4.01 in
      XML. (Quelle: http://de.wikipedia.org/wiki/XHTML)

   CSS
      Cascading Style Sheets (Abk.: CSS) ist eine deklarative
      Stylesheet-Sprache für strukturierte Dokumente. Sie wird vor
      allem zusammen mit HTML und XML eingesetzt. CSS legt dabei fest,
      wie ein besonders ausgezeichneter Inhalt oder Bereich
      dargestellt werden soll. (Quelle:
      http://de.wikipedia.org/wiki/Cascading_Style_Sheets)

   Structured Text
      Structured Text ist eine vereinfachte Markup-Sprache (siehe Restructured Text).

   Textile
      Textile ist eine vereinfachte Markup-Sprache (siehe Restructured Text).

   Preformatted Text
      Text, der in einem <pre>-Tag steht, wird so dargestellt, wie er
      formatiert wurde. So werden beispielsweise Einrückungen bei der
      Darstellung beachtet.  

   Tar 
      Tar ist der Name eines Archivierungsprogramms. Mit ihm können
      Dateien in einem Verzeichnisbaum in eine Datei geschrieben
      werden. 

   Produktionsmodus
      Wenn eine Plone-Site im Produktionsmodus läuft, werden CSS- und
      Javascript-Daten gecacht. Änderungen in CSS- und Javascript-Dateien
      wirken sich deshalb nicht auf das Verhalten und das Aussehen der Website
      aus.

   Entwicklungsmodus
      Läuft eine Plone-Site im Entwicklungsmodus, werden CSS- und
      Javascript-Daten nicht gecacht, sodass Veränderungen, die ein Entwickler
      vornimmt sich sofort auswirken. 

   Rolle
      Das Rechtemanagement von Plone basiert auf Rollen (in Plone Funktionen
      genannt). Zahlreiche einzelne Berechtigungen werden dabei in
      einer Rolle zusammengefasst. Dem Benutzer werden so nicht mehr
      einzelne Berechtigungen zugeteilt, sondern eine Rolle. Dies
      dient vor allem der Übersichtlichkeit, da in einem CMS wie Plone eine
      Vielzahl von einzelnen Berechtigungen vorhanden sind. 

   XCode
      Die Anwendung Xcode ist eine von Apple bereitgestellte
      integrierte Entwicklungsumgebung zur nativen Softwareentwicklung
      für Mac OS X. Durch seine Modularität und die Unterstützung von
      weiteren Sprachen wie C, C++, Java, Python, Ruby und Perl ist es
      auch dazu geeignet, plattformübergreifende Software zu
      entwickeln. (Quelle: http://de.wikipedia.org/wiki/XCode)

   Metatag
      Das Metatag oder Meta-Element dient in HTML- oder
      XHTML-Dokumenten zum Angeben von Metadaten. Die Metadaten werden
      im Kopf-Bereich eines HTML-Dokuments, also im head-Element,
      notiert. (Quelle: http://de.wikipedia.org/wiki/Meta-Element)

   Unified Installer
      Der Unified Installer ist ein Installationsprogramm, mit dem
      die Python-, Zope- und Plone-Quellen auf unix-basierten
      Betriebssystemen installiert werden. 

   HTTP
      Das Hypertext Transfer Protocol (HTTP, dt.
      Hypertext-Übertragungsprotokoll) ist ein Protokoll zur Übertragung von
      Daten über ein Netzwerk. Es wird hauptsächlich eingesetzt, um Webseiten
      aus dem World Wide Web (WWW) in einen Webbrowser zu laden. (Quelle:
      Wikipedia)

   HTTPS
      HTTPS steht für HyperText Transfer Protocol Secure (dt. sicheres
      Hypertext-Übertragungsprotokoll) und ist ein Verfahren, um Daten im World
      Wide Web abhörsicher zu übertragen. (Quelle: Wikipedia) 

   FTP
      Das File Transfer Protocol (dt. Dateiübertragungsverfahren, kurz FTP),
      ist ein 1985 spezifiziertes Netzwerkprotokoll zur Übertragung von Dateien
      über IP-Netzwerke.  

   Interface
      Ein Interface ist ein Python-Objekt, das das nach außen hin gerichtete
      Verhalten eines Objekts beschreibt. Die Spezifizierung des Verhaltens
      erfolgt durch Dokumentation im Docstring des Interfaces sowie durch die
      Definition von Attributen und Invarianten. Interfaces bilden die
      Grundlage des komponentenbasierten Programmierens.

   Portlet 
      Ein Portlet ist eine Komponente innerhalb der Benutzeroberfläche
      einer Website, deren Inhalt ganz oder teilweise unabhängig von
      den übrigen Informationen auf der jeweils angezeigten Website
      erzeugt wird. Sie werden bei der Darstellung einer Webseite an
      bestimmten Stellen eingeblendet.
       
   Protokollebene
      Die Protokollebene (engl. logging level) bestimmt den Zweck oder die
      Wichtigkeit eines Protokolleintrags. Wenn ein protokolliertes Ereignis
      den Betrieb einer Anwendung gefährdet, bezeichnet man es als kritisch.
      Der entsprechende Protokolleintrag bekommt die Bezeichnung ›CRITICAL‹.
      Ist ein Fehler passiert, der keine gefährliche Auswirkung auf den Betrieb
      hat, so erhält der Protokolleintrag die Bezeichnung ›ERROR‹. Wurden
      bestimmte Grenzwerte festgelegt, so wird das Erreichen oder Überschreiten
      der Grenzwerte häufig als Warnung im Protokoll verzeichnet. Die
      entsprechende Protokollebene heißt ›WARNING‹. Dient der Eintrag nur
      Informationszwecken, so ordnet man den Eintrag der Protokollebene ›INFO‹
      zu. Die niedrigste Protokollebene lautet ›DEBUG› ihr werden
      Protokolleinträge zugeordnet, die dazu dienen sollen, den Ablauf eines
      Computerprogramms nachzuvollziehen und aktiv Fehler zu suchen.   


