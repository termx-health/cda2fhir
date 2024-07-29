# Scripts for working with TermX and GitHub

### Structure
Explanaition of the content in the folder.

|- CDA-2.0-classes \             # The CDA resources from https://registry.fhir.org/package/hl7.cda.uv.core|2.0.0-sd
|- used-cda-models \             # The CDA classes used in the TermX (limited set downloaded with _get-structure-definition.py_)

### Download StructureDefinitions from TermX

~~~
python get-structure-definition.py
~~~ 
The _get-structure-definition.py_ Python script:
- query data from https://termx.kodality.dev/api/structure-definitions. 
- Process results. 
- For every element in data array save the file with content from element "content", witn name from element "code" and extension from element "contentFormat".

### Download StructureMaps from TermX

~~~
python get-structure-map.py
~~~ 
The _get-structure-map.py_ Python script:
- query data from https://termx.kodality.dev/api/transformation-definitions. 
- Process results. 
- For every transformation in data array queries detailed information  https://termx.kodality.dev/api/transformation-definitions/$id
- Save three the files: 1) mapping; 2) related resources; and 3) example.
