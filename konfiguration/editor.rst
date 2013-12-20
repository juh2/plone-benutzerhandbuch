.. _sec_konfiguration-editor:

========================
Visueller Editor TinyMCE
========================

Der Texteditor, mit dem Autoren und Redakteure Inhalte in Plone einpflegen
können, lässt sich konfigurieren. Über den Verweis :guilabel:`Visueller Editor
TinyMCE` gelangen Sie in den Konfigurationsbereich des Editors. Die
Konfiguration besteht aus drei Teilformularen (siehe Abbildung
:ref:`fig_konfiguration-tinymce-1`) 

.. _fig_konfiguration-tinymce-1:

.. figure::
   ../images/konfiguration-tinymce-1.*
   :width: 80%
   :alt: Einstellungen von TinyMCE

   Einstellungen von TinyMCE

Teilformular Layout
===================

Im ersten Teilformular werden Einstellungen gemacht, die sich auf das Aussehen
des Texteditors auswirken.

Größenveränderung des Editor-Fensters einschalten
   Wenn Sie diese Funktion einschalten, kann der Benutzer die Größe von
   Formularfeldern im Texteditor verändern (siehe Abbildung
   :ref:`fig_tinymce-fenstergroesse-veraendern`) Rechts unten in 
   veränderbaren Formularfeldern gibt es einen Anfasser. Sobald sich die Maus
   über dem Anfasser befindet, verändert sich der Mauszeiger. Die Größe wird
   geändert, indem man die Maustaste gedrückt hält und die Größe durch
   Verschieben der Maus einstellt.   
   
   .. _fig_tinymce-fenstergroesse-veraendern:
   .. figure::
      ../images/tinymce-fenstergroesse-veraendern.*
      :width: 100%
      :alt: An der rechten unteren Ecke kann die Größe des Fensters verändert
            werden.

      Anfasser für Größenänderung

Automatische Größenveränderung des Editorfensters einschalten.
   Wenn Sie die Option einschalten, passt sich das Editorfenster in der Größe
   dem bearbeiteten Inhalt automatisch an. Es wird also automatisch so groß
   eingestellt, dass der gesamte Inhalt ohne Scrollen innerhalb des
   Formularfeldes sichtbar ist. Je nach Größe von Monitor und Inhalt kann
   jedoch ein Scrollen im Browser weiterhin notwendig sein.  
Breite des Editors
   Mit dieser Option können Sie die Breite des Editorfensters in Pixel oder
   Prozent (der Browsergröße) einstellen. Wenn die Breite des Editorfenster
   prozentual festgelegt ist, kann die Größe der Formularfelder nur vertikal
   verändert werden. 
Höhe des Editors
   Mit dieser Option können Sie die Höhe des Editorfensters in Pixeln
   bestimmen. Wenn die automatische Größenanpassung eingeschaltet ist, wird der
   eingegebene Wert als minimale Höhe genutzt.
Schreibrichtung
   Mit dieser Option legen Sie die Schreibrichtung fest. Einige Sprache wie
   Hebräisch, Arabisch oder Urdu laufen von rechts nach links anstatt von links
   nach rechts.
Kontextmenü einschalten
   Mit dieser Option können Sie das Kontextmenü ein- und ausschalten. Die
   Funktion wird in Kapitel :ref:`sec_tinymce-kontext-menu` näher beschrieben. 
Das CSS wählen, das im WYSIWYG-Editorbereich genutzt wird
   Wenn Sie diese Option auswählen, können Sie eine eigene CSS-Datei bestimmen,
   die die CSS-Datei des Themes ersetzt. Die CSS-Datei wird im Texteditor im
   Bearbeitungsfeld benutzt. Sie muss sich im ZMI im Ordner
   :file:`portal_skins/custom` befinden oder als Bestandteil eines Themes in
   der CSS-Registry :file:`portal_css` registriert sein. 
