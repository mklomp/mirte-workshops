:orphan:

Hoe werkt een computer?
-----------------------

De computer ken je natuurlijk wel van je latop, of je telefoon. Maar tegenwoorig zitten er in bijna
alle machines wel kleine computers. Of dit nou een wasmachine is, of een koffiezetapparaat. allemaal
hebben ze een kleine computer om de machine aan te sturen. Maar hoe weet die computer nou wat hij
moet doen?

Een computer bestaat grofweg uit twee elementen: de processor en het geheugen. De processor is een chip in je computer die instructies
uit kan voeren. Dit kan bijvoorbeeld het optellen van 2 getallen zijn. Bij meer gespeciaseerde prossesoren
(zoals een GPU) kunnen dit veel complexere berekeningne zijn die speciaal voor dat geval nuttig
zijn. Denk bijvoorbeeld aan matrixberekeningen voor een GPU. Een processor word zo ontworpen dat hij een aantal
berekening (ook wel instructies genoemd) kan uitvoeren. De hele lijst noem je ook wel de instructieset van
de processor.

.. d2::

    direction: right
    vars: {
      d2-config: {
        sketch: true
        theme-id: 8
      }
    }

    computer: {
      processor
      geheugen
    }

    toesenboard\nmuis\nsensoren -> computer: input
    computer -> scherm\nactuatoren: output

Door een heleboel van deze instrcuties uit te voeren kan je een complex programma maken. Stel je voor dat je een 
processor hebt die op drie pins een instructie kan krijgen en de volgende 5 instructies
uit kan voeren:

+------------+--------+------------------------------------------+
| Instructie | Binair | Uitleg                                   |
+============+========+==========================================+
| STORE X Y  | 01     | Sla getal X op in het geheugen plek Y    |
+------------+--------+------------------------------------------+
| ADD X Y    | 10     | Tel getal X bij getal Y op (in register) |
+------------+--------+------------------------------------------+
| JUMP X     | 11     | Spring naar regel X                      |
+------------+--------+------------------------------------------+

Het gehegen van een computer bestaat uit een hele lange lijst bits achter elkaar. Om hier een
beetje orde in te houden wordt dit opgedeeld in adressen van een bepaalde lengte. Zo heb je allemaal
vakjes in het geheugen die allemaal een waarde kunnen representeren. Computers die op deze
manier (processor en geheugen) zijn opgebouwd noemt met ook wel Von Neumann architeruur.


Voorbeeld
----------

Met de 3 instructies van hierboven kunnen we al een klein programmatje maken. In de tabel
hieronder zie je per regel een instructie en wat dat met het geheugen doet. Verder zie
je een computer met 3 gehegen plekken. De eerste moenem we even REG (van register). Daar
komen alle antwoorden van de ADD te staan. Verder hebben we nog 2 gehegenvakjes in RAM.
Je ziet dat dit simpele programmatje de zogenoemde fibonacci reeks bekerkend.

+--------+------------+-----------------------+
|        | Instructie |        Geheugen       |
+--------+------------+-------+-------+-------+
| Regel  |            |  REG  | RAM 0 | RAM 1 |  
+========+============+=======+=======+=======+
| 1      | STORE 2 0  |       | **2** |       |
+--------+------------+-------+-------+-------+
| 2      | STORE 3 1  |       |   2   | **3** |
+--------+------------+-------+-------+-------+
| 3      | ADD 0 1    | **5** |   2   |   3   |
+--------+------------+-------+-------+-------+
| 4      | STORE A 1  |   5   | **5** |   3   |
+--------+------------+-------+-------+-------+
| 5      | ADD 0 1    | **8** |   5   |   3   |
+--------+------------+-------+-------+-------+
| 6      | STORE A 2  |   8   |   5   |   8   |
+--------+------------+-------+-------+-------+
| 7      | JUMP 3     |   8   |   5   |   8   |
+--------+------------+-------+-------+-------+

De instructieset is dus afhankelijk van de procerssor. Wat je er vervolgens mee 
wil gaan doen is aan degene die eenprogramma hiervoor schijft. De processor is 
de kok. De instructieset zijn alle ingredienten en apparaten die de kok tot zijn 
beschikking heeft. En jij schrijft een recept op wat je wil dat de kok kan maken. Een
programma wat geschreven is in regels instructies heet Assembly.
Of misschien analogie met:

componist - programmeur (bedenker)
bladmuziek - code (taal die orkest bergijpt)
orkest - cpu (uitvoerder)

(compiler)
assembly -> machinecode -> cpu


EXTRA

Processortype     Applicatie                              Architectuur (intructiesets)
CPU               Generiek (bv computer, telefoon)        x84, ARM, RISC-V
GPU               Grafische kaart (bv )                   GCN, CUDA, PTX
NPU               Neurale Netwerken (gezichts herkenning)
ASIC              Specifiek ontworpen (bv crypto minen)   Eigen ontwerp
FPGA              Flexibel                                Moet je helemaal zelf maken

MCU (CPU + RAM)
SoC (CPU + GPU)

Eigenschappen van een processor: aantal bits, kloksnelheid, architectuur

Dit voorbeeld kan je ook in gobalt.org zien. Daar kan je ook kijken hoe andere programmeertalen en compilers de koppeling 
maken naar assembly. Over het algemeen geldt: hoe minder regels je assembly heeft, hoe sneller je programma is. Wat je ook 
ziet is dat er niet altijd dezelfde soort instructies uit komen. Als je bijvoordbeeld, Python of Javascript aanklikt
zal je zien dat er een heel ander soort instrcuties komt te staan. Dat is nog niet iets wat de procesor direct begrijpt.


Welke waarde staat er in RAM1 tijdens regel 1? 
Dat is ongedefinieerd. Dat verschilt per procerssor, operating system, compiler.
Soms wordt dit bij initializatie op 0 gezet, maar vaak wordt hier ook niets mee gedaan en kan dit dus een waarde zijn die een
vorig programma er in heeft gezet. 

Een CPU is bv 32 of 64 bits. Wat betekent dat?
Dit is de grootte van het getal waar de processor berekeningen mee kan maken. Bij een 32 bits processor kan deze dus getallen
optellen tot 32 bits grootte (2^32 ~= 4.3 miljard). Bij een 64 bits processir is dit dus vele malen groter.

Waar staat de code die je gemaakt hebt? Is dat op de processor, of in het geheugen?
De code zelf staat meestal op de harde schijf. Dat is uit eindelijk geheugen.

Kan je nu alles programmeren wat je maar wil?
Met de 3 instructies uit het voobeeld kan je niet elk programma maken wat je wil. Daar heb je nog meer instructies voor nodig.
Standaard processoren hebben een instructieset die dat wel kan. Zo een set noem je Turing complete. Het kan dan wel zijn 
dat je veel tijd en/of veel geheugen nodig hebt.
