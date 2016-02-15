# coding: utf-8

"""
Domain specific language for lov quepy.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation, FixedDataRelation

# Setup the Keywords for this application
#HasKeyword.relation = "rdfs:label"
HasKeyword.relation = "vann:preferredNamespacePrefix"
#HasKeyword.language = "en"



## here started the properties for LOV

class DefinitionOf(FixedRelation):
    relation = "dcterms:description"
    language = "en"
    reverse = True

class IsVocab(FixedType):
    fixedtype = "voaf:Vocabulary"

class PublishedBy(FixedRelation):
    relation = "dcterms:publisher"

class VersionOf(FixedRelation):
    relation = "dcat:distribution"
    reverse = True


class IsHomePageOf(FixedRelation):
    relation = "foaf:homepage"
    reverse = True
    

class ReuseVocab(FixedRelation):
	relation = "voaf:reusedByVocabularies"
	reverse = True

class UseByDataset(FixedRelation):
	relation = "voaf:reusedByDatasets"
	reverse = True


class HasVersion(FixedRelation):
	relation = "dcat:distribution"
	reverse = True


class HasCategory(FixedRelation):
	relation = "dcat:keyword"
	reverse = True


class HasURI(FixedRelation):
	relation = "vann:preferredNamespaceUri"
	reverse = True


class CreatorOf(FixedRelation):
    relation = "dcterms:creator"
    reverse = True

class IsCreatorOf(FixedRelation):
    relation = "dcterms:creator"
    reverse = True


class IsContributorOf(FixedRelation):
    relation = "dcterms:contributor"
    reverse = True


class ReleaseDateOf(FixedRelation):
    relation = "dcterms:issued"
    reverse = True

class IsPerson(FixedType):
    fixedtype = "foaf:Person"


class PublisherOf(FixedRelation):
    relation = "dcterms:publisher"
    reverse = True


class BirthDateOf(FixedRelation):
    relation = "dcterms:issued"
    reverse = True

class HasLanguage(FixedRelation):
    relation = "dcterms:language"
    reverse = True


class TitleOf(FixedRelation):
    relation = "dcterms:title"
    reverse= True

class IsTitleOf(FixedRelation):
    relation = "rdfs:label"
    language= "en"


class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True

class ModifiedDateOf(FixedRelation):
	relation = "dcterms:modified"
	reverse = True 