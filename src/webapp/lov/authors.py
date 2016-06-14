# coding: utf-8

# This file is based on quepy file sample for creating agents
#
# Author: Ghislain A. Atemezing
#          ghislain.atemezing@gmail.com

# TODO: this file needs to be cleaned up

"""
Authors related regex.
"""


from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dsl import  IsPerson


nouns = Pos("DT") | Pos("IN") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS")


class Book(Particle):
    regex = Plus(nouns)

    def interpret(self, match):
        name = match.words.tokens
        return IsBook() + HasKeyword(name)


class Author(Particle):
    regex = Plus(nouns | Lemma("."))

    def interpret(self, match):
        name = match.words.tokens
        return IsPerson() + HasKeyword(name)


class WhoWroteQuestion(QuestionTemplate):
    """
    Ex: "who wrote The Little Prince?"
        "who is the author of A Game Of Thrones?"
    """

    regex = ((Lemmas("who write") + Book()) |
             (Question(Lemmas("who be") + Pos("DT")) +
              Lemma("author") + Pos("IN") + Book())) + \
            Question(Pos("."))

    def interpret(self, match):
        author = NameOf(IsPerson() + AuthorOf(match.book))
        return author, "literal"


class BooksByAuthorQuestion(QuestionTemplate):
    """
    Ex: "list books by George Orwell"
        "which books did Suzanne Collins wrote?"
    """

    regex = (Question(Lemma("list")) + Lemmas("book by") + Author()) | \
            ((Lemma("which") | Lemma("what")) + Lemmas("book do") +
             Author() + Lemma("write") + Question(Pos(".")))

    def interpret(self, match):
        book = IsBook() + HasAuthor(match.author)
        book_name = NameOf(book)
        return book_name, "enum"
