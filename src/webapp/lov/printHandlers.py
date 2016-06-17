# coding: utf-8

# This file define some pretty print functions for the result
#
# Author: Pierre-Yves Vandenbussche


import time
import datetime
import random
import urllib


def print_literal(results, target, isHtml, metadata=None):
    for result in results["results"]["bindings"]:
        literal = result[target]["value"]
        if metadata:
            print ("<p>" if isHtml else "") + metadata.format(literal) + ("</p>" if isHtml else "")
        else:
            print ("<p>" if isHtml else "") + literal + ("</p>" if isHtml else "")


def print_agent(results, target, isHtml, metadata=None):
    for result in results["results"]["bindings"]:
        literal = result[target]["value"]
        if metadata:
            if isHtml:
                print "<p><a href='http://lov.okfn.org/dataset/lov/agents/"+urllib.quote('literal', safe='')+"'>"+metadata.format(literal)+"</a></p>"
            else:
                print metadata.format(literal)
        else:
            print ("<p>" if isHtml else "") + literal + ("</p>" if isHtml else "")


def print_category(results, target, isHtml, metadata=None):
    for result in results["results"]["bindings"]:
        literal = result[target]["value"]
        if metadata:
            print ("<p>" if isHtml else "") + metadata.format(literal) + ("</p>" if isHtml else "")
        else:
            print ("<p>" if isHtml else "") + literal + ("</p>" if isHtml else "")


def print_lang(results, target, isHtml, metadata=None):
    for result in results["results"]["bindings"]:
        literal = result[target]["value"]
        if metadata:
            print ("<p>" if isHtml else "") + metadata.format(literal) + ("</p>" if isHtml else "")
        else:
            print ("<p>" if isHtml else "") + literal + ("</p>" if isHtml else "")


def print_url(results, target, isHtml, metadata=None):
    for result in results["results"]["bindings"]:
        literal = result[target]["value"]
        if metadata:
            print ("<p>" if isHtml else "") + metadata.format(literal) + ("</p>" if isHtml else "")
        else:
            print ("<p>" if isHtml else "") + literal + ("</p>" if isHtml else "")

def print_define(results, target, isHtml, metadata=None):
    for result in results["results"]["bindings"]:
        if result[target]["xml:lang"] == "en":
            print result[target]["value"]
        else:
            print "not available in English"

        #else:
        #    print result[target]["value"]
        #    print


def print_enum(results, target, isHtml, metadata=None):
    used_labels = []

    for result in results["results"]["bindings"]:
        if result[target]["type"] == u"literal":
            if result[target]["xml:lang"] == "en":
                label = result[target]["value"]
                if label not in used_labels:
                    used_labels.append(label)
                    print label


def print_time(results, target, isHtml, metadata=None):
    gmt = time.mktime(time.gmtime())
    gmt = datetime.datetime.fromtimestamp(gmt)

    for result in results["results"]["bindings"]:
        offset = result[target]["value"].replace(u"−", u"-")

        if "to" in offset:
            from_offset, to_offset = offset.split("to")
            from_offset, to_offset = int(from_offset), int(to_offset)

            if from_offset > to_offset:
                from_offset, to_offset = to_offset, from_offset

            from_delta = datetime.timedelta(hours=from_offset)
            to_delta = datetime.timedelta(hours=to_offset)

            from_time = gmt + from_delta
            to_time = gmt + to_delta

            location_string = random.choice(["where you are",
                                             "your location"])

            print "Between %s and %s, depending %s" % \
                  (from_time.strftime("%H:%M"),
                   to_time.strftime("%H:%M on %A"),
                   location_string)

        else:
            offset = int(offset)

            delta = datetime.timedelta(hours=offset)
            the_time = gmt + delta

            print the_time.strftime("%H:%M on %A")


def print_age(results, target, isHtml, metadata=None):
    assert len(results["results"]["bindings"]) == 1

    birth_date = results["results"]["bindings"][0][target]["value"]
    year, month, days = birth_date.split("-")

    birth_date = datetime.date(int(year), int(month), int(days))

    now = datetime.datetime.utcnow()
    now = now.date()

    age = now - birth_date
    print "{} years old".format(age.days / 365)