Stile
   In diesem Fenster werden die Stile festgelegt, die über die Stilauswahl
   eingefügt werden können. Pro Zeile wird ein Stil definiert. Dabei wird ein
   bestimmtes Schema verlangt: ``Bezeichnung|HTML-Tag`` beziehungsweise
   ``Bezeichnung|CSS-Klasse``. Stile mit HTML-Tag sind zum Beispiel::

      Heading|h2
      Subheading|h3
      Literal|pre

   Im Auswahlmenü für den Stil erscheinen die Begriffe »Heading«, »Subheading«
   und »Literal« beziehungsweise die entsprechenden Übersetzungen. In den Code
   werden die HTML-Tags ``h2``, ``h3`` und ``pre`` eingefügt. 

   Einige Stile stehen nur in einem bestimmten Kontext im Stilmenü zur Auswahl
   zur Verfügung. Dies sind zum Beispiel Listenstile wie::

      Disc|ul|listTypeDisc
      Square|ul|listTypeSquare
      Circle|ul|listTypeCircle
      
   Sie sind im Stilmenü aufgeführt, wenn sich der Cursor in einer bestimmten
   Umgebung, hier in einer Liste, befindet. Ihr Bezeichnungsschema ist etwas
   anders: ``Bezeichnung|Umgebung|Klasse``.  Die Umgebung im angeführten
   Beispiel ist ``ul`` (unordered list/unsortierte Liste). Die Klassen, die in
   den HTML-Code eingetragen werden, heißen: ``listTypeDisc``,
   ``listTypeSquare`` und ``listTypeCircle`` und die Bezeichnungen, die im
   Stilmenü auftauchen, lauten »Disc«, »Square« und »Circle«. Beachten Sie,
   dass die Bezeichnungen in Plone standardmäßig übersetzt werden. Sie müssen
   hier also keine deutschen Bezeichnungen eintragen. 

   Falls Ihr Theme eigene Stile definiert, können Sie diese hier eintragen,
   damit Ihre Benutzer sie bequem im Texteditor benutzen können.  
         
Tabellenstile
   In diesem Fenster sind die Stile für Tabellen definiert. Das
   Bezeichnungsschema entspricht dem der anderen Stile. 

Teilformular Werkzeugleiste
===========================

Im Teilformular Werkzeugleiste können Sie in der Hauptsache die Funktionen
auswählen, die in der Werkzeugleiste zur Verfügung stehen sollen (siehe
Abbildung :ref:`fig_konfiguration-tinymce-2`). 

.. _fig_konfiguration-tinymce-2:

.. figure::
   ../images/konfiguration-tinymce-2.*
   :width: 40%
   :alt: Das Teilformular Werkzeugleiste zur Auswahl der Funktionen in TinyMCE

   Teilformular Werkzeugleiste

Breite der Werkzeugleiste
   Hiermit bestimmen Sie die Breite der Werkzeugleiste in Pixeln.
Extern
   Wenn Sie diese Option einschalten, wird die Werkzeugleiste nicht direkt am
   oberen Rand des Formularfeldes angezeigt, sondern ganz oben über der
   gesamten Webseite. 
Sichern
   Sichert den Inhalt des Formularfeldes ohne die gesamte Seite neu zu laden.
Ausschneiden
   Diese Funktion wird in einigen Browsern aus Sicherheitsgründen unterdrückt.
Kopieren
   Diese Funktion wird in einigen Browsern aus Sicherheitsgründen unterdrückt.
Einfügen
   Diese Funktion wird in einigen Browsern aus Sicherheitsgründen unterdrückt.
Als einfachen Text einfügen
   Diese Funktion ermöglicht es, formatierte Inhalte aus der Zwischenablage als
   einfachen Text einzugeben.
Von Word einfügen
   Bei dieser Funktion werden störende Formatierungen aus Texten, die über die
   Zwischenablage aus Word übernommen werden, entfernt.   
Rückgängig
   Macht die letzte Aktion rückgängig.
Wiederholen
   Führt die rückgängig gemachte Aktion erneut aus.
Finden
   Öffnet den Suchdialog.
Suchen/Ersetzen
   Öffnet den Such- und Ersetzen-Dialog
Stil auswählen
   Das Stilauswahlmenü
Fett
   Markierter Text wird fett dargestellt.
Kursiv
   Markierter Text wird kursiv dargestellt.
Unterstrichen
   Markierter Text wird unterstrichen.
Durchgestrichen
   Markierter Text wird durchgestrichen.
