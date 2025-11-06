Programmeertalen
----------------

.. admonition:: info
   :class: margin

   Leer meer over hoe een computer werkt. :doc:`hoe werkt een computer <computers_explained>`

In de vorige sectie heb je geleerd hoe de basis van een computer werk. Je kan je voorstellen dat het programmeren
van een computer met alleen maar instructies aan de processor (assembly) erg ingewikkeld en niet intuitief is. Om dat op te
lossen zijn er programmeertalen ontwikkeld. Dit worden ook wel hoger-level (*higher-level*) programmeertalen genoemd. 
Voorbeelden hiervan zijn Fortran, C, C++ en Rust. Om van je code in een higher-level taal naar machinetaal (soms met assembly 
als tussenstap) te komen heb je een compiler nodig. Deze compiler vertaalt bijvoorbeeld de C-code naar assembly voor jouw 
specifieke processor/instructieset. Zodoende worden deze talen ook wel **compiled** talen genoemd.

.. d2::

    classes: {
      invisible: {style.opacity: 0}
    }

    vars: {
      d2-config: {
        sketch: true
        theme-id: 8
      }
    }

    compiletime: {
      grid-rows: 2
      grid-columns: 2
      source-code: |md source-code |
      dummy1.class: invisible
      int x = 42\; -> compiler
      # x = 42
      # dummy2.class: invisible
    }

    dummy: {
      grid-rows: 2
      dummy2.class: invisible
      start\nprogramma
    }
    dummy.class: invisible

    runtime: {
      grid-rows: 2
      grid-columns: 2
      dummy3.class: invisible
      source-code: |md machine-code |
      dummy4.class: invisible
      01011011
      # interpreter -> 10011101
    }

    compiletime.compiler -> dummy.start\nprogramma -> runtime.01011011
    # compiletime.x = 42 -> dummy.start\nprogramma -> runtime.interpreter


Dat betekent ook dat je code niet meteen naar de processor gestuurd wordt. De compiler maakt van je code een nieuw
bestandje (bijvoorbeeld .exe) die je vervolgens uit kan voeren. Op het moment dat je die uitvoert wordt de machinecode
naar de processor gestuurd en start je programma. Het compileren van je code kan bij grotere programmas erg lang
(soms wel tientallen minuten) duren.

.. figure:: https://imgs.xkcd.com/comics/compiling.png
    :alt: Code Compiling XKCD
    :width: 300
    :align: center

    CC-BY van xkcd.com door Randall Munroe

Maar niet elke programmeertaal gebruikt een compiler om tot machinecode te komen. Er zijn ook programmeertalen die direct
machinecode maken en deze meteen naar de processor sturen. Python, PHP en Javascript, zijn hier voorbeelden van.
Dit worden **interpreted** talen genoemd, maar je kan het ok hebben over **scripted** talen.

.. d2::

    classes: {
      invisible: {style.opacity: 0}
    }

    vars: {
      d2-config: {
        sketch: true
        theme-id: 8
      }
    }

    compiletime: {
      grid-rows: 2
      grid-columns: 2
      source-code: |md source-code |
      dummy1.class: invisible
      # int x = 42\; -> compiler
      x = 42
      dummy2.class: invisible
    }

    dummy: {
      grid-rows: 2
      dummy2.class: invisible
      start\nprogramma
    }
    dummy.class: invisible

    runtime: {
      grid-rows: 2
      grid-columns: 2
      dummy3.class: invisible
      source-code: |md machine-code |
      # dummy4.class: invisible
      # 01011011
      interpreter -> 10011101
    }

    # compiletime.compiler -> dummy.start\nprogramma -> runtime.01011011
    compiletime.x = 42 -> dummy.start\nprogramma -> runtime.interpreter

Het grootste verschil tussen compiled en interpreted talen is wanneer ze de source-code omzetten naar machinetaal.
Bij compiled talen gebeurt dit dus tijdens het ontwikkelprocess, terwijl dit bij script-talen juist tijdens het
uitvoeren van het programma gebeurt. Dit betekent ook dat je voor compiled talen het programma pas kan starten
nadat alles af (en gecompileerd) is. Script talen kan je regel voor regel direct uitvoeren. Hierdoor is het voor
het testen van een programma veel makkelijker om met scripttalen te werken. Wil je echter dat je programma sneller
kan draaien, dan is het handiger om naar een compiled taal over te gaan. Zodoende zie je ook wel vaker dat er eerst 
een prototype gemaakt wordt in een interpreted taal (zoals Python), en als er echt tijdskritische elementen in zitten
overgegaan wordt naar gecompileerde talen (zoals C).

