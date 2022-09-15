# AUTOGENERATED! DO NOT EDIT! File to edit: ../02_tabular_summaries.ipynb.

# %% auto 0
__all__ = []

# %% ../02_tabular_summaries.ipynb 3
import pandas as pd
from .Missing import PandasMissingDataFrame, PandasMissingSeries
from fastcore.basics import patch

# %% ../02_tabular_summaries.ipynb 10
@patch
def summarize_variable_missing(
    self: PandasMissingDataFrame,
    sort: bool = True, # Indicate whether to sort the result by `number_missing`.
    ascending: bool = False ,# Sort ascending vs. descending. Only applicable when sort is `True`.
    add_cumsum: bool = False # Indicate wheter or not to add the cumulative sum of missings. **Note**: cumsum is calculated based on input data.
) -> pd.DataFrame: # A pandas DataFrame containing the following columns: `variable`, `number_missing`, `proportion_missing`, `percentage_missing`, and optionally`number_missing_cumsum`.
    """Summarize the missingness in each variable.
    The summary always includes the number, proportion and percentage of missings.
    Besides, it could include the cumulative sum of missings.
    """
    return (
        self._df
        .isna()
        .sum()
        .reset_index(name="number_missing")
        .rename(columns={"index": "variable"})
        .assign(
            proportion_missing=lambda df: df.number_missing / df.number_missing.sum(),
            percentage_missing=lambda df: df.proportion_missing * 100        
        )
        .pipe(
            lambda df: df if not add_cumsum else (
                df
                .assign(
                    number_missing_cumsum=lambda internal_df: internal_df.number_missing.cumsum()
                )
            )
        )
        .pipe(
            lambda df: df if not sort else df.sort_values(
                by="number_missing",
                ascending=ascending
            )
        )
    )
