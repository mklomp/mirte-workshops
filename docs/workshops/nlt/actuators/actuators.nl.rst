:orphan:

Actuatoren
########################

Introductie
-----------

Vorig hoofdstuk stond in het teken van het waarnemen van de omgeving met sensoren. Deze sensoren nemen fysische eigenschappen zoals geluid en licht uit de omgeving waar, wat de robot kan gebruiken. De informatie uit de omgeving wordt gebruikt in de "plannen & redeneren" stap om te bepalen wat de robot gaat doen. Het uiteindelijke 'doen' van de robot is de laatste stap en wordt wel 'actueren' of output genoemd. 

De meest bekende vorm van output in een robot is het aansturen van een motor. Hiermee kan bijvoorbeeld een wiel worden rondgedraaid of een robotarm worden verplaatst. Een andere manier van output kan zijn om de gebruiker van de robot inzicht te geven in de werking of status van de robot. Zo kan bijvoorbeeld een rood lampje gaan branden of een bepaald geluid worden uitgezonden. In dit geval zijn de actuatoren dan respectievelijk een lampje en een microfoon. Ook kan een tekst op een schermpje worden laten zien bij bepaalde gebeurtenissen om de gebruiker meer inzicht te geven in wat er in de robot gebeurt.

Zoals is uitgelegd, is een robot zonder sensoren 'blind' en 'doof', maar een robot zonder actuatoren is niet eens een robot. Zonder actuatoren kan een robot geen fysieke taak uitvoeren en is hoogstens een stuk software die iets kan beredeneren aan de hand van de sensorwaardes. Actuatoren zorgen ervoor dat de robot kan bewegen en interactie kan hebben met de omgeving, bijvoorbeeld het oppakken van objecten.


Opdracht:

Robots voeren vaak autonoom een bepaalde taak uit. Het is echter meestal niet zichtbaar wat er in de robot gebeurt. Als de robot even stil staat weet je bijvoorbeeld niet of hij iets aan het 'zoeken' is met de sensoren of aan het 'nadenken' is. In deze opdracht gaan we actuatoren gebruiken om deze interne processen aan de gebruiker van de robot duidelijk te maken.

Ontwerp een systeem voor een robot waarmee de robot de gebruiker inzicht kan geven in wat er in de robot gebeurt. Gebruik minimaal 3 verschillende actuatoren en 3 verschillende stukken informatie waar de robot de gebruiker over kan informeren. Maak een ontwerp op een A4 papier en presenteer jullie idee in 1 minuut aan 3 andere groepen.

Maak bij deze opdracht gebruik van de scientific approach (linkje). In dit geval doe je de observatie aan de hand van het hierboven geschetste 'probleem' wat zich met robots voordoet. Daarna doorloop je de volgende 2 stappen van de scientific approach. In plaats van een experiment te doen, presenteer en bediscuseer je jullie plan met andere groepen. Kijk kritisch naar elkaars ontwerp en kijk of je valkuilen of verbeterpunten kunt ontdekken. Daarna doe je een korte analyse en sluit je af met een conclusie.

TODO maak werkblad hierbij


Motoren (DC en Servo)
---------------------

Vorige les heeft een overzicht gegeven van verschillende vormen van actuatie en beschreven waarom een robot actuatoren nodig heeft. Deze les gaat in op de belangrijkste actuatoren voor robots, namelijk motoren. Twee veelgebruikte motoren worden behandeld, namelijk de Direct Current Motor (DC motor) en de Servo.

Een DC motor wordt gebruikt vanwege zijn continue rotatie. Dit betekent dat als je een DC Motor aanzet, hij rond zal blijven draaien. Dit is nodig om bijvoorbeeld een wiel voor een rijdende robot aan te sturen. Door het elektrische vermogen wat de motor ingaat aan te passen, kan de DC motor harder of zachter draaien.

Een Servo wordt gebruikt om heel precies een bepaalde orientatie te krijgen. De Servo kan bijvoorbeeld bewegen tussen 0 en 180 graden en kan heel precies naar een hoek van 35 graden worden gestuurd. Dit wordt bijvoorbeeld gebruikt om robotarmen naar specifieke posities te sturen en een grijper open en dicht te doen. Door het elektrische vermogen wat de motor ingaat aan te passen, kan de Servo meer kracht (torque) uitoefenen en zal deze sneller van positie kunnen wisselen (dit zal de tijd die het kost om van bijvoorbeeld 0 naar 50 graden te gaan, versnellen).

Om het verschil tussen een DC motor en een servo nog wat duidelijker te maken, is het goed om na te denken wat er zou gebeuren als we in bovenstaande voorbeelden de andere soort motor gebruiken.
Als een servo wordt gebruikt om een wiel aan te sturen van een rijdende robot, kan dit wiel draaien van 0 tot 180 graden en terug. Dit betekent dat de robot niet zou kunnen rijden, maar alleen een beetje heen en weer rolt op zijn plek. Als we daarentegen een DC motor zouden gebruiken om een robotarm aan te sturen, zou de arm constant rondjes blijven draaien. Naast dat dit niet praktisch is, is zo'n rondvliegende arm ook nog eens heel gevaarlijk. Het is dus belangrijk om het verschil tussen deze twee motoren te kunnen begrijpen om ze in de juiste toepassing te kunnen gebruiken.


Sluit de servo en de dc motor aan. 

1. Gebruik de scientific approach om vast te stellen of de wielen van de robot worden aangestuurd met een servo motor of met een dc motor (en schrijf op waarom).

2. Sluit nu allebei de wielen aan op de juiste motoren en monteer ze op de robot (als je dit nog niet hebt gedaan). Zet allebei de motoren aan en stel vast of ze de goede kant op draaien. Gebruik de scientific approach om ervoor te zorgen dat de wielen uiteindelijk de juiste kant op draaien corresponderend met de gegeven instructie (bijvoorbeeld, instructie: rechtdoor, allebei de wielen zorgen dat de robot rechtdoor rijdt).

3. Nu allebei de wielen van de robot dezelfde kant op draaien, kunnen we de snelheid en acceleratie van de robot gaan bepalen. Hiervoor gebruiken we wederom de scientific approach.
Voeg tekstblokjes toe 'hoe was het ook alweer' voor snelheid en acceleratie 
-> uiteindelijk hiermee een stukje onderbroken lijn overbruggen?

4. Ontwerp een grijper voor jouw robot. Afhankelijk van het materiaal dat voor jou beschikbaar is, maak je gebruik van 1 of 2 servo's. Ontwerp de grijper zo, dat de robot een object kan grijpen en op een later moment ook weer los kan laten. 


TODO: maak werkbladen hierbij
TODO: Opdracht 3 aanvullen