Tiefgestellt
   Markierter Text wird tiefgestellt.
Hochgestellt
   Markierter Text wird hochgestellt.
Vordergrundfarbe
   Werkzeug zur Auswahl der Textfarbe. Die Eingaben werden in Plone in der
   Regel herausgefiltert. Wenn Sie diese Funktion benötigen, passen Sie die
   :ref:`HTML-Filter <sec_konfiguration-html-filter>` an.
Hintergrundfarbe
   Werkzeug zur Auswahl der Hintergrundfarbe. Die Eingaben werden in Plone in
   der Regel herausgefiltert. Wenn Sie diese Funktion benötigen, passen Sie die
   :ref:`HTML-Filter <sec_konfiguration-html-filter>` an.
Linksbündig
   Der Absatz, in dem sich der Cursor befindet, wird linksbündig gesetzt.
Zentriert
   Der Absatz, in dem sich der Cursor befindet, wird zentriert gesetzt.
Rechtsbündig
   Der Absatz, in dem sich der Cursor befindet, wird rechtsbündig gesetzt.
Blocksatz
   Der Absatz, in dem sich der Cursor befindet, wird im Blocksatz dargestellt.
Ungeordnete Liste
   Eine unsortierte Liste wird erzeugt.
Geordnete Liste
   Eine Aufzählungsliste wird erzeugt.
Definitionsliste
   Eine Definitionsliste wird erzeugt.
Ausrücken
   Der Absatz, in dem sich der Cursor befindet, wird nach links ausgerückt.
Einrücken
   Der Absatz, in dem sich der Cursor befindet, wird eingerückt.
Tabellenbedienung
   Werkzeug zur Anlage einer Tabelle
Link einfügen/bearbeiten
   Werkzeug zum Einfügen eines Verweises
Verweis entfernen
   Der Verweis unter dem Cursor wird entfernt.
Anker einfügen/bearbeiten
   Werkzeug zur Erstellung von Ankern.
Bild einfügen/bearbeiten
   Werkzeug zum Einfügen und Bearbeiten von Bildern
Mediendatei einfügen/bearbeiten
   Werkzeug, um Videos einzufügen. Der :ref:`HTML-Filter
   <sec_konfiguration-html-filter>` von Plone verhindert in der Voreinstellung
   die Einbindung von Medien-Dateien. Damit Sie Medien-Dateien einbinden
   können, müssen Sie die entsprechenden Filterregeln im Konfigurationsbereich
   :ref:`HTML-Filter <sec_konfiguration-html-filter>` anpassen. 
Eigene Zeichen eingeben
   Werkzeug zur Eingabe von Sonderzeichen
Horizontales Lineal einfügen
   Funktion steht in Plone nicht zur Verfügung.
Erweitertes horizontales Lineal einfügen
   Funktion steht in Plone nicht zur Verfügung.
Datum eingeben
   Das aktuelle Datum wird eingefügt.
Zeit einfügen
   Die aktuelle Uhrzeit wird eingefügt.
Emoticons
   Funktion steht in Plone nicht zur Verfügung.
Festes Leerzeichen eingeben
   Funktion steht in Plone nicht zur Verfügung.
Seitenumbruch einfügen
   Funktion steht in Plone nicht zur Verfügung. Nutzen Sie stattdessen im
   Stilmenü den Eintrag :guilabel:`Seitenumbruch`. 
Drucken
   Druckt den Inhalt des Editorfensters aus.
Vorschau
   Öffnet ein Fenster mit einer Vorschau, in die jedoch keine Stilinformationen
   (CSS) eingebunden sind. Da der Text im Editorfenster von Plone in der Regel
   bereits formatiert angezeigt wird, ist diese Funktion überflüssig und daher
   in der Voreinstellung nicht aktiv.
Rechtschreibprüfung
   Funktion steht in Plone nicht zur Verfügung. Nutzen Sie die
   Rechtschreibprüfung, die in Ihrem Browser ohnehin zur Verfügung steht.
Formatierung entfernen
   Funktion steht in Plone nicht zur Verfügung
