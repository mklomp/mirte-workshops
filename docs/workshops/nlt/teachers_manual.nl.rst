Docenten Handleiding
====================

Sciencitif Approach

Sensoren naar achteren



CH Sensoren
===========

We hebben er voor gekozen om in deze module een overzicht te geven van de verschillende sensoren
die vaak binnen robotica gebruikt worden. Bovendien hebben we de werking van twee sensoren
uitgelegd. Dit zijn de lijvolgsensor (licht) en de afstandssensor (geluid). Hiermee kunnen we goed
de basis uitleggen.

CH Programming
==============

Functies:

Waar we het hebben over functies, zouden we het eigenlijk moeten hebben over routines. Een routine is
een modulair stukje code wat je vanaf ander plekken aan kan roepen. Dat is vrij algemeen. Er zijn vervolgens
twee smaakjes:

- procedure: Een stukje code dat iets uitvoert (eventueel op basis van input), maar geen output
  (returnwaarde) heeft.
- functie: Een stukje code dat iets uitvoert, en ook een (return)waarde teruggeeft. 

.. d2::

    classes: {
      invisible: {
        style.opacity: 0
        label: ""
        width: 1
        height: 1
      }
    }

    routine: {
      grid-rows: 2
      grid-columns: 3

      dummy1.class: invisible
      procedure
      dummy2.class: invisible
      dummy3.class: invisible
      functie
      dummy4.class: invisible

      dummy1 -> procedure
      dummy3 -> functie -> dummy4
    }

Als een functie altijd dezelfde output geeft op basis van dezelfde input (dus niets globaal verandert) noem
je dit ook wel een pure functie en is dus te vergelijken met een wiskundige functie. 

Binnen deze module willen we dit onderscheid echter nog niet meegeven en zijn wij van mening dat de 
term functie voor de leerlingen herkenbaarder is dan routine.

Diagrams:

Hier hebben we gekozen om flowcarts te gebruiken ipv UML/SysML activity diagrams. Mochten leerlingen
een meer formele manier willen om hun programma te beschrijven (bv ook dmv concurrency), dan kunnen
zij kijken naar activity diagrams.

Typen programmeren:

Binnen programmeren heb je een aantal prgrammeer paradigmas:

- Procedural: 
- Functional: Zoveel mogelijk gebruik makend van pure functies (zie hierboven). Wordt snel gebruikt
  als je meer wiskundige software schrijft (bv sensor fusion, path planning, etc).
- Even driven: Reageert op events, die functie-callbacks aanroepen. Een event zou bijvoorbeeld
  een wijziging van een sensorwaarde kunnen zijn.
- Object oriented: Alles wordt als object weergegeven. Denk bjivoorbeeld aan een Arm-, Sensor-, 
  of Controller-object.

Onze insteek is om in de introductie voor programmeren bij het procedurele te blijven. Uiteraard
kunnen leerlingen ook functies maken, maar dat is wat anders dan functioneel programmeren.

Vervolgens willen we in het hoofdstuk 'Algoritmes' een event driven aanpak bespreken (dmv 
state-mahcines). De manier van programmeren blijft echter procedureel.