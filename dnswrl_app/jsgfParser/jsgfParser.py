from jsgf import PublicRule, Literal, Grammar
from jsgf.parser import parse_grammar_string
import os

def findTags(inputText):
    current_path = os.path.abspath(__file__)
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    examinePath = father_path+'/example.jsgf'
    with open(examinePath, "r", encoding='utf-8') as f:
        lines = f.readlines()

    content = "".join(lines)

    grammar = parse_grammar_string(content)
    matching = grammar.find_matching_rules(inputText)
    if len(matching) > 0:
        tags = matching[0].get_tags_matching(inputText)
    else:
        tags = []
    # tags = grammar.get_tags_matching(inputText)
    return matching, tags

if __name__ == '__main__':
    input_text = '我有点胃疼'
    matching, tags = findTags(input_text)
    # print(matching)
    # print(tags)
    for tag in tags:
        print(tag)

    str = '头痛'
    print(str in str.split('|'))

    # print(matching[0].get_tags_matching(input_text))
    # print(tags)
