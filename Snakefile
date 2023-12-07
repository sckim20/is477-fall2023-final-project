rule prepare:
    output:
        "data/wine.data"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    input:
        "data/wine.data"
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

rule analyze:
    input:
        "data/wine.data"
    output:
        "results/alcohol_distribution.png",
        "results/correlation_matrix.png",
        "results/summary_statistics.csv"
    shell:
        "python scripts/analysis.py"
