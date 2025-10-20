:orphan:

Algoritmes
########################

Introductie
-----------

Tot nu toe hebben we de singalen van de sensoren uitgelezen en onafhankelijk hiervan de actuatoren aangestuurd. In deze module gaan we de signalen van de sensoren interpreteren en gebruiken om de actuatoren aan te sturen. Daarnaast worden systemen om de robot *aftypen* 


Proportionele Controller
------------------------

Om de sensorgegevens te verwerken en op de juiste manier de actuatoren aan te sturen, wordt gebruik gemaakt van een zogenoemde 'controlmethode'. Omdat het hier gaat om het direct aansturen van hardware, wordt een low-level controlmethode gebruikt. De meest eenvoudige methode is het implementeren van een zogenoemde 'P-Controller'. Hoe dit precies werkt, is het best uit te leggen aan de hand van een voorbeeld.

Stel het doel is dat een robot precies 10 km/u rijdt. Wanneer de robot minder hard rijdt dan 10 km/u, moet er gas worden gegeven en wanneer de robot harder rijdt dan 10 km/u, moet er worden afgeremd.
Ten eerste moet de huidige snelheid worden vergeleken met het setpoint van 10 km/u, hier komt dan een 'error' waarde uit:

error = 10 km/u - huidige_snelheid

Deze error wordt vermenigvuldigd met een contstante Kp, die bepaalt hoe erg gereageerd wordt op de error: bij een hoge Kp wordt er heel agressief gereageerd op de error, bij een lage Kp waarde minder agressief.

Output = Kp * error = Kp * (10 km/u - huidige_snelheid)

De output waarde wordt naar de actuatoren gestuurd, in dit geval de motoren. Een positieve error betekent dat de huidige snelheid lager is dan het setpoint, dus moeten de motoren hard vooruit draaien. Bij een negatieve error is de huidige snelheid hoger dan het setpoint, dus moeten de motoren de andere kant opdraaien om de robot af te remmen. Hoe verder de huidige waarde van het setpoint is, hoe groter of meer negatief de output is en hoe meer de motoren dus gaan compenseren. 

Door elke tijdstap het bovenstaande uit te rekenen en de signalen naar de motoren te sturen, kan de robot zo goed mogelijk op de gewenste snelheid te laten rijden. Dit systeem is ook ingebouwd in alle moderne auto's: cruise control.



Opdracht: bouw (in stappen) een proportionele controller om een bepaalde afstand van de muur te houden.


(intro voor opdracht)
In de module 'Sensoren' is behandeld hoe de ultrasoon sensor werkt. Zorg dat je eerst deze opdracht hebt afgerond, voordat je deze opdracht gaat doen.

	1. Lees de ultrasoonsensor uit en sla deze waarde op in de variabele huidige_afstand
	2. Maak een nieuwe variabele, gewenste_afstand, aan en sla de waarde 8 hierin op 
	3. Bereken de error en sla deze op in een nieuwe variabele 'error'
	4. Maak een nieuwe variabele, Kp, aan en sla de waarde 1 hierin op
	5. Bereken de output waarde en sla deze op in een nieuwe variabele 'output'
	6. Gebruik de output waarde om de motoren aan te sturen
	Nu worden alle bovenstaande stappen eenmalig uitgevoerd, maar dit moet eigenlijk vaker gebeuren.
	7. Gebruik een loop-structuur om alle bovenstaande stappen meerdere malen uit te voeren. Maak een weloverwogen keuze om de for- of while-loop structuur te gebruiken.


State machine
-------------

