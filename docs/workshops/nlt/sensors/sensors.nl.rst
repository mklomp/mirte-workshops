:orphan:

Sensoren
########################

Wat zijn sensoren en waarom zijn ze belangrijk in de robotica?
--------------------------------------------------------------

Om een robot taken uit te laten voeren, is het belangrijk dat deze interactie kan hebben met de omgeving. Zo kan de robot bijvoorbeeld weten waar hij is in een bepaalde ruimte, weten waar een pakketje staat wat hij op moet tillen of mensen herkennen die door de ruimte heen bewegen. 

Dit wordt gedaan door de robot sensoren te geven. De robot krijgt via de sensoren informatie over de omgeving, verwerkt deze informatie en doet dan een actie. Bijvoorbeeld: De robot meet de afstand tot een object en krijgt via de sensor de waarde 20cm binnen. Het doel is om op 10cm van het object te stoppen, dus de actie die de robot gaat doen is de motoren laten draaien om naar voren te rijden. 
Als de afstand kleiner was geweest dan 10cm, bijvoorbeeld 8cm, dan had de robot als actie de motoren laten draaien om naar achteren te rijden.

Wat voor sensoren heeft een robot nodig?
----------------------------------------

Er bestaan enrom veel verschillende sensoren, met elk een eigen functie. Om te bepalen wat voor sensoren een robot nodig heeft, moet worden bepaald wat de taak is van de robot en in wat voor omgeving de robot opereert. Een robot die objecten in een fabriek op een lopende band moet plaatsen heeft namelijk andere sensoren nodig dan een robot die in een ziekenhuis pakketjes rond moet brengen.

Opdracht: *scenario en wat voor soort sensoren zijn daarvoor nodig*
Om te opereren in een bepaalde omgeving, is het handig als robots de mogelijkheid hebben om obstakels te detecteren. Dit kan voorkomen dat een robot hard tegen iets aan botst én geeft de robot de mogelijkheid om van richting te veranderen en het obstakel te ontwijken.

Schakelaar sensor *andere naam?*
--------------------------------

De meest eenvoudige manier om een obstakel in de omgeving waar te nemen is door gebruik te maken  van een schakelaar sensor. Dit soort schakelaren kunnen op de voorkant van de robot worden geplaatst om obstakels aan de voorkant van de robot te detecteren. De schakelaar is onderdeel van een stroomcircuit. Als de robot vrij rondrijdt is het circuit onderbroken en loopt er geen stroom doorheen. Wanneer de robot ergens tegenaan rijdt, wordt de sensor ingedrukt en het circuit gesloten. De robot weet nu dat hij ergens tegenaan is gereden en kan afhankelijk hiervan beslissen om een andere richting op te rijden en het object in het vervolg te ontwijken.

Lichtsensor
-----------

Handiger is om het obstakel al te kunnen waarnemen voordat de robot daadwerkelijk ertegenaan botst. Hiervoor kunnen we gebruikmaken van een lichtsensor *IR? Ff testen hoe dit werkt met IR en de licht modus van de kleurensensor van lego.* Deze sensor bestaat uit twee delen: een zender en een ontvanger. De zender zendt licht uit, en de ontvanger vangt dit licht wel of niet op, afhankelijk van de situatie. Als er een object voor de robot staat, zal het uitgezonden licht reflecteren op het object en terug bewegen richting de sensor:  de ontvanger zal dit licht opvangen. Als er geen object voor de robot staat, is er geen oppervlak waar het licht op kan reflecteren en gaat het dus rechtdoor: de ontvanger vangt nu niks op. Hierdoor kan op afstand worden gedetecteerd worden of er een object voor de robot staat. Nu kan de robot, voordat hij ertegenaan botst, een andere kant op sturen.

*Maak hiertussen een praktische opdracht om de robot van A naar B te laten rijden door obstakels op de juiste manier neer te zetten/voor de robot te bewegen.*

