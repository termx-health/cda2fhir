# Scripts for working with TermX and GitHub

### Structure
Explanaition of the content in the folder.

|- CDA \             # The CDA resources from https://registry.fhir.org/package/hl7.cda.uv.core|2.0.0-sd

### Download StructureDefinitions from TermX

~~~
python get-structure-definition.py
~~~ 
The **get-structure-definition.py** Python script:
- query data from https://termx.kodality.dev/api/structure-definitions. 
- Process results. 
- For every element in data array save the file with content from element "content", witn name from element "code" and extension from element "contentFormat".


