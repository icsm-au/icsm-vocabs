from pathlib import Path
from typing import List
from rdflib import Graph
from labelify import get_missing_labels

VOCABS_DIR = Path(__file__).parent.parent / "vocabs"
CONTEXT_DIR = Path(__file__).parent.parent / "_background"


def _get_context_graph():
    g = Graph()
    for f in CONTEXT_DIR.glob("*.ttl"):
        g.parse(f)
    return g

def _get_vocab_files() -> List[Path]:
    vocab_directories = [
        VOCABS_DIR
    ]
    files = []

    for directory in vocab_directories:
        files += directory.glob("**/*.ttl")

    return files


def get_missing_for_one_vocab(vocab: Graph, context_graph: Graph) -> List[str]:
    return get_missing_labels(vocab, context_graph)

CONTEXT_GRAPH = _get_context_graph()
print(f"Context graph generated, {len(CONTEXT_GRAPH)} triples long")

iris_missing_labels = set()
for vocab in _get_vocab_files():
    g = Graph().parse(vocab)
    print(f"{vocab.name}: {len(g)}")
    iris_missing_labels.update(get_missing_for_one_vocab(g, CONTEXT_GRAPH))
    print(f"missing labels count: {len(iris_missing_labels)}")

print(f"final missing labels count: {len(iris_missing_labels)}")

with open("missing_labels.txt", mode="w",) as myfile:
    myfile.write("\n".join(sorted(iris_missing_labels)))