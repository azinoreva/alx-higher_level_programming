#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        senLen = len(sentence)
    else:
        senLen = 0
    return (senLen, sentence if not sentence else sentence[:1])
