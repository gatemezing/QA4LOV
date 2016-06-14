# coding: utf-8

# This file is based on quepy file sample for creating agents
#
# Author: Ghislain A. Atemezing
#          ghislain.atemezing@gmail.com

"""
agents related regex
"""

from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dsl import  VersionOf, LabelOf, IsContributorOf, IsCreatorOf, IsVocab, HasVersion, HasLanguage, \
     ReuseVocab, UseByDataset, HasURI, Name


class Band(Particle):
    regex = Question(Pos("DT")) + Plus(Pos("NN") | Pos("NNP"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return IsBand() + HasKeyword(name)


class Vocab(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("FW") | Pos("DT") | Pos("JJ") | Pos("VBN"))

    def interpret(self, match):
        name = match.words.tokens
        return IsVocab() + HasKeyword(name)

class VocabContributorsQuestion(QuestionTemplate):
    """
    Regex for questions about band member.
    Ex: "adms contributors"
        "What are the contributors of adms?"
        result are the names 
    """

    regex1 = Vocab() + Lemma("contributor")
    regex2 = Lemma("contributor") + Pos("IN") + Vocab()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("contributor") + \
        Pos("IN") + Vocab()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member = IsContributorOf(match.vocab)
        member_name = Name(member)
        return member_name, "literal"


class VocabURIContributorsQuestion(QuestionTemplate):
    """
    Regex for questions about band member.
    Ex: "adms uri contributors"
        "What are the uri contributors of adms?"
        result are uris
    """

    regex1 = Vocab() + Lemmas("uri contributor")
    regex2 = Lemmas("uri contributor") + Pos("IN") + Vocab()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemmas("uri contributor") + \
        Pos("IN") + Vocab()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member = IsContributorOf(match.vocab)
        return member, "literal"


class VocabCreatorQuestion(QuestionTemplate):
    """
    regex for creators of vocabs.
    Ex: "adms creator"
        "What are the creators of adms?"
        Note: seems not to work. Todo: Fix me
    """

    regex1 = Vocab() + Lemma("creator")
    regex2 = Lemma("creator") + Pos("IN") + Vocab()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("creator") + \
        Pos("IN") + Vocab()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member = IsCreatorOf(match.vocab)
        #member_name = Name(member)
        return member, "literal"


class HowManyVocabQuestion(QuestionTemplate):
    """
    regex for reusing vocabs.
    Ex: "how many vocabularies reuse adms?"
        
    """

    regex1 = Lemmas("how many") + (Lemma("vocabularies")| Lemma("vocabulary")) + Lemma("reuse") + \
     Vocab() 
    
    regex = regex1 + Question(Pos("."))

    def interpret(self, match):
        number = ReuseVocab(match.vocab)
        return number, "literal"


class HowManyDatasetQuestion(QuestionTemplate):
    """
    regex for using datasets.
    Ex: "how many datasets use adms?"
        
    """

    regex1 = Lemmas("how many") + Lemma("datasets") + Lemma("use") + \
     Vocab() 
    
    regex = regex1 + Question(Pos("."))

    def interpret(self, match):
        numberd = UseByDataset(match.vocab)
        return numberd, "literal"


class VocabCreatorQuestion(QuestionTemplate):
    """
    regex for vocab versions.
    Ex: "adms versions"
        "What are the versions of adms?"
    """

    regex1 = Vocab() + Lemma("version")
    regex2 = Lemma("version") + Pos("IN") + Vocab()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("version") + \
        Pos("IN") + Vocab()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member = HasVersion(match.vocab)
        return member, "literal"



class VocabLanguageQuestion(QuestionTemplate):
    """
    regex for vocab languages.
    Ex: 
        "What are the languages of dcat?"
    """

    regex1 = Vocab() + Lemma("language")
    regex2 = Lemma("language") + Pos("IN") + Vocab()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("language") + \
        Pos("IN") + Vocab()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member_lang = HasLanguage(match.vocab)
        return member_lang, "literal"









