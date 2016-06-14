# coding: utf-8

# This file is based on quepy file sample for settings
#
# Author: Ghislain A. Atemezing
#          ghislain.atemezing@gmail.com
"""
Settings.
"""

# Generated query language
LANGUAGE = "sparql"

# NLTK config
NLTK_DATA_PATH = []  # List of paths with NLTK data

# Encoding config
DEFAULT_ENCODING = "utf-8"

# Sparql config
SPARQL_PREAMBLE = u"""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX quepy: <http://www.machinalis.com/quepy#>
PREFIX dbpedia: <http://dbpedia.org/ontology/>
PREFIX dbpprop: <http://dbpedia.org/property/>
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX vann:<http://purl.org/vocab/vann/>
PREFIX voaf:<http://purl.org/vocommons/voaf#>
PREFIX dcterms:<http://purl.org/dc/terms/>
PREFIX dcat:<http://www.w3.org/ns/dcat#>

"""
