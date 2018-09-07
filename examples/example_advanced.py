import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.advanced.AdvancedXMLLoader import AdvancedXMLLoader

ENDPOINT = 'http://gaiadev01.isi.edu:3030/rpi0901aif80d2/query'

def run(xml_query):
    with open(xml_query) as f:
        xml = f.read()

    loader = AdvancedXMLLoader(xml)
    # auto answer all:
    all_ans = loader.answer_all(ENDPOINT)

    for ans in all_ans:
        print(ans['sparql'])
        print(ans['response'])


def run_single(xml_query):
    with open(xml_query) as f:
        xml = f.read()

    loader = AdvancedXMLLoader(xml)
    # try specified relaxation for a single query:
    relax = {
        'wider_range': False,
        'at_least_n': 0,
        'on_supergraph': True,
        'ignore_enttype': False
    }
    ans = loader.answer_one_specify_relaxation(loader.get_question_list()[0], ENDPOINT, relax)
    print(ans['sparql'])
    print(ans['response'])


# example query provided by NIST
# run('xml_queries/graph_query.xml')

# subgraph as query in our dataset
run_single('xml_queries/autogenerated_query_2.xml')

# run('xml_queries/simple_query.xml')


