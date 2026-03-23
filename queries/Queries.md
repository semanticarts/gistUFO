# Queries Directory

This directory is a place to store queries used for inference and validation. The validation directory contains three subdirectories:
- antipattern_detection, used to check for antipatterns defined in Tiago Prince Sales' thesis [Ontology Validation for Managers](https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/ontology_validation_for_managers_2014.pdf)
- stereotype_validation, used to ensure that classes mapped to OntoUML stereotypes conform to their associated constraints, based on the [OntoUML documentation](https://ontouml.readthedocs.io/en/latest/classes/index.html) and [Giancarlo Guizzardi's thesis](https://www.researchgate.net/publication/215697579_Ontological_Foundations_for_Structural_Conceptual_Models).
- mapping_checks, used to find errors in ontologies that have been mapped to [gUFO](https://nemo-ufes.github.io/gufo/) 

## Notes

All queries have been adopted for use with gUFO and gist, meaning that some OntoUML sterotypes present in the original definitions of some constraints have been removed. In particular, the OntoUML concepts of Collective, Quantity, Relator, Mode, and Quality are not used in these queries, as they are not mapped to the Types hierarchy in gUFO. 

As gist and gUFO predicates have yet to be mapped to one another, several queries use gist predicates with similar meanings to the original gUFO counterparts. 

Annotations/definitions for queries are from the [OntoUML documentation](https://ontouml.readthedocs.io/en/latest/index.html). 

The sortal and endurant constraints have been pulled from the [nemo-ufes ufo-types repository](https://github.com/nemo-ufes/ufo-types/blob/master/models/sparql-queries.rq) and reformatted. 

While some antipatterns ought to be avoided, some are closer to guidelines than requirements. It is recommended that modelers take a look at the definitions of each antipattern before deciding whether or not to use their corresponding queries. 

The antipatterns BinOver, ImpAbs, MixIden, PartOver, RelComp, RelOver, RelSpec, RepRel, UndefFormal, UndefPhase and WholeOver have been determined to not be of immediate relevance to our work and have not been implemented at this time. 

