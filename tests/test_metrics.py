from src.metrics.recursive_depth import RecursiveDepth
from src.metrics.consequence_coupling import ConsequenceCoupling
from src.metrics.adaptive_consolidation import AdaptiveConsolidation


def test_metrics_initialize():

    dc = RecursiveDepth()
    ce = ConsequenceCoupling()
    ac = AdaptiveConsolidation()

    assert dc is not None
    assert ce is not None
    assert ac is not None
