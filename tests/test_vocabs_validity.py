from pathlib import Path
from typing import List

import pytest
import pyshacl
from rdflib import Graph

REPO_DIR = Path(__file__).parent.parent.resolve()
VOCABS_DIR = REPO_DIR / "vocabs"


@pytest.fixture
def _get_vocpub_graph() -> Graph:
    graph = Graph()
    graph.parse(Path(__file__).parent / "vocpub-4.10.ttl")
    return graph


@pytest.fixture
def _get_labels_graph() -> Graph:
    graph = Graph()
    graph.parse(Path(__file__).parent.parent / "labels.ttl")
    return graph


def _get_vocab_files() -> List[Path]:
    vocab_directories = [
        VOCABS_DIR,
        # VOCABS_DIR / "Addresses",
        # VOCABS_DIR / "LandParcels",
        # VOCABS_DIR / "GeographicalNames",
        # VOCABS_DIR / "TransportNetworks",
    ]
    files = []

    for directory in vocab_directories:
        files += directory.glob("**/*.ttl")

    return files


@pytest.mark.parametrize("vocab_file", _get_vocab_files())
def test_vocabs(vocab_file: List[Path], _get_vocpub_graph: Graph, _get_labels_graph: Graph):
    g = Graph().parse(vocab_file)

    # add labels & org details to data
    g += _get_labels_graph

    conforms, _, results_text = pyshacl.validate(
        data_graph=g,
        shacl_graph=_get_vocpub_graph,
        allow_warnings=True,
    )

    assert conforms, f"{vocab_file} failed:\n{results_text}"
