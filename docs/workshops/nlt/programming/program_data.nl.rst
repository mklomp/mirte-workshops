Gegevens en variabelen
----------------------

Variablene. En voorbeeld met doosjes.


Na de vorige secties weet je dat een computer bestaat uit een processor en geheugen, en weet je hoe deze samenwerken.
Om te programmeren, moet je ook nog weten hoe je deze twee kan aansturen zodat de computer doet wat jij wil. Je zal de
computer namelijk stap voor stap moeten vertellen wat deze moet gaan doen. Om dit te doen zijn er verschillende
programmeertalen die allemaal hun eigen syntax hebben.

Datatypes: Hoe moeten de 0-en 1-en in het geheugen gerepresenteerd worden?
Flow: Wat is de volgorde van de taken die de computer moet uitvoeren.

Zoals je weet bestaat het geheugen van een computer alleen maar uit 0-en en 1-en. Dat programmeert alleen wel erg lastig.
Om dit makkelijker te maken heeft elke programmeertaal zijn eigen datatypes/datastrcuturen zodat het weet hoe deze bits
geinterpreteerd moeten worden. Ondanks dat elke programmeertaal zijn eigen types heeft, hebben de meeste programmeertalen
in de basis wel dezelfde smaakjes:

+----------+----------------------+-----------+
| Datatype | Representeert        | Voorbeeld |
+==========+======================+===========+
| boolean  | waar/niet waar       | True      |
+----------+----------------------+-----------+
| integer  | gehele getallen      | 42        |
+----------+----------------------+-----------+
| float    | niet gehele getallen | 3.1415    |
+----------+----------------------+-----------+
| string   | zinnen               | "Hallo"   |
+----------+----------------------+-----------+

Hiermee kan je dus makkelijker tegen de computer zeggen hoe je wil dat die bits gebruikt moeten worden. Dit maakt het
voor jou als programmeur makkelijker om te begrijpen wat de computer doet. Uitendelijk hangt het dus van de interpreatatie
van de bits af welke waarde de bits representeren:

+----------+-----------------------------------------+
|          |         geinterpreteerd als...          |
+----------+---------+----------------------+--------+
| bits     | integer | float                | string |
+==========+=========+======================+========+
| 01001100 | 77      | 8.22752278660603e+62 | M      |
+----------+---------+----------------------+--------+


OPDRACHT:
Ga na de python omgeving van de MIRTE robot (of gebruik een online versie van python, bv. https://pythononline.net/).
Probeer hier maar eens de volgende commandos:

.. code-block:: python

    42 + 42
    True + 42
    True + 0.2
    42 + 0.1
    "Hallo" + 42
    "Hallo" + " MIRTE"

In Python kijkt het programma zelf welk datatype je waarschijnlijk bedoelt. Hierdoor kan je dus ongestraft floats
bij integers optellen. Of dus zelfs booleans (0 of 1) bij een integer of float. Dit lijkt handig, maar kan natuurlijk
ook snel voor ongeplande fouten leiden. Om dit te voorkomen zijn er ook talen die *typed* zijn. Daar moet je dus 
altijd zeggen hoe de programmeertaal de waarde moet interpreteren. Zo moet je in C/C++ expliciet aangeven welk type 
je variabele is:

.. code-block:: c++

   int x = 42;

Zoals je zag kan Python ook niet standaard een string ("Hallo") bij een integer (42) optellen. Wat zou dat ook moeten
worden? Als je toch wil dat dit gebeurt, moet je dat (net zoals in *typed* talen) expliciet maken en de computer
vertellen dat je dit type om wil zetten (Engels: *type casten*).

.. code-block:: python

  "Hallo" + str(42)

Hierdoor kunnen we dus wel getallen bij zinnen "optellen". voor een computer blijft het echter heel moeilijk om
niet gehele getallen (*floats*) bij elkaar op te tellen. Dit heeft er mee te maken dat een computer natuurlijk
niet zo maar alle niet gehele getallen met alleen 0-en en 1-en weer kan geven. Hierdoor blijft de represantatie
van een niet geheel getal altijd een benadering!

OPDRACHT:

Probeer de volgende commando's:

.. code-block:: python

    0.1 + 0.2
    0.1 + 0.2 == 0.3

Ondanks dat we altijd zeggen dat een computer goed kan rekenen, kan deze dus eigenlijk helemaal niet goed met
niet gehele getallen overweg. Hier moet je dus altijd extra voorzichtig zijn! 

<voorbeel van 1991 Patriot Missile failure in Dhahran (Gulf War)>

Maar met alleen de data hebben we nog geen programma. Een programma moet ook een bepaalde volgorde van taken hebben.
Simpele programma's zijn vaak goed weer te geven middels een flowchart.
