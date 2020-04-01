from elasticsearch import Elasticsearch


def search_python(es, query):
    res = es.search(index='python', doc_type='func', body={
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["func_name", "original_string", "language"]
            }
        }
    })
    return res['hits']['hits'][:10]


def get_doc(es, id):
    return es.get(index='python', doc_type='func', id=id)


if __name__ == '__main__':
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for i in search_python(es, "predict"):
        print(i['_source']['docstring'])
        print("************")
    print("00000000000")
    for i in search_python(es, "infer"):
        print(i['_source'])
        print("************")
