# coding: utf-8

"""
Main script for lov quepy.
"""

import sys
import argparse

import quepy
from SPARQLWrapper import SPARQLWrapper, JSON
import lov.printHandlers as printHandlers

# using directly the LOV endpoint to query
sparql = SPARQLWrapper("http://lov.okfn.org/dataset/lov/sparql")

lov = quepy.install("lov")


def vocaburi(vocab_url):
    """ Give the uri of a vocabulary
    """

    query = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    SELECT * WHERE {
        <%s> foaf:primaryTopic ?uri .
    }
    """ % vocab_url
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    if not results["results"]["bindings"]:
        print "Snorql URL not found"
        sys.exit(1)
    else:
        return results["results"]["bindings"][0]["uri"]["value"]


if __name__ == "__main__":
    default_questions = [
        "What is a car?",
        "What is foaf",
        "Who is Tom Cruise?",
        "Who is George Lucas?",
        "Who is Mirtha Legrand?",
        # "List Microsoft software",
        "Name Fiat cars",
        "time in argentina",
        "what time is it in Chile?",
        "List movies directed by Martin Scorsese",
        "How long is Pulp Fiction",
        "which movies did Mel Gibson starred?",
        "When was Gladiator released?",
        "who directed Pocahontas?",
        "actors of Fight Club",
    ]

    parser = argparse.ArgumentParser()
    parser.add_argument('--q', action='store', type=str, required=True, default=None, help='Query to be processed')
    parser.add_argument('--html', action='store_true', help='Output with HTML tags')
    parser.add_argument('--d', action='store_true', help='Set log level to Debug')
    args = parser.parse_args()

    # print('q: '+args.q)
    # print('html: '+str(args.html))
    # print('d: '+str(args.d))
    if args.d:
        quepy.set_loglevel("DEBUG")

    if len(args.q) > 1:
        question = args.q
        if question.count("http"):
            print vocaburi(question)
            sys.exit(0)
        else:
            questions = [question]
    else:
        questions = default_questions

    print_handlers = {
        "define": printHandlers.print_define,
        "category": printHandlers.print_category,
        "agent": printHandlers.print_agent,
        "url": printHandlers.print_url,
        "lang": printHandlers.print_lang,
        "enum": printHandlers.print_enum,
        "age": printHandlers.print_age,
        "literal": printHandlers.print_literal
    }

    for question in questions:
        ## Here we print the question
        print question
        print "-" * 2* len(question)
    
        target, query, metadata = lov.get_query(question)

        if isinstance(metadata, tuple):
            query_type = metadata[0]
            metadata = metadata[1]
        else:
            query_type = metadata
            metadata = None

        if query is None:
            print "Sorry. I don't understand your question...\n"
            continue

        #print query

        if target.startswith("?"):
            target = target[1:]
        if query:
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            if not results["results"]["bindings"]:
                print "Sorry. I am not able to answer your question..."
                continue

        print_handlers[query_type](results, target, args.html, metadata)
        print