Robots werken in allerlei verschillende omstandigheden en omgevingen. De taken die een robot moet doen zijn aangepast aan deze omstandigheden, zodat hij zo goed mogelijk deze taken uit kan voeren. Dit kan worden gedaan door 1 'recht' pad aan taken te creeeren en deze achter elkaar uit te laten voeren. Dit kan het best worden uitgelegd aan de hand van een voorbeeld. Een veelgebruikte robot is een stofzuigrobot zoals hiernaast te zien. De robot moet op commando de kamer waarin die zich bevindt kunnen stofzuigen en zichzelf opladen wanneer nodig. De robot heeft dus eigenlijk verschillende subtaken: 'wachten', 'schoonmaken', 'opladen'. Het is ook handig als de robot kan gaan opladen als de batterij bijna leeg is tijdens het schoonmaken. Een extra subtaak 'terugrijden naar laadstation' kan dan worden toegevoegd. Deze subtaak moet soms wel en soms niet worden uitgevoerd: alleen als de batterij bijna leeg is, moet de robot terug naar zijn laadstation. Om de relatie tussen de verschillende subtaken weer te geven en te implementeren, gebruiken we een state machine.


*Add info graphic voor state machine voorbeeld*
Een state machine bestaat uit een aantal 'states' waarin een robot zich kan bevinden. Voor de stofzuigrobot die we hierboven hebben besproken, zijn dat de volgende states: 'wachten', 'schoonmaken', 'opladen' en 'terugrijden naar laadstation'.  De states worden weergegeven als cirkels, getiteld naar de state.
*Laat hier verschillende states zien*

Onder bepaalde condities kan een robot veranderen van state. Als de robot bijvoorbeeld in de state 'wachten' is en de opdracht krijgt om schoon te maken, gaat hij naar de state 'schoonmaken'. De hele state machine bestaat uit alle states waar een robot in kan zijn en alle mogelijke transities tussen de states. Transities worden aangegeven met pijlen, afhankelijk van welke kant de transitie mogelijk is. Bij de pijlen staat kort welke conditie nodig is om de transitie teweeg te brengen.


Let op! Als een state geen uitgaande pijl heeft, blijft de robot dus vastzitten in die state totdat die opnieuw wordt opgestart. In dit geval wordt daarom de 'schoonmaken' state weer terugverbonden met de 'wachten' staat.

Opdracht:
Teken op papier de state machine voor jouw robot. *geef ze 3 states die de robot in ieder geval moet hebben*

	1. Bepaal welke verschillende 'states' jouw robot moet hebben.
	2. Bepaal welke states transities moeten hebben naar welke andere states.
	3. Bepaal onder welke voorwaarden de transities tussen de verschillende states plaatsvinden.


Laat je getekende state machine checken door de docent voordat je verder gaat met de volgende opdracht!


Als we de in de vorige paragraaf getekende state machine willen implementeren in de software van de robot, werkt dat als volgt. Ten eerste willen we verschillend gedrag maken, afhankelijk van in welke 'state' de robot zich bevindt. We gebruiken dus een 'als/dan' structuur afhankelijk van welke state de robot heeft. In elke state komt het gedrag van die bepaalde state, zoals schoonmaken en opladen. Tot slot bevat elke state een conditie om over te gaan naar een andere state (zoals bij de pijltjes in de tekening). *voorbeeld code voor de voorbeeld state machine?*

Opdracht:

Implementeer de state machine in de software van de robot.

AI in robotica
--------------

Artificial Intelligence (kunstmatige intelligentie), of afgekort AI, speelt een steeds grotere rol in onze huidige samenleving. Algortimes die bepalen welke video jij hierna wilt kijken, welke post er bovenaan je feed staat, welke muziek je ook leuk kan vinden of wat je nog meer wilt weten na een bepaalde zoekopdracht, zijn allemaal een vorm van AI. Ook ChatGPT en Microsoft CoPilot zijn voorbeelden van AI waar je vragen aan kunt stellen en mee kunt communiceren. Deze AI kunnen ook kunnen ook afbeeldingen genereren aan de hand van een beschrijving.
Aangezien deze les te kort is om AI volledig uit te leggen en de materie daarnaast zeer complex, is het doel van deze les om je te leren wat een AI model in grote lijnen is en hoe dit in de praktijk werkt. Aanvullen/aanpassen

Een AI model wordt gemaakt door er heel veel bestaande informatie aan te geven, die het algoritme verwerkt en onthoudt.  Aan de hand van deze geleerde informatie kan de AI dan voorspellingen doen, problemen oplossen of video's aanbevelen.