Unordentlichen Code aufräumen
   Funktion steht in Plone nicht zur Verfügung. Unordentlicher Code wird in
   Plone durch einen speziellen HTML-Filter aufgeräumt. 
Hilfslinien und unsichtbare Objekte einblenden
   Funktion steht in Plone nicht zur Verfügung.
Formatierungszeichen ein- und ausschalten
   Funktion steht in Plone nicht zur Verfügung.
Attribut einfügen/bearbeiten
   Werkzeug zur Einstellung der Schreibrichtung.
HTML bearbeiten
   Werkzeug zur direkten Bearbeitung des HTML-Codes
In Vollbildmodus umschalten
   Bringt den Texteditor in den Vollbildmodus.
Angepasster Schalter in Werkzeugbalken
   Funktion steht in Plone nicht zur Verfügung.

.. todo:: Letzte Funktion überprüfen, geht vielleicht doch 

Teilformular Ressourcentypen
============================

In diesem Teilformular werden Einstellungen vorgenommen, die sich auf die
Ressourcen beziehen, mit denen TinyMCE arbeitet.

.. _fig_konfiguration-tinymce-3:

.. figure::
   ../images/konfiguration-tinymce-3.*
   :width: 50%
   :alt: Das Teilformular Ressourcentypen 

   Teilformular Ressourcentypen

Verweise mit UID
   Wenn diese Option aktiviert ist verweisen interne Links, die innerhalb von
   TinyMCE eingefügt werden, nicht auf den Pfad des Artikels, sondern auf seine
   UID (Unique ID). Dadurch ist gewährleistet, dass ein Verweis auch dann
   funktioniert, wenn der referenzierte Artikel verschoben wurde. 
Bilder mit Legende erlauben
   Wenn Sie diese Option einschalten, erhalten eingefügte Bilder automatisch
   eine Bildlegende, die entweder aus der Beschreibung des Bildes gewonnen wird
   oder manuell eingegeben werden kann.
Verwurzelt im aktuellen Artikel
   Wenn diese Option eingeschaltet wird, kann der Benutzer nur Bilder einfügen,
   die sich im gleichen Ordner befinden, wie der bearbeitete Artikel. Das
   Gleiche gilt für Verweise. 
Enthält Objekte
   Damit TinyMCE weiß, welche Artikel in Plone als Ordner fungieren, die andere
   Artikel enthalten können, müssen diese Artikeltypen hier eingetragen werden.
   Im Wesentlichen sind dies die Artikeltypen ``Folder``, ``Large Plone
   Folder`` und die ``Plone Site`` selbst. Wenn Sie eigene, ordnerartige
   Artikeltypen erstellen, tragen Sie diese hier ein. 
Enthält Anker
   Damit TinyMCE weiß, welche Artikel Anker enthalten können, müssen die
   entsprechenden Artikeltypen hier eingetragen sein. Wenn Sie eigene
   Artikeltypen erstellen, die Anker enthalten können, tragen Sie diese hier
   ein.
Referenzierbares Objekt 
   Damit TinyMCE weiß, auf welche Objekte verwiesen werden kann, müssen die
   entsprechenden Artikeltypen hier eingetragen sein. Wenn Sie eigene
   Artikeltypen erstellen, auf die verwiesen werden soll, tragen Sie sie hier
   ein.  
Bildobjekt
   Damit TinyMCE weiß, welche Artikeltypen als Bilder fungieren, müssen die
   entsprechenden Artikeltypen hier eingetragen werden. Wenn Sie eigene
   Artikeltypen für Bilder erstellen, tragen Sie diese hier ein. 
Angepasstes Plugin
   In diesem Feld sind Plugins aufgelistet, die von TinyMCE genutzt werden. 
Datensatzkodierung
   Mit diesem Schalter können Sie festlegen, wie TinyMCE die eingegebenen Texte
   abspeichert. Zur Auswahl stehen:
   
   * Unbearbeitet (Sonderzeichen werden nicht verändert)
   * Benannt (Sonderzeichen werden als benannte Zeichen gespeichert (Beispiel:
     ``&auml;`` für »ä«)
   * Numerisch (Sonderzeichen werden in numerischer Notation gespeichert
     (Beispiel: ``&#228;`` für »ä«)
