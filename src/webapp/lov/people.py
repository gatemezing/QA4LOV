# coding: utf-8

# This file is based on quepy file 
#
# Author: Ghislain A. Atemezing
#          ghislain.atemezing@gmail.com

"""
vocabulary related regex
"""

from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dsl import IsPerson, LabelOf, DefinitionOf, BirthDateOf, IsVocab, ReleaseDateOf, \
    TitleOf, PublisherOf, CreatorOf, ModifiedDateOf, IsTitleOf, IsHomePageOf, HasURI, \
    HasCategory



class Person(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens
        return IsPerson() + HasKeyword(name)


class Vocabulary(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("FW") | Pos("DT") | Pos("JJ") | Pos("VBN"))

    def interpret(self, match):
        name = match.words.tokens
        return IsVocab() + HasKeyword(name)


class WhatIs(QuestionTemplate):
    """
    Regex for questions like "What is foaf"
    Ex: "What is dcterms"
         
    """

    regex = Lemma("what") + Lemma("be")  + Vocabulary() + \
         Question(Pos("."))

    def interpret(self, match):
        desc = DefinitionOf(match.vocabulary)
        return desc, "define"

class WhoIs(QuestionTemplate):
    """
    Ex: "Who is foaf?"
    """

    regex = Lemma("who") + Lemma("be") + Vocabulary() + \
        Question(Pos("."))

    def interpret(self, match):
        definition = DefinitionOf(match.vocabulary)
        return definition, "define"


class WhereIsFromQuestion(QuestionTemplate):
    """
    Ex: "Where is foaf from?"
    """

    regex = Lemmas("where be") + Vocabulary() + Lemma("from") + \
        Question(Pos("."))

    def interpret(self, match):
        publisher_uri = PublisherOf(match.vocabulary)
        #label = LabelOf(birth_place)

        return publisher_uri, "literal"   #use enum for label


class WhereIsHomePageQuestion(QuestionTemplate):
    """
    Ex: "Where to find foaf documentation?"
    """

    regex = Lemmas("where to") + Lemma("find") + Vocabulary() +  \
        Lemma("documentation") + Question(Pos("."))

    def interpret(self, match):
        home_uri = IsHomePageOf(match.vocabulary)
        #label = LabelOf(birth_place)

        return home_uri, "literal"   #use enum for label


class ReleaseDateQuestion(QuestionTemplate):
    """
    Ex: when was voaf release?
        When was voaf release
    """

    regex = Lemmas("when be") + Vocabulary() + Lemma("release") + \
        Question(Pos("."))

    def interpret(self, match):
        release_date = ReleaseDateOf(match.vocabulary)
        return release_date, "literal"


class ModifiedDateQuestion(QuestionTemplate):
    """
    Ex: when was voaf last update?
        When was voaf last update
    """

    regex = Lemmas("when be") + Vocabulary() + Lemmas("last update") + \
        Question(Pos("."))

    def interpret(self, match):
        modif_date = ModifiedDateOf(match.vocabulary)
        return modif_date, "literal"



class WhoIsCreatorQuestion(QuestionTemplate):
    """
    Ex: "Who is creator of dcterms?"
    """

    regex = Lemmas("who is") + Lemmas("creator of") + Vocabulary() + \
        Question(Pos("."))

    def interpret(self, match):
        creator_uri = CreatorOf(match.vocabulary)

        return creator_uri, "literal"


class HowOldIsQuestion(QuestionTemplate):
    """
    Ex: "How old is dcterms".
    """

    regex = Pos("WRB") + Lemma("old") + Lemma("be") + Vocabulary() + \
        Question(Pos("."))

    def interpret(self, match):
        birth_date = BirthDateOf(match.vocabulary)
        return birth_date, "age"



class WhatIs(QuestionTemplate):
    """
    Ex: "What is dcterms?"
    """

    regex = Lemma("what") + Lemma("be") + Vocabulary() + \
        Question(Pos("."))

    def interpret(self, match):
        definition = DefinitionOf(match.vocabulary)
        return definition, "define"



class WhoPublish(QuestionTemplate):
    """
    Ex: "Who publish foaf?"
    """

    regex = Lemma("who") + Lemma("publish") + Vocabulary() + \
        Question(Pos("."))

    def interpret(self, match):
        publisher = PublisherOf(match.vocabulary)
        return publisher, "literal"


class WhatCategory(QuestionTemplate):
    """
    Ex: "What is the category of foaf?"
    """

    regex = Lemma("what")  + Lemma("be") + Lemma("the") + Lemma("category")  + Pos("IN") + Vocabulary() + \
        Question(Pos("."))

    def interpret(self, match):
        category = HasCategory(match.vocabulary)
        return category, "literal"


# confusing. How to distinguish with namespace?
# TODO: fixme
class WhatIsTitleQuestion(QuestionTemplate):
    """
    Ex: "What is the title of dcterms?"
    """

    regex = Lemma("what") + Lemma("be") + Lemmas("the title") + Pos("IN") + Vocabulary() +\
        Question(Pos("."))

    def interpret(self, match):
        title = TitleOf(match.vocabulary)
        return title, "enum"



class WhatIsNamespaceQuestion(QuestionTemplate):
    """
    Ex: "what is the namespace of dcterms?"
    """

    regex1 = Lemma("what") + Lemma("be") + Lemmas("the namespace") + Pos("IN") + Vocabulary()

    regex = (regex1) + Question(Pos("."))  
        

    def interpret(self, match):
        uri = HasURI(match.vocabulary)
        return uri, "literal"


class WhatIsTitleENQuestion(QuestionTemplate):
    """
    Ex: "What is the title of foaf?"
    """

    regex =  Vocabulary() +  Lemma("title") + \
        Question(Pos("."))

    def interpret(self, match):
        title_en = IsTitleOf(match.vocabulary)
        #label = LabelOf(title)
        return title_en, "enum"


