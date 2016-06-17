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
import dsl as dsl


class Vocabulary(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("FW") | Pos("DT") | Pos("JJ") | Pos("VBN"))

    def interpret(self, match):
        name = match.words.tokens
        return dsl.IsVocab() + HasKeyword(name)


class WhatIsVocabQuestion(QuestionTemplate):
    """
    Regex for questions like "What is foaf"
    Ex: "What is dcterms"
    """
    regex1 = Lemma("who") + Lemma("be") + Vocabulary()
    regex2 = Lemma("what") + Lemma("be") + Vocabulary()

    regex = (regex1 | regex2) + Question(Pos("."))

    def interpret(self, match):
        desc = dsl.DefinitionOf(match.vocabulary)
        return desc, "define"


class WhereIsHomePageQuestion(QuestionTemplate):
    """
    Ex: "Where to find foaf documentation?"
    """
    regex = Lemmas("where to") + Lemma("find") + Vocabulary() + Lemma("documentation") + Question(Pos("."))

    def interpret(self, match):
        home_uri = dsl.IsHomePageOf(match.vocabulary)
        return home_uri, "url"


class ReleaseDateQuestion(QuestionTemplate):
    """
    Ex: when was voaf release?
        When was voaf release
    """
    regex1 = Lemmas("when be") + Vocabulary() + Lemma("release")
    regex2 = Lemmas("when be") + Vocabulary() + Lemma("issue")

    regex = (regex1 | regex2) + Question(Pos("."))

    def interpret(self, match):
        release_date = dsl.ReleaseDateOf(match.vocabulary)
        return release_date, "literal"


class ModifiedDateQuestion(QuestionTemplate):
    """
    Ex: when was voaf last update?
        When was voaf last update
    """
    regex1 = Lemmas("when be") + Vocabulary() + Lemmas("last update")
    regex2 = Lemmas("when be") + Vocabulary() + Lemmas("last modify")

    regex = (regex1 | regex2) + Question(Pos("."))

    def interpret(self, match):
        modif_date = dsl.ModifiedDateOf(match.vocabulary)
        return modif_date, "literal"


class HowOldIsQuestion(QuestionTemplate):
    """
    Ex: "How old is dcterms".
    """
    regex = Pos("WRB") + Lemma("old") + Lemma("be") + Vocabulary() + Question(Pos("."))

    def interpret(self, match):
        birth_date = dsl.ReleaseDateOf(match.vocabulary)
        return birth_date, "age"


class WhatCategory(QuestionTemplate):
    """
    Ex: "What is the category of foaf?"
    """
    regex = Lemma("what") + Lemma("be") + Lemma("the") + Lemma("category") + Pos("IN") + Vocabulary() + Question(Pos("."))

    def interpret(self, match):
        category = dsl.HasCategory(match.vocabulary)
        return category, "category"


# confusing. How to distinguish with namespace?
class WhatIsTitleQuestion(QuestionTemplate):
    """
    Ex: "What is the title of dcterms?"
    """
    regex1 = Lemma("what") + Lemma("be") + Lemmas("the title") + Pos("IN") + Vocabulary()
    regex2 = Vocabulary() + Lemma("title")

    regex = (regex1 | regex2) + Question(Pos("."))

    def interpret(self, match):
        title = dsl.TitleOf(match.vocabulary)
        return title, "enum"


class WhatIsNamespaceQuestion(QuestionTemplate):
    """
    Ex: "what is the namespace of dcterms?"
    """
    regex = Lemma("what") + Lemma("be") + Lemmas("the namespace") + Pos("IN") + Vocabulary() + Question(Pos("."))

    def interpret(self, match):
        uri = dsl.HasURI(match.vocabulary)
        return uri, "url"


class HowManyVocabQuestion(QuestionTemplate):
    """
    regex for reusing vocabs.
    Ex: "how many vocabularies reuse adms?"
    """
    regex1 = Lemmas("how many") + (Lemma("vocabularies") | Lemma("vocabulary")) + Lemma("reuse") + Vocabulary()

    regex = regex1 + Question(Pos("."))

    def interpret(self, match):
        number = dsl.ReuseVocab(match.vocabulary)
        return number, "literal"


class HowManyDatasetQuestion(QuestionTemplate):
    """
    regex for using datasets.
    Ex: "how many datasets use adms?"
    """

    regex1 = Lemmas("how many") + Lemma("datasets") + Lemma("use") + Vocabulary()

    regex = regex1 + Question(Pos("."))

    def interpret(self, match):
        numberd = dsl.UseByDataset(match.vocabulary)
        return numberd, "literal"


class VocabVersionQuestion(QuestionTemplate):
    """
    regex for vocab versions.
    Ex: "adms versions"
        "What are the versions of adms?"
    """
    regex1 = Vocabulary() + Lemma("version")
    regex2 = Lemma("version") + Pos("IN") + Vocabulary()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("version") + \
        Pos("IN") + Vocabulary()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member = dsl.HasVersion(match.vocabulary)
        return member, "url"


class VocabLanguageQuestion(QuestionTemplate):
    """
    regex for vocab languages.
    Ex: "What are the languages of dcat?"
    """
    regex1 = Vocabulary() + Lemma("language")
    regex2 = Lemma("language") + Pos("IN") + Vocabulary()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("language") + Pos("IN") + Vocabulary()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        lang = dsl.HasLanguage(match.vocabulary)
        lang_label = dsl.LabelOf(lang)
        return lang_label, "lang"
