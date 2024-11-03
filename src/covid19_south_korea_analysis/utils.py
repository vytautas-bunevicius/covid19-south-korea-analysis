"""Module for loading and inspecting COVID-19 related datasets with detailed logging."""

import logging
from pathlib import Path
from typing import Any, Dict, Tuple
from collections import namedtuple

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_covid_data(assign_to_globals: bool = False
                   ) -> Tuple[Dict[str, pd.DataFrame], Any]:
    """Load COVID-19 related CSV files and optionally assign them to globals.

    This function reads multiple CSV files from a designated data directory and
    returns a dictionary of DataFrames and a named tuple containing all datasets.
    Optionally, it assigns each DataFrame to the global namespace for direct access.

    Args:
        assign_to_globals (bool): If True, assigns each DataFrame to a global
            variable.

    Returns:
        Tuple containing:
            - Dict[str, pd.DataFrame]: Dictionary mapping dataset filenames to
              their corresponding DataFrames.
            - CovidData: Named tuple containing all datasets as attributes.

    Raises:
        FileNotFoundError: If no datasets are loaded from the specified data path.
    """
    notebook_dir = Path(__file__).resolve().parent.parent.parent
    data_path = notebook_dir / 'data'

    file_to_var = {
        'seoul_floating.csv': 'seoul',
        'time_age.csv': 'timeage',
        'search_trend.csv': 'searchtrend',
        'time_province.csv': 'time_province',
        'weather.csv': 'weather',
        'patient_info.csv': 'patientinfo',
        'region.csv': 'region',
        'time_gender.csv': 'timegender',
        'policy.csv': 'policy',
        'case.csv': 'case',
        'time.csv': 'time'
    }

    datasets: Dict[str, pd.DataFrame] = {}
    CovidData = namedtuple('CovidData', list(file_to_var.values()))
    loaded_dfs: Dict[str, pd.DataFrame] = {}

    for filename, varname in file_to_var.items():
        file_path = data_path / filename
        try:
            if file_path.exists():
                df = pd.read_csv(file_path)
                datasets[filename] = df
                loaded_dfs[varname] = df
                logger.info(
                    "Successfully loaded '%s' into variable '%s'.", filename, varname
                )

                if assign_to_globals:
                    globals()[varname] = df
            else:
                logger.info(
                    "Could not find '%s' to load into variable '%s'.", filename, varname
                )
                loaded_dfs[varname] = None
        except (pd.errors.EmptyDataError, pd.errors.ParserError, FileNotFoundError) as error:
            logger.info(
                "Error loading '%s' into variable '%s': %s", filename, varname, str(error)
            )
            loaded_dfs[varname] = None

    if not datasets:
        error_msg = f"No datasets were loaded from {data_path}"
        logger.info(error_msg)
        raise FileNotFoundError(error_msg)

    covid_data = CovidData(**loaded_dfs)

    return datasets, covid_data


def get_dataset_info(datasets: Dict[str, pd.DataFrame]
                    ) -> pd.DataFrame:
    """Retrieve information about loaded datasets.

    This function compiles details such as the number of rows, columns,
    memory usage, and column names for each loaded dataset.

    Args:
        datasets (Dict[str, pd.DataFrame]): Dictionary of loaded datasets.

    Returns:
        pd.DataFrame: DataFrame containing information about each dataset.
    """
    info_data = []

    for name, df in datasets.items():
        if df is not None:
            info = {
                'Dataset': name,
                'Rows': len(df),
                'Columns': len(df.columns),
                'Memory (MB)': round(
                    df.memory_usage(deep=True).sum() / 1024 / 1024, 2
                ),
                'Columns List': ', '.join(df.columns)
            }
        else:
            info = {
                'Dataset': name,
                'Rows': 'N/A',
                'Columns': 'N/A',
                'Memory (MB)': 'N/A',
                'Columns List': 'N/A'
            }
        info_data.append(info)

    return pd.DataFrame(info_data)