Dit is duidelijker aan de hand van een voorbeeld. Elke dag kijken miljoenen mensen video's op YouTube. Iedereen heeft zijn eigen voorkeuren en dus 'kijkpatronen'. Door een AI al deze informatie te geven van wat mensen in het verleden hebben gekeken en welke video's ze achter elkaar keken, wordt een model gemaakt die kan voorspellen wat voor video iemand daarna wil kijken. Wat de AI dus eigenlijk doet is jouw kijkgedrag vergelijken met miljoenen andere mensen en uit de overeenkomsten met andere gebruikers voorspellen wat voor video's jij nog meer leuk vindt.

Het voeden van data aan de AI wordt ook wel 'trainen' genoemd: de AI wordt 'getraind' om bepaalde patronen te gaan herkennen of informatie op te slaan.

In de robotica wordt AI ook steeds meer gebruikt. AI modellen maken de robot nog slimmer en zo kunnen robots nog meer complexe taken uitvoeren. Zo wordt AI gebruikt om objecten, mensen of obstakels te herkennen, te leren van ervaringen en zich aan te passen aan nieuwe situaties.

Opdracht:

In deze les maken we een simpele AI die zelf kan bepalen of er een obstakel gedetecteerd wordt. Hiervoor gebruiken we data van de ultrasound sensor van de robot.

De AI is opgebouwd als een zogenoemd 'perceptron'. Deze perceptron bootst eigenlijk de vergelijking y = ax + b na. Hierbij is de 'x' de data die de perceptron binnenkomt, namelijk de data van de ultrasound sensor. De 'a' en de 'b' worden bepaald door het perceptron te trainen. Door te trainen op data waarvan wij weten of er wel of niet een object gezien is, wordt de correcte vergelijking y = ax + b gemaakt die bij deze situatie past. 
De output van de perceptron ('y'), is een floating point number.  Hieruit kunnen we niet opmaken of er een obstakel is gezien of niet. Om dit duidelijk te maken, maken we gebruik van de binaire getallen. (voeg een 'weet je nog' toe). Door het getal 0 ('false') te gebruiken voor de situatie dat er geen obstakel is gezien en het getal 1 ('true'), wanneer er wel een obstakel gedetecteerd is, kan deze distinctie wel worden gemaakt. 
Om als uiteindelijke output een 0 of een 1 te krijgen, wordt de 'y' uit de perceptron gebruikt. Als 'y' negatief is, is de uiteindelijke output 0 en als 'y' positief is, is de uiteindelijke output 1. Visueel ziet dat er als volgt uit: input delta function

Zoals al een aantal keer aangegeven, moet het algoritme getraind worden. We moeten het algoritme leren bij welke data een obstakel gedetecteerd wordt en bij welke data niet. Stel, we willen dat bij een afstand van 20cm een obstakel gedetecteerd wordt. Dan worden alle datapunten kleiner of gelijk aan 20 'gelabeld' als obstakel gedetecteerd, en dus met een 1. Alle datapunten groter dan 20 worden 'gelabeld' met een 0. voeg tabel toe.
Creeer aan de hand van bovenstaande tabel 2 variabelen, waarbij de waarde een lijst is met de data per rij van de tabel.

Het trainingsalgortime is al geconstrueerd, je hoeft deze code niet te begrijpen. Kopieer de onderstaande code in je Python script en roep de trainingsfunctie aan (maak gebruik van de lijsten die je in de vorige stap hebt gemaakt). Sla de weight en bias op in losse variabelen.

Nu kunnen we de weight en bias gebruiken in de perceptron. Roep de perceptron functie aan met argumenten de weight, bias en een datapunt tussen de 0 en 40 (probeer verschillende datapunten). Check hoe goed het algoritme nu kan aangeven of er een obstakel is (<= 20 moet 1 geven, > 20 0). Bedenk nu hoe je het algoritme meer accuraat zou kunnen maken. HINT: Bedenk op welke data het algoritme getraind is. Je kan proberen of jouw oplossing het algoritme beter werkt door stap .. aan te passen en daarna met de nieuwe weight en bias de datapunten te checken.

Je hebt nu zelf een AI gemaakt om obstakels te herkennen!




