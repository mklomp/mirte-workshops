:orphan:

Lijn volgen
################################

.. article-info::
    :author: :fa:`brain` Programmeren
    :read-time: 30 min

1
---

Je hebt nu een goed beeld wat de robot allemaal kan. In de komende workshops zal 
je op verschillende manieren een lijn gaan volgen. Dit werkt toe naar deelname aan 
de RoboCupJunior Redden wedstrijd. In de eerste lijn volg workshop zullen we de 
lijn gaan volgen met slechts 1 sensor.


2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      In workshop ‘licht meten’ heb je geleerd wanneer je sensor een zwarte lijn
      ziet en wanneer niet. Deze waardes kan je gebruiken om te bepalen wat de robot
      moet gaan doen. Om met 1 sensor op de lijn te blijven moet je een programma
      (ook wel algoritme genoemd) maken dat zorgt dat de robot dit gaat doen.

      Dit programma kan je op verschillende manieren maken. Het kan helpen om naar 
      het plaatje hiernaast te kijken. Wat moet de robot doen als de robot zwart ziet?
      En wat moet de robot doen als de robot wit ziet? Je kan hiervoor dus ook
      de functies gebruiken die je in de vorige workshop gebruikt hebt.

      Omdat we maar 1 sensor hebben, gaan we eigenlijk het linker of rechterdeel
      van de lijn volgen. Je bent dus vooral aan het kijken of je op de lijn zit 
      of niet. Het voorbeeld in het plaatje volgt dus de rechterkant van de lijn.

   .. grid-item::

      .. image:: _media/mirte_line_1_sensor_theory.png
         :width: 350
         :alt: Mirte sensor on a line


.. dropdown:: :fa:`question-circle` Help

   - Ik snap niet wat ik moet doen:
      - Je computerprogramma kan bijvoorbeeld iets zijn als: als ik zwart zie draai ik
        ik naar links en als ik wit die draai ik naar rechts.
   - Hoe kan ik goed bepalen welke waarde ik moet nemen:
      - Je wilt graag dat je robot zo goed mogelijk het verschil tussen wit en zwart
        ziet. Als je een waarde voor zwart hebt gemeten en een waarde voor wit, kan je
        dus het beste precies tussen die twee waardes in gaan zitten.
   - De robot wertke gisteren/daarnet goed, maar nu niet meer. En ik heb niets veranderd:
      - Zoals uitgelegd meet de sensor de waarde van het papier. Maar als je dit in een
        donkere ruimte doet zullen de waardes anders zijn dan wanneer je dit in een lichte
        ruimte doet. Probeer dus dat het licht hetzelfde blijft (doe bv de gordijnen dicht).


