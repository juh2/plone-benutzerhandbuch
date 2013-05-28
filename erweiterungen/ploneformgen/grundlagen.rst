============
 Grundlagen
============

Formulare haben die Aufgabe, den Benutzern ein Schema zur Eingabe von
Informationen vorzugeben. Sie spielen bei einem CMS wie Plone eine
große Rolle. Alle Inhalte werden mit Hilfe von Formularen
erstellt. Sie geben dem Benutzer vor, wo er beispielsweise den Titel
eines Artikels eingeben muss, und sie unterstützen ihn bei der Eingabe
durch Auswahlmenüs, Auswahllisten und andere :term:`Widgets <Widget>`.

Formulare dienen jedoch nicht nur der Eingabeunterstützung. Sie kontrollieren
im Zusammenspiel mit :term:`Validatoren <Validator>` die Gültigkeit und
Zulässigkeit der eingegebenen Information und weisen ungültige Eingaben zurück.
Wird vom Benutzer die Eingabe einer E-Mail-Adresse verlangt, muss das Formular
sicherstellen, dass der Benutzer wirklich eine E-Mail-Adresse und nicht etwa
irrtümlich eine Postleitzahl oder sogar böswillig Schadcode eingibt.

Die Artikeltypen in Plone werden mit Hilfe von Formularen erstellt,
die vom Benutzer nicht verändert werden können. Der Typ eines Artikels
legt vielmehr fest, wie das Formular aussieht, mit dem die
entsprechenden Eingaben getätigt werden. 

Aufgrund der zunehmenden Digitalisierung benötigt man jedoch immer
häufiger komplexe Online-Formulare für Verwaltungszwecke, bei Umfragen
oder bei Prüfungen. Um den Aufbau solcher Formulare zu vereinfachen, wurde
PloneFormGen entwickelt. Mit PloneFormGen lassen sich beliebig
strukturierte Formulare für jeden nur denkbaren Zweck erstellen. 
