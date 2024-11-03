"""This module contains unit tests for COVID-19 data loading and inspection functionality.

The tests cover data loading from CSV files, handling of corrupted files,
global variable assignments, and dataset information retrieval functions.
"""

from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

from src.covid19_south_korea_analysis.utils import load_covid_data, get_dataset_info


@pytest.fixture
def mock_csv_files():
    """Create mock CSV data for testing.

    Returns:
        dict: Dictionary containing mock DataFrames for testing.
    """
    return {
        'case.csv': pd.DataFrame({'id': [1, 2], 'case': ['A', 'B']}),
        'time.csv': pd.DataFrame({'date': ['2020-01-01', '2020-01-02'], 'count': [10, 20]}),
        'policy.csv': pd.DataFrame({'policy': ['X', 'Y'], 'date': ['2020-01-01', '2020-01-02']})
    }


@pytest.fixture
def mock_data_path(tmp_path: Path) -> Path:
    """Set up a temporary directory with mock CSV files.

    Args:
        tmp_path: Pytest fixture providing temporary directory path.

    Returns:
        Path: Path to temporary data directory.
    """
    data_dir = tmp_path / 'data'
    data_dir.mkdir()
    return data_dir


def test_load_covid_data_successful(mock_data_path: Path, mock_csv_files: dict): # pylint: disable=redefined-outer-name
    """Verify successful loading of COVID data files."""
    for filename, dataframe in mock_csv_files.items():
        dataframe.to_csv(mock_data_path / filename, index=False)

    with patch('src.covid19_south_korea_analysis.utils.Path.resolve') as mock_resolve:
        mock_resolve.return_value.parent.parent.parent = mock_data_path.parent

        datasets, covid_data = load_covid_data()

        assert isinstance(datasets, dict)
        assert len(datasets) == 3
        assert all(isinstance(df, pd.DataFrame) for df in datasets.values())
        assert isinstance(covid_data, tuple)
        # Assuming CovidData is a namedtuple or similar with attributes 'case', 'time', 'policy'
        assert hasattr(covid_data, 'case')
        assert hasattr(covid_data, 'time')
        assert hasattr(covid_data, 'policy')


def test_load_covid_data_with_globals(mock_data_path: Path, mock_csv_files: dict): # pylint: disable=redefined-outer-name
    """Verify loading COVID data with global variable assignment."""
    for filename, dataframe in mock_csv_files.items():
        dataframe.to_csv(mock_data_path / filename, index=False)

    with patch('src.covid19_south_korea_analysis.utils.Path.resolve') as mock_resolve:
        mock_resolve.return_value.parent.parent.parent = mock_data_path.parent

        _, _ = load_covid_data(assign_to_globals=True)

        # Suppress linter warnings since these are dynamically assigned
        from src.covid19_south_korea_analysis.utils import case, time, policy  # pylint: disable=no-name-in-module,import-outside-toplevel

        assert all(var is not None for var in [case, time, policy])


def test_load_covid_data_empty_directory(tmp_path: Path):
    """Verify handling of empty data directory."""
    empty_dir = tmp_path / 'empty'
    empty_dir.mkdir()

    with patch('src.covid19_south_korea_analysis.utils.Path.resolve') as mock_resolve:
        mock_resolve.return_value.parent.parent.parent = empty_dir.parent

        with pytest.raises(FileNotFoundError):
            load_covid_data()


def test_load_covid_data_corrupted_file(mock_data_path: Path, mock_csv_files: dict): # pylint: disable=redefined-outer-name
    """Verify handling of corrupted CSV file."""
    for filename, dataframe in mock_csv_files.items():
        if filename != 'case.csv':
            dataframe.to_csv(mock_data_path / filename, index=False)

    corrupted_file = mock_data_path / 'case.csv'
    corrupted_file.write_text('corrupted,data\n1,2,3\ncompletely,invalid,data,extra,columns')

    with patch('src.covid19_south_korea_analysis.utils.Path.resolve') as mock_resolve:
        mock_resolve.return_value.parent.parent.parent = mock_data_path.parent

        datasets, covid_data = load_covid_data()

        assert isinstance(datasets, dict)
        assert 'case.csv' not in datasets
        assert 'time.csv' in datasets
        assert 'policy.csv' in datasets
        # Assuming CovidData has an attribute 'case' set to None if loading fails
        assert covid_data.case is None


def test_get_dataset_info():
    """Verify dataset information retrieval functionality."""
    datasets = {
        'test1.csv': pd.DataFrame({'A': [1, 2], 'B': [3, 4]}),
        'test2.csv': pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9]})
    }

    info_df = get_dataset_info(datasets)

    assert isinstance(info_df, pd.DataFrame)
    assert len(info_df) == 2
    assert all(col in info_df.columns for col in [
        'Dataset', 'Rows', 'Columns', 'Memory (MB)', 'Columns List'
    ])

    test1_info = info_df[info_df['Dataset'] == 'test1.csv'].iloc[0]
    assert test1_info['Rows'] == 2
    assert test1_info['Columns'] == 2
    assert 'A, B' in test1_info['Columns List']


def test_get_dataset_info_with_none():
    """Verify dataset information retrieval with None values."""
    datasets = {
        'test1.csv': None,
        'test2.csv': pd.DataFrame({'A': [1, 2]})
    }

    info_df = get_dataset_info(datasets)

    none_info = info_df[info_df['Dataset'] == 'test1.csv'].iloc[0]
    assert none_info['Rows'] == 'N/A'
    assert none_info['Columns'] == 'N/A'
    assert none_info['Memory (MB)'] == 'N/A'
    assert none_info['Columns List'] == 'N/A'


@pytest.mark.parametrize('test_input,expected', [
    ({'test.csv': pd.DataFrame()}, 1),
    ({}, 0),
    ({'a.csv': None, 'b.csv': None}, 2)
])
def test_get_dataset_info_edge_cases(test_input: dict, expected: int):
    """Verify dataset information retrieval edge cases.

    Args:
        test_input: Input dictionary containing test data.
        expected: Expected number of rows in result DataFrame.
    """
    info_df = get_dataset_info(test_input)
    assert len(info_df) == expected
    assert isinstance(info_df, pd.DataFrame)
