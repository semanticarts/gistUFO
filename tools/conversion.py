from pathlib import Path
import requests
import json
from rdflib import Namespace, URIRef, Literal
from rdflib.graph import Graph, ConjunctiveGraph, Dataset
from rdflib.namespace import NamespaceManager, RDF, RDFS, XSD, SKOS, OWL
import csv
import re


DEBUG = False

dct = Namespace("http://purl.org/dc/terms/")
gist = Namespace("https://w3id.org/semanticarts/ns/ontology/gist/")
gistd = Namespace("https://w3id.org/semanticarts/ns/data/gist/")
owl = Namespace("http://www.w3.org/2002/07/owl#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
gistx = Namespace("https://w3id.org/semanticarts/ns/ontology/gistx/")

g = Dataset()

g.bind("dct", dct)
g.bind("gist", gist)
g.bind("gistd", gistd)
g.bind("owl", owl)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("skos", skos)
g.bind("xsd", xsd)
g.bind("gistx", gistx)

special = re.compile("[^A-Za-z0-9-:]")

def main():

    # open csv with rigidity data from data folder
    UFO_file = Path("./data/gist to UFO Stereotype(class stereotypes).csv")
    with open(UFO_file.absolute()) as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if DEBUG:  print(row)
            # fetch data from gist class and rigidity consesus rows
            gist_class = row.get("gist class")
            rigidity = row.get("Rigidity(consensus)")
            # identity = row.get("Provides Identity (consensus)") -- can use later 

            # trim gist class data into appropriate string, mint IRI
            gist_class_trimmed = gist_class[5:]
            gist_class_iri = URIRef(f"https://w3id.org/semanticarts/ns/ontology/gist/{gist_class_trimmed}")

            # if rigidity consensus data is present, trim to appropriate string, mint IRI, and add to graph
            if rigidity != "":
                rigidity_trimmed = "_Rigidity_" + re.sub("-", "",(rigidity.lower()))
                rigidity_iri = URIRef(f"https://w3id.org/semanticarts/ns/ontology/gistx/{rigidity_trimmed}")
                g.add((gist_class_iri, gist.isCategorizedBy, rigidity_iri))

    # output triples in turtle format to data folder
    output_file = Path("./data/gistUFOTriples.ttl")
    g.serialize(output_file)


if __name__ == "__main__": 
    main()