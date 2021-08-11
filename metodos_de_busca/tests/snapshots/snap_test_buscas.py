# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_busca_gulosa busca_gulosa"] = [
    "Cidade: Sibiu, heuristica: 253",
    "Cidade: Fagaras, heuristica: 178",
    "Cidade: Bucharest, heuristica: 0",
]
