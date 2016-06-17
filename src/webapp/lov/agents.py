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
import dsl as dsl


class Vocabulary(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("FW") | Pos("DT") | Pos("JJ") | Pos("VBN"))

    def interpret(self, match):
        name = match.words.tokens
        return dsl.IsVocab() + HasKeyword(name)


class Person(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens
        return dsl.IsPerson() + HasKeyword(name)


class VocabContributorsQuestion(QuestionTemplate):
    """
    Regex for questions about band member.
    Ex: "adms contributors"
        "What are the contributors of adms?"
        result are the names 
    """
    regex1 = Vocabulary() + Lemma("contributor")
    regex2 = Lemma("contributor") + Pos("IN") + Vocabulary()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("contributor") + \
        Pos("IN") + Vocabulary()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member = dsl.IsContributorOf(match.vocabulary)
        member_name = dsl.Name(member)
        return member_name, "agent"


class VocabURIContributorsQuestion(QuestionTemplate):
    """
    Regex for questions about band member.
    Ex: "adms uri contributors"
        "What are the uri contributors of adms?"
        result are uris
    """
    regex1 = Vocabulary() + Lemmas("uri contributor")
    regex2 = Lemmas("uri contributor") + Pos("IN") + Vocabulary()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemmas("uri contributor") + \
        Pos("IN") + Vocabulary()

    regex = (regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        member = dsl.IsContributorOf(match.vocabulary)
        return member, "url"


class VocabCreatorQuestion(QuestionTemplate):
    """
    regex for creators of vocabs.
    Ex: "adms creator"
        "What are the creators of adms?"
        Note: seems not to work. Todo: Fix me
    """
    regex0 = Lemmas("who is") + Lemmas("creator of") + Vocabulary()
    regex1 = Vocabulary() + Lemma("creator")
    regex2 = Lemma("creator") + Pos("IN") + Vocabulary()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("creator") + \
        Pos("IN") + Vocabulary()

    regex = (regex0 | regex1 | regex2 | regex3) + Question(Pos("."))

    def interpret(self, match):
        creator = dsl.IsCreatorOf(match.vocabulary)
        creator_name = dsl.Name(creator)
        return creator_name, "agent"


class WhoPublishQuestion(QuestionTemplate):
    """
    Ex: "Who publish foaf?"
    return the name not the uri
    """
    regex0 = Lemma("who") + Lemma("publish") + Vocabulary()
    regex1 = Vocabulary() + Lemma("publish")
    regex2 = Lemma("publish") + Pos("IN") + Vocabulary()
    regex3 = Pos("WP") + Lemma("be") + Pos("DT") + Lemma("publish") + Pos("IN") + Vocabulary()
    regex4 = Lemmas("where be") + Vocabulary() + Lemma("from")

    regex = (regex0 | regex1 | regex2 | regex3 | regex4) + Question(Pos("."))

    def interpret(self, match):
        publisher = dsl.PublisherOf(match.vocabulary)
        publisher_name = dsl.Name(publisher)
        #return publisher, "literal"
        return publisher_name, "agent"







