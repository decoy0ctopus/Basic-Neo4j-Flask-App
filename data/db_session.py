from py2neo import Graph


def db_auth():
    user = 'neo4j'
    pword = 'password'
    graph = Graph("bolt://localhost:7687", auth=(user, pword))
    return graph