Lijnvolgsensor
--------------

Door obstakels slim te plaatsen, kan de robot van A naar B rijden. Dit is in de praktijk echter niet heel praktisch om te realiseren. Als het doel is dat de robot precies een bepaalde route rijdt van punt A naar punt B, kan beter gebruikt gemaakt worden van een lijn en een 'lijnvolgsensor'. Een zwarte lijn op een witte achtergrond kan worden gebruikt om een bepaald parcours voor de robot aan te geven. 
De lijnvolgsensor is een infrarood licht sensor, met een zender en een ontvanger. *licht? Ff testen hoe dit werkt met IR en de licht modus van de kleurensensor van lego*
De IR sensor stuurt infrarood straling uit met een infrarood zender, en vangt deze straling op met een infrarood ontvanger. Net zoals zichtbaar licht, heeft de kleur van het oppervlak invloed op hoeveel licht er geabsorbeerd en weerkaatst wordt. *Klopt de bewoording?*
De zwarte lijn absorbeert de infrarode straling, waardoor de IR ontvanger geen IR straling ontvangt: de sensor geeft een hoge waarde terug. 
De witte ondergrond naast de lijn reflecteert de infrarode straling, die wordt opgevangen door de IR ontvanger: de sensor geeft een lage waarde terug.
De precieze waarde die de sensor terug geeft is niet te voorspellen, dit hangt af van hoeveel IR licht er in de omgeving is (bijvoorbeeld van de zon) en hoe absorberend/reflecterend het zwart en wit van het papier zijn.
Door nu logica in te bouwen om de robot te sturen afhankelijk van of de sensor zwart of wit meet, kunnen we de robot over de lijn laten rijden.

Sonar
-----

In sommige gevallen kan het handig zijn om de precieze afstand tot een obstakel weten. Hiermee kan de robot inschatten hoeveel vooruit hij nog kan rijden, of een bepaald obstakel met een grijper oppakken. Voor deze taak kan een ultrasoon sensor worden gebruikt.  Ultrasone golven zijn geluidsgolven met een hogere frequentie dan wat wij mensen kunnen horen. De ultrasoon sensor stuurt ultrasone golven uit met een ultrasoon zender en vangt deze golven op met een ultrasoon ontvanger. Door de tijd te meten die de golven erover doen om na uitzenden weer te worden ontvangen, kan worden uitgerekend hoe ver het object van de sensor af staat. 


Let op! Als het object van een materiaal is gemaakt dat geluidsgolven absorbeert, zal de ontvanger van de sensor geen golven ontvangen. Hierdoor is het object niet detecteerbaar door de sensor en lijkt het voor de robot alsof er geen object staat.

Opdracht: Bereken de snelheid die het geluid aflegt met object op bepaalde afstand van de sensor *dit moet ongeveer de geluidssnelheid zijn*
Opdracht: Voor de materialen plastic, hout, aluminium/spiegel en glas *misschien nog iets met kleur*: test de IR en sonar met deze materialen en volg hierbij de Scientific Approach.

Kleursensor
-----------

Het volgen van de lijn met de lijnvolgsensor kan alleen als de lijn continue is en niet al te scherpe hoeken maakt. Splitsingen kunnen met deze sensor niet worden gedetecteerd en de robot kan niet bepalen welke kant hij op moet. Door splitsingen gekleurde markers te geven, kan de robot zo geprogrammeerd worden dat hij afhankelijk van de marker een bepaalde kant op rijdt. Om de markers te detecteren, kan gebruik gemaakt worden van een kleurensensor. Deze sensor zendt wit licht uit, wat reflecteert op het oppervlak. Het gereflecteerde licht wordt vervolgens weer door de sensor opgevangen, die de golflengtes van het opgevangen licht bepaalt. Dit wordt uitgedrukt in een R, G en B waarde, die de kleur van het oppervlak representeren. 
