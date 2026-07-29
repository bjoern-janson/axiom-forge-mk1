from src.experiments.reca_vs_baseline import run_experiment


if __name__ == "__main__":
    results = run_experiment()

    print("\nExperiment complete.")
    print(results)
