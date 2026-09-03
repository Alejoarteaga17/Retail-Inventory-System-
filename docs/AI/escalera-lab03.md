# Escalera - Laboratorio

### Prompt 1

Haz el endpoint de inventario de productos

### Prompt 2

Nosotros queremos hacer un "reail inventory-system" nuestro objetivo actual es crear el endoint para el sistema con FastAPI con una data_mock basada en la informacion de docs y esto va a ir en el /src folder y ya tu te enfocas con las mejores prácticas y principios de software como sepraarlos correctametne

### Prompt 3

Nosotros queremos hacer un "reail inventory-system" nuestro objetivo actual es crear el endoint para el sistema con FastAPI con una data_mock basada en la informacion de docs y esto va a ir en el /src folder y ya tu te enfocas con las mejores prácticas y principios de software como sepraarlos correctametne.

Por favor actua como un ingenierio de software senior y utiliza estos requisitos para crear el codigo:

- The system shall allow users to create, update, view, and deactivate inventory items.
- The system shall maintain an item catalog containing, at minimum, an item identifier, name, current quantity, and reorder threshold.
- The system shall display the current inventory quantity for each item.
- The system shall validate all required input fields before processing inventory item requests.
Para el formato de los archivos por favor utiliza clean code practices, y el formato de industria de python.

### Prompt 4

Nosotros queremos hacer un "reail inventory-system" nuestro objetivo actual es crear el endoint para el sistema con FastAPI con una data_mock basada en la informacion de docs y esto va a ir en el /src folder y ya tu te enfocas con las mejores prácticas y principios de software como sepraarlos correctametne.

Por favor actua como un ingenierio de software senior y utiliza estos requisitos para crear el codigo:

- The system shall allow users to create, update, view, and deactivate inventory items.
- The system shall maintain an item catalog containing, at minimum, an item identifier, name, current quantity, and reorder threshold.
- The system shall display the current inventory quantity for each item.
- The system shall validate all required input fields before processing inventory item requests.
Para el formato de los archivos por favor utiliza clean code practices, y el formato de industria de python.

Ahora utiliza como contexto los archivos dentro: @src/data y @src/service

## Calificaciones

Prompt 1: 5/8
Prompt 2: 5/8
Prompt 3: 7/8
Prompt 4: 8/8

## Alucinaciones

Prompt 1: 5
Prompt 2: 3
Prompt 3: 2
Prompt 4: 1

## Conclusión

Los resultados evidencian una correlación clara entre la especificidad del prompt y la calidad del código generado. En el Prompt 1, una instrucción vaga como "haz el endpoint de inventario de productos" dejó al modelo sin contexto sobre el stack tecnológico, la estructura del proyecto o los requisitos funcionales, lo cual se tradujo en una calificación baja (5/8) y el mayor número de alucinaciones (5), producto de que el modelo tuvo que inventar supuestos sobre framework, esquema de datos y organización de carpetas. El Prompt 2 mejoró ligeramente al introducir el stack (FastAPI), la ubicación del código (/src) y la exigencia de buenas prácticas, pero mantuvo la misma calificación y aún generó alucinaciones porque seguía faltando una definición precisa de los requisitos funcionales y el formato esperado de los datos mock.

El salto más significativo ocurre entre el Prompt 2 y el Prompt 3, donde la incorporación de un rol explícito ("ingeniero de software senior"), una lista de requisitos funcionales concretos (RF en formato "shall") y una indicación de estándar de formato (clean code, PEP8) elevó la calificación a 7/8 y redujo las alucinaciones a 2, mostrando que estructurar el prompt como una especificación técnica reduce drásticamente el espacio de ambigüedad que el modelo debe rellenar por su cuenta. Finalmente, el Prompt 4 alcanzó el máximo (8/8) con solo 1 alucinación al añadir contexto de archivos existentes (@src/data y @src/service), lo que confirma que anclar la generación a artefactos reales del proyecto —en lugar de dejar que el modelo infiera la arquitectura— es el factor decisivo para minimizar errores. En conjunto, el experimento demuestra que la ingeniería de prompts efectiva combina tres elementos: rol/persona, requisitos explícitos y verificables, y contexto real del código existente, y que omitir cualquiera de estos incrementa tanto la probabilidad de alucinación como la necesidad de retrabajo posterior.
