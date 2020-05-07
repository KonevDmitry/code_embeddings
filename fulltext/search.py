from elasticsearch import Elasticsearch


def search_python(es, is_s_ast, query):
    res = es.search(index='python', body={
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["pred"]
            }
        }
    }) if is_s_ast else \
        es.search(index='python', body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["original_string"]
                }
            }
        })

    return res['hits']['hits'][:10]


def get_doc(es, id):
    return es.get(index='python', id=id)


if __name__ == '__main__':
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for i in search_python(es, "predict"):
        print(i['_source']['docstring'])
        print("************")
    print("00000000000")
    for i in search_python(es, "infer"):
        print(i['_source'])
        print("************")
