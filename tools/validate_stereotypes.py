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

DEBUG = False

g = Graph()

g.bind("gist", gist)
g.bind("owl", owl)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("sh", sh)
g.bind("skos", skos)
g.bind("xsd", xsd)
g.bind("saox", saox)
g.bind("gistx", gistx)

g.parse("../ontologies/gistUFO.ttl")

def main():
    print("Running validation queries...")
    violation_count = 0
    violation_dict = {}
    for i in os.listdir("../queries/stereotype_validation"):
        if DEBUG:
            print(f"Running {i}")

        with open("../queries/stereotype_validation/" + i) as query_file:
            query = query_file.read()
            results = g.query(query)
            violation_count += len(results)
            if DEBUG:
                print(f"Found {len(results)} violations.")
            if len(results) > 0:
                violation_dict[i] = results

    print(f"Found {violation_count} violations total.")
    for k, v in violation_dict.items():
        print(f"Violations in {k}:")
        for row in v:
            print(f"{row.invalid} due to: {row.error_msg}")

if __name__ == "__main__": 
    main()