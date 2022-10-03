# -*- coding: utf-8 -*-
"""Task07.ipynb의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aT3eVeIl2rKiDvDmIM3q6Bf8WoiCaGHq

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo (We read the RDF file in the way we have been doing)"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

ns = Namespace("http://somewhere#")
for s,p,o in g.triples((None, RDFS.subClassOf,ns.Person)):
  print(s)

from rdflib.plugins.sparql import prepareQuery
q1 = prepareQuery('''
SELECT ?sub 
WHERE {
  ?sub rdfs:subClassOf ns:Person.
      }
      ''',
      initNs={"rdfs":RDFS, "ns":ns})

for r in g.query(q1):
 print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)

for s,p,o in g.triples((None,RDFS.subClassOf, ns.Person)):
  for s1,p1,o1 in g.triples((None, RDF.type, s)):
    print(s1)

q1 = prepareQuery('''
  SELECT ?per 
  WHERE { 
    ?sub rdfs:subClassOf* ns:Person.
    ?per rdf:type ?sub. 
        }
        ''',
  initNs = { "rdf": RDF, "rdfs": RDFS, "ns": ns})

for r in g.query(q1):
  print(r)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

for s,p,o in g.triples((None, RDF.type,ns.Person)): 
  for s1,p1,o1 in g.triples((s,None,None)): 
    print(s1,p1,o1)

for s,p,o in g.triples((None, RDFS.subClassOf,ns.Person)): 
  for s1,p1,o1 in g.triples((None, RDF.type, s)): 
    for s2,p2,o2 in g.triples((s1,None,None)): 
      print(s2,p2,o2)


q2 = prepareQuery('''
SELECT ?per ?properties ?o 
WHERE {
  {
    ?sub rdfs:subClassOf* ns:Person.
    ?per rdf:type ?sub.
    ?per ?properties ?o.
  }
  UNION
  {
    ?per rdf:type ns:Person.
    ?per ?properties ?o.
  }
}
  ''', 
initNs={"ns":ns})

for r in g.query(q2):
 print(r)