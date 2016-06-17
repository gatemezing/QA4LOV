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
## Vocabulary

class IsVocab(FixedType):
    fixedtype = "voaf:Vocabulary"


class HasURI(FixedRelation):
    relation = "vann:preferredNamespaceUri"
    reverse = True


class DefinitionOf(FixedRelation):
    relation = "dcterms:description"
    language = "en"
    reverse = True


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


class ReleaseDateOf(FixedRelation):
    relation = "dcterms:issued"
    reverse = True


class HasLanguage(FixedRelation):
    relation = "dcterms:language"
    reverse = True


class TitleOf(FixedRelation):
    relation = "dcterms:title"
    reverse = True


class IsTitleOf(FixedRelation):
    relation = "rdfs:label"
    language = "en"


class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True


class ModifiedDateOf(FixedRelation):
    relation = "dcterms:modified"
    reverse = True


## agents
class IsPerson(FixedType):
    fixedtype = "foaf:Person"


class PublishedBy(FixedRelation):
    relation = "dcterms:publisher"


class CreatorOf(FixedRelation):
    relation = "dcterms:creator"
    reverse = True


class IsCreatorOf(FixedRelation):
    relation = "dcterms:creator"
    reverse = True


class IsContributorOf(FixedRelation):
    relation = "dcterms:contributor"
    reverse = True


class PublisherOf(FixedRelation):
    relation = "dcterms:publisher"
    reverse = True


class Name(FixedRelation):
    relation = "foaf:name"
    reverse = True