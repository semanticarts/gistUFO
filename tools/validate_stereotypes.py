import os
from rdflib import Namespace, URIRef, Literal
from rdflib.graph import Graph, ConjunctiveGraph, Dataset
from rdflib.namespace import NamespaceManager, RDF, RDFS, XSD, SKOS, OWL

gist = Namespace("https://w3id.org/semanticarts/ns/ontology/gist/")
owl = Namespace("http://www.w3.org/2002/07/owl#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
sh = Namespace("http://www.w3.org/ns/shacl#")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
saox = Namespace("https://taxonomies.semanticarts.com/SemArts/")
gistx = Namespace("https://w3id.org/semanticarts/ns/ontology/gistx/")

DEBUG = True

initial_mapping = Graph()
initial_mapping.bind("gist", gist)
initial_mapping.bind("owl", owl)
initial_mapping.bind("rdf", rdf)
initial_mapping.bind("rdfs", rdfs)
initial_mapping.bind("sh", sh)
initial_mapping.bind("skos", skos)
initial_mapping.bind("xsd", xsd)
initial_mapping.bind("saox", saox)
initial_mapping.bind("gistx", gistx)
initial_mapping.parse("./ontologies/gistToGufoTypes.ttl")
initial_mapping.parse("./ontologies/gistToGufoIndividuals.ttl")
initial_mapping.parse("./ontologies/gistCore14.0.0/gistCore14.0.0.ttl")
initial_mapping.parse("./ontologies/gistCore14.0.0/gistSubClassAssertions14.0.0.ttl")
initial_mapping.parse("./ontologies/gUFO1.0.0/gUFO1.0.0.ttl")

gistUFO = Graph()
gistUFO.bind("gist", gist)
gistUFO.bind("owl", owl)
gistUFO.bind("rdf", rdf)
gistUFO.bind("rdfs", rdfs)
gistUFO.bind("sh", sh)
gistUFO.bind("skos", skos)
gistUFO.bind("xsd", xsd)
gistUFO.bind("saox", saox)
gistUFO.bind("gistx", gistx)
gistUFO.parse("./ontologies/gistUFO.ttl")
gistUFO.parse("./ontologies/gistCore14.0.0/gistCore14.0.0.ttl")
gistUFO.parse("./ontologies/gistCore14.0.0/gistSubClassAssertions14.0.0.ttl")
gistUFO.parse("./ontologies/gUFO1.0.0/gUFO1.0.0.ttl")


def run_query_set(query_directory, query_kind):
    print(f"Running {query_kind} queries...")
    violation_count = 0
    violation_dict = {}
    for i in os.listdir(f"./queries/validation/{query_directory}"):
        if DEBUG:
            print(f"Running {i}")

        with open(f"./queries/validation/{query_directory}/" + i) as query_file:
            query = query_file.read()
            results = initial_mapping.query(query)
            violation_count += len(results)
            if DEBUG:
                print(f"-Initial mapping: Found {len(results)} violations.")
            if len(results) > 0:
                violation_dict[i] = results
                
            results2 = gistUFO.query(query)
            violation_count += len(results2)
            if DEBUG:
                print(f"-gistUFO: Found {len(results2)} violations.")
            if len(results2) > 0:
                violation_dict[i] = results2

    print(f"Found {violation_count} {query_kind} violations total.")
    for k, v in violation_dict.items():
        print(f"Violations in {k}:")
        for row in v:
            print(f"{row.invalid_class} due to: {row.error_msg}")
    
# If this is every made into a command line tool, probably just have a few query kind options and alter main to just run the specified kind
def main():
    run_query_set("stereotype_validation", "Stereotype")
    run_query_set("antipattern_detection", "Anti-Patterns")
    run_query_set("mapping_checks", "Mapping Checks")

if __name__ == "__main__": 
    main()
    