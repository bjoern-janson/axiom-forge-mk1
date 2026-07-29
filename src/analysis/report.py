"""
report.py

Axiom Forge Mk1

Experiment Reporting

Converts raw benchmark outputs into a concise
research summary.

The report should answer:

    - Which agent had higher future viability?
    - Did RECA variables predict persistence?
    - Which perturbations mattered most?
    - Did performance diverge under repeated shock?

This file does not perform inference itself.
It formats results produced by:

    - trajectory_analysis.py
    - statistical_tests.py
    - benchmark experiments
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Sequence
from datetime import datetime

try:
    from src.analysis.trajectory_analysis import TrajectoryMetrics
except Exception:  # pragma: no cover
    TrajectoryMetrics = Any  # type: ignore

try:
    from src.analysis.statistical_tests import TestResult
except Exception:  # pragma: no cover
    TestResult = Any  # type: ignore


@dataclass
class AgentSummary:
    """
    Summary statistics for one agent.
    """

    name: str
    trajectory: TrajectoryMetrics
    extras: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ReportSection:
    """
    One named section in the final report.
    """

    title: str
    body: str


@dataclass
class ExperimentReport:
    """
    Full experiment report object.
    """

    title: str
    generated_at: str
    sections: List[ReportSection] = field(default_factory=list)

    def add_section(self, title: str, body: str) -> None:
        self.sections.append(
            ReportSection(title=title, body=body)
        )

    def to_markdown(self) -> str:
        lines: List[str] = [f"# {self.title}", "", f"_Generated: {self.generated_at}_", ""]

        for section in self.sections:
            lines.append(f"## {section.title}")
            lines.append("")
            lines.append(section.body.strip())
            lines.append("")

        return "\n".join(lines).strip()

    def to_text(self) -> str:
        lines: List[str] = [self.title, "=" * len(self.title), "", f"Generated: {self.generated_at}", ""]

        for section in self.sections:
            lines.append(section.title)
            lines.append("-" * len(section.title))
            lines.append("")
            lines.append(section.body.strip())
            lines.append("")

        return "\n".join(lines).strip()


def _fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        if value != value:  # NaN
            return "n/a"
        return f"{value:.{digits}f}"
    return str(value)


def _metric_table_row(label: str, value: Any) -> str:
    return f"| {label} | {_fmt(value)} |"


def format_trajectory_summary(summary: AgentSummary) -> str:
    t = summary.trajectory

    lines = [
        f"**Agent:** {summary.name}",
        "",
        "| Metric | Value |",
        "|---|---:|",
        _metric_table_row("Initial viability", t.initial_viability),
        _metric_table_row("Final viability", t.final_viability),
        _metric_table_row("Viability growth", t.viability_growth),
        _metric_table_row("Average reward", t.average_reward),
        _metric_table_row("Recovery speed", t.recovery_speed),
        _metric_table_row("Viability volatility", t.viability_volatility),
        _metric_table_row("Mean RECA score", t.reca_mean),
    ]

    if summary.extras:
        lines.extend(["", "**Extras**", ""])
        for k, v in summary.extras.items():
            lines.append(f"- {k}: {_fmt(v)}")

    return "\n".join(lines)


def format_prediction_results(results: Sequence[TestResult]) -> str:
    if not results:
        return "No statistical test results available."

    lines = [
        "| Predictor | Statistic | p-value | Interpretation |",
        "|---|---:|---:|---|",
    ]

    for r in results:
        statistic = getattr(r, "statistic", None)
        p_value = getattr(r, "p_value", None)
        interpretation = getattr(r, "interpretation", "n/a")
        name = getattr(r, "name", getattr(r, "predictor", "unknown"))

        lines.append(
            f"| {name} | {_fmt(statistic)} | {_fmt(p_value)} | {interpretation} |"
        )

    return "\n".join(lines)


def format_ranked_agents(ranked: Sequence[tuple[str, float]]) -> str:
    if not ranked:
        return "No ranking available."

    lines = [
        "| Rank | Agent | Score |",
        "|---:|---|---:|",
    ]

    for idx, (name, score) in enumerate(ranked, start=1):
        lines.append(f"| {idx} | {name} | {_fmt(score)} |")

    return "\n".join(lines)


def build_experiment_report(
    title: str,
    agent_summaries: Sequence[AgentSummary],
    prediction_results: Sequence[TestResult] | None = None,
    ranked_agents: Sequence[tuple[str, float]] | None = None,
    notes: Sequence[str] | None = None,
) -> ExperimentReport:
    """
    Build a full report object.

    Parameters
    ----------
    title:
        Human-readable report title.

    agent_summaries:
        One summary per evaluated agent.

    prediction_results:
        Statistical test outputs comparing predictors.

    ranked_agents:
        Optional ranking by viability score.

    notes:
        Optional bullet-point observations.
    """

    report = ExperimentReport(
        title=title,
        generated_at=datetime.utcnow().isoformat() + "Z",
    )

    overview_lines = [
        "This report summarizes Axiom Forge Mk1 benchmark results.",
        "",
        "Primary hypothesis:",
        "",
        r"\[
D_c \times C_e \times A_c \rightarrow G_{\mathcal V} \rightarrow \text{long-horizon persistence}
\]",
        "",
        "The benchmark tests whether future viability expansion predicts persistence better than current capability.",
    ]

    report.add_section(
        "Overview",
        "\n".join(overview_lines),
    )

    for summary in agent_summaries:
        report.add_section(
            f"Agent Summary — {summary.name}",
            format_trajectory_summary(summary),
        )

    if ranked_agents:
        report.add_section(
            "Agent Ranking",
            format_ranked_agents(ranked_agents),
        )

    if prediction_results is not None:
        report.add_section(
            "Predictive Statistics",
            format_prediction_results(prediction_results),
        )

    if notes:
        note_lines = [f"- {note}" for note in notes]
        report.add_section(
            "Notes",
            "\n".join(note_lines),
        )

    conclusion_lines = [
        "Key questions:",
        "",
        "1. Did RECA-style variables increase future viability?",
        "2. Did viability expansion predict future performance?",
        "3. Did the baseline merely recover while the RECA agent accumulated adaptive capacity?",
        "",
        "Interpretation guidance:",
        "",
        "- If RECA variables do not predict future persistence, the hypothesis fails.",
        "- If they do, the benchmark has identified a measurable property of evolvability.",
    ]

    report.add_section(
        "Conclusion",
        "\n".join(conclusion_lines),
    )

    return report


def write_report(
    report: ExperimentReport,
    path: str,
    markdown: bool = True,
) -> None:
    """
    Write report to disk.

    Parameters
    ----------
    report:
        ExperimentReport instance.

    path:
        Output file path.

    markdown:
        If True, write Markdown.
        Otherwise write plain text.
    """

    content = report.to_markdown() if markdown else report.to_text()

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def summarize_trajectory_metrics(
    agent_name: str,
    metrics: TrajectoryMetrics,
) -> str:
    """
    Convenience wrapper for a single-agent summary.
    """

    return format_trajectory_summary(
        AgentSummary(
            name=agent_name,
            trajectory=metrics,
        )
    )


def infer_best_agent(
    ranked_agents: Sequence[tuple[str, float]],
) -> str | None:
    """
    Return the name of the highest-ranked agent.
    """

    if not ranked_agents:
        return None

    return ranked_agents[0][0]
