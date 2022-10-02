# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/DCY1117/Curso2022-2023-ODKG/blob/master/Assignment4/course_materials/notebooks/Task08.ipynb

**Task 08: Completing missing data**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

from rdflib.plugins.sparql import prepareQuery

ns = Namespace("http://data.org#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

print("Grafo g1##############")
for subj, pred, obj in g1:
  print(subj,pred,obj)

print("Elementos de la clase Person en el primer grafo 1############")

q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdf:type ns:Person 
  } 
  ''',
  initNs = { "ns": ns}
)

for r in g1.query(q1):
  print(r)

print("Grafo 2 , Elementos de la clase persona y su given name, family name y email##############")

q2 = prepareQuery('''
  SELECT ?Subject ?given ?family ?email WHERE { 
    ?Subject rdf:type ns:Person.
    OPTIONAL{ ?Subject VCARD:Given ?given. }
    OPTIONAL{ ?Subject VCARD:Family ?family. }
    OPTIONAL{ ?Subject VCARD:EMAIL ?email. }
  }
  ''',
  initNs = { "ns": ns ,"VCARD": VCARD }
)

for r in g2.query(q2):
  print(r)

print("Completar campos en el grafo 1############")

g1.add((ns.SaraJones, VCARD.Given, Literal('Sara')))
g1.add((ns.SaraJones, VCARD.Family, Literal('Jones')))
g1.add((ns.SaraJones, VCARD.EMAIL, Literal('sara.jones@data.org')))

g1.add((ns.JohnSmith, VCARD.Given, Literal('John')))
g1.add((ns.JohnSmith, VCARD.Family, Literal('Smith')))
g1.add((ns.JohnSmith, VCARD.EMAIL, Literal('j.smith@data.org')))

g1.add((ns.JohnDoe, VCARD.Given, Literal('John')))
g1.add((ns.JohnDoe, VCARD.Family, Literal('Doe')))
g1.add((ns.JohnDoe, VCARD.EMAIL, Literal('doe@data.org')))

g1.add((ns.HarryPotter, VCARD.Given, Literal('Harry')))
g1.add((ns.HarryPotter, VCARD.EMAIL, Literal('hpotter@hogwarts.org')))

for r in g2.query(q2):
  print(r)