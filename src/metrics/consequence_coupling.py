"""
consequence_coupling.py

ASEB / RECA Benchmark Metric

Measures:

    C_e = Consequence Coupling

Definition:

    How strongly do environmental consequences
    influence which adaptive modifications persist?

A system has high C_e when:

    consequence
          |
          v
    modification selection
          |
          v
    retained structure


A system has low C_e when:

    modification
          |
          v
    arbitrary persistence


Core distinction:

    change != selected change

"""


from dataclasses import dataclass
from typing import List, Sequence
import math



@dataclass
class ModificationEvent:
    """
    Single adaptive modification attempt.

    Represents:

        T -> T'

    before selection.
    """

    modification_id: str

    predicted_effect: float

    observed_consequence: float

    retained: bool



@dataclass
class ConsequenceCouplingResult:
    """
    Output of C_e estimation.
    """

    coupling_score: float

    retention_rate: float

    consequence_alignment: float

    sample_size: int



def retention_rate(
    events: Sequence[ModificationEvent]
) -> float:
    """
    Fraction of modifications retained.

    This alone is not enough.

    A system retaining everything
    could have high retention but
    zero evolutionary filtering.
    """

    if not events:
        return 0.0

    retained = sum(
        1
        for event in events
        if event.retained
    )

    return retained / len(events)



def consequence_alignment(
    events: Sequence[ModificationEvent]
) -> float:
    """
    Measures whether consequences predict retention.

    High score:

        good consequences
        -> retained

        bad consequences
        -> rejected


    Low score:

        retention unrelated
        to reality.
    """

    if not events:
        return 0.0


    scores = []


    for event in events:

        consequence = (
            event.observed_consequence
        )

        prediction = (
            event.predicted_effect
        )


        # Agreement between expected
        # and observed consequence.

        agreement = (
            1 -
            abs(
                consequence -
                prediction
            )
            /
            (
                abs(consequence)
                +
                abs(prediction)
                +
                1e-8
            )
        )


        if event.retained:

            scores.append(
                max(
                    0,
                    agreement
                )
            )

        else:

            # Rejecting useful changes
            # reduces coupling.

            scores.append(
                max(
                    0,
                    1 - agreement
                )
            )


    return sum(scores) / len(scores)



def compute_consequence_coupling(
    events: Sequence[ModificationEvent]
) -> ConsequenceCouplingResult:
    """
    Main C_e estimator.

    Combines:

        retention
        +
        consequence alignment


    C_e is high when:

    1. changes are filtered,
    2. filtering follows consequences.

    """

    if not events:

        return ConsequenceCouplingResult(
            coupling_score=0.0,
            retention_rate=0.0,
            consequence_alignment=0.0,
            sample_size=0,
        )


    r_rate = retention_rate(
        events
    )


    alignment = consequence_alignment(
        events
    )


    # Geometric mean prevents one
    # component compensating completely
    # for the absence of another.

    coupling = math.sqrt(
        r_rate *
        alignment
    )


    return ConsequenceCouplingResult(
        coupling_score=coupling,
        retention_rate=r_rate,
        consequence_alignment=alignment,
        sample_size=len(events),
    )



def intervention_test(
    events: Sequence[ModificationEvent],
    shuffle_consequences: bool = True,
):
    """
    Causal sanity check.

    If consequences are randomly shuffled,
    a true consequence-coupled system
    should lose coupling.

    Expected:

        real consequences:
            high C_e

        shuffled consequences:
            lower C_e


    This prevents confusing:

        correlation

    with:

        consequence-driven selection.
    """

    if not shuffle_consequences:
        return compute_consequence_coupling(events)


    shuffled = list(events)

    consequences = [
        e.observed_consequence
        for e in shuffled
    ]


    import random

    random.shuffle(
        consequences
    )


    randomized = []

    for event, consequence in zip(
        shuffled,
        consequences
    ):

        randomized.append(
            ModificationEvent(
                modification_id=
                    event.modification_id,

                predicted_effect=
                    event.predicted_effect,

                observed_consequence=
                    consequence,

                retained=
                    event.retained,
            )
        )


    return compute_consequence_coupling(
        randomized
    )
