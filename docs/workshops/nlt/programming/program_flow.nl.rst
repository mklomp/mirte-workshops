Uitvoeringsvolgorde
--------------------

Maar het is nog lang niet makkelijk om een computer precies te vertellen wat deze moet doen. Een
computer heeft namelijk duidelijke instructies nodig. En deze instructies moeten elkaar goed
opvolgen. Dit heet ook wel de uitoeringsvolgorde (Engels: *flow*) van je programma. Dit kan
vervolgens goed weergegeven worden in een flowchart zoals hieronder.

.. d2::

    direction: right
    vars: {
      d2-config: {
        sketch: true
        theme-id: 8
      }
    }

    1: Pak twee boterhammen
    2: Leg kaas op één boterham
    3: Leg de andere boterham erop
    4: Doe de tosti in het tosti-ijzer
    5: Wacht tot de tosti klaar is
    6: Haal de tosti eruit

    1->2->3->4->5->6

.. note::

   Maar let op. Dit lijkt allemaal vrij duidelijk, maar dat komt vooral omdat wij mensen bij het 
   lezen van deze instructies erg veel aannames maken. Als je deze instructies echt heel precies
   gaat interpresteren kan het goed zijn dat er toch niet gebeurt wat jij wil. Een mooi en bekend 
   voorbeeld daarvan is de Exact Instruction Challenge.
   https://www.youtube.com/watch?v=FN2RM-CHkuI

In plaats van een tosti maken, kunnen we natuurlijk ook een robot een taak uit laten voeren.
Zo zouden we ook kunnen kijken hoe we de robot een vierkantje laten rijden.

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      .. d2::

          vars: {
            d2-config: {
              sketch: true
              theme-id: 8
            }
          }

          0: Start
          1: Rij 1s rechtdoor
          2: Draai links voor 1s
          3: Rij 1s rechtdoor
          4: Draai links voor 1s
          5: Rij 1s rechtdoor
          6: Draai links voor 1s
          7: Rij 1s rechtdoor
          8: Draai links voor 1s
          9: Stop

          0->1->2->3->4->5->6->7->8->9

   .. grid-item::

      .. code-block:: python

          from mirte_robot import robot
          mirte=robot.createRobot()

          mirte.drive('straight', 1)
          mirte.drive('left', 1)
          mirte.drive('straight', 1)
          mirte.drive('left', 1)
          mirte.drive('straight', 1)
          mirte.drive('left', 1)
          mirte.drive('straight', 1)
          mirte.drive('left', 1)




      


      .. code-block:: python

          from mirte_robot import robot
          mirte=robot.createRobot()

          for (i in range(4)):
            mirte.drive('straight', 1)
            mirte.drive('left', 1)


Veel voorkomende programmeerfouten
- syntax fouten
- niet alle condities in if/else
- overflow
- floating point