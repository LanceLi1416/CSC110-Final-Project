# -*- coding: <UTF-8> -*-
"""Your Anxiety During COVID-19: data

Module Description
==================
This module contains the functions that read, extract, and process data from a dataset. It provides
two public IO interfaces to store processed data, and to read the stored data. It also provides an
interface for calculating the extrema of the processed data.

Copyright and Usage Information
===============================
This project is licensed under the GNU General Public License v3.0.
    Permissions of this strong copyleft license are conditioned on making available complete source
    code of licensed works and modifications, which include larger works using a licensed work,
    under the same license. Copyright and license notices must be preserved. Contributors provide an
    express grant of patent rights.

Authors (by alphabetical order):
  - Faruk, Fardin   https://github.com/Fard-Faru
  - Hsieh, Sharon   https://github.com/SharonHsieh22
  - Li, Sinan       https://github.com/LanceLi1416/
  - Zhan, Jeffery   https://github.com/jeffzhan
"""
import csv
import json
from typing import Dict, List, Tuple

import constants


def calculate_extrema(data: List[Dict[str, float]]) -> Tuple[float, float]:
    """Calculate the minimum and maximum anxiety score for all combinations of identity groups.

    >>> import math
    >>> sample_data = [{"18-24": 5.0792821066052225, "25-34": 0.5522088004403117,}, \
                       {"Male": -5.757139888991139, "Female": -1.7634546268885034}]
    >>> extrema = calculate_extrema(sample_data)
    >>> math.isclose(extrema[0], -2.6024655442754137)
    True
    >>> math.isclose(extrema[1], 1.6579137398583597)
    True
    """
    min_so_far, max_so_far, len_data = 0, 0, len(data)

    for identity_group in data:
        min_so_far = min_so_far + min(identity_group.values())
        max_so_far = max_so_far + max(identity_group.values())

    return min_so_far / len_data, max_so_far / len_data


def load_json_data(file_name: str, file_encoding: str = 'UTF-8') -> List[Dict[str, float]]:
    """Load the previously stored json file

    Preconditions:
      - os.path.isfile(file_name)

    >>> test_data = load_json_data(constants.TEST_DATA_JSON_FILE)
    """
    with open(file_name, 'r', encoding=file_encoding) as json_file:
        data = json.load(json_file)
    return data


def process_data(input_file_name: str, output_file_name: str,
                 input_encoding: str = 'ISO-8859-1', output_encoding: str = 'UTF-8') -> None:
    """Process the data, then store it in a json file for future reference

    Preconditions:
      - os.path.isfile(file_name)
      - input_file_name.endswith('.csv')
      - output_file_name.endswith('.json')
    """
    data = _calculate_data_average(_regulate_na(read_csv_file(input_file_name, input_encoding)))
    with open(output_file_name, 'w', encoding=output_encoding) as json_file:
        json.dump(data, json_file)


def read_csv_file(file_name: str, file_encoding: str = 'ISO-8859-1') -> \
        List[Dict[str, Tuple[int, float]]]:
    """Return the data stored in a csv file with the given filename.

    The return value is list consisting of 11 dictionaries:
    - The first is a dictionary with age ranges (in groups of 10)
    - The second is a dictionary of genders
    - The third is a dictionary of education statuses
    - The fourth is a dictionary of employment statuses
    - The fifth is a dictionary of countries of residence
    - The sixth is a dictionary of whether or not the participant is an expatriate
    - The seventh is a dictionary of marital statuses
    - The eighth is a dictionary of whether or not the participant is part of a high-risk group
        for Coronavirus
    - The ninth is a dictionary of isolation status
    - The tenth is a dictionary of ranges of the number of adults the participant is isolating with
    - The eleventh is a dictionary of ranges of the number of children the participant
        is isolating with (edited)

    The dictionaries each map to their own tuple of two items,
    the first being the population (or number of people) that have added their score to it
    and the second being the total stress_score that has been added to them,

    Preconditions:
      - file_name.endswith('.csv')
      - os.path.isfile(file_name)
    """
    # ACCUMULATOR data_processed_so_far: the running list of
    data_processed_so_far = _initialize_data_list()

    with open(file_name, encoding=file_encoding) as file:
        reader = csv.reader(file)
        # Reads the first row of the csv file, which contains the headers.
        next(reader)
        # This list comprehension reads each remaining row of the file, where each row is
        # represented as a list of strings.
        # The header row is *not* included in this list.
        for row in reader:
            stress_score = _calc_stress_score(row)

            # change from numerical to category
            _add_age_to_dict(int(row[4]), stress_score, data_processed_so_far)
            _add_isolation_to_dict(row[16], 9, stress_score, data_processed_so_far)
            _add_isolation_to_dict(row[17], 10, stress_score, data_processed_so_far)
            # countries - some countries are not displayed correctly
            _add_country_to_dict(row[9], stress_score, data_processed_so_far)
            # expat - csv file uses lower case
            _add_expat_to_dict(row[10], stress_score, data_processed_so_far)
            # marital - csv file uses ' or ' instead of '/'
            _add_marital_to_dict(row[12], stress_score, data_processed_so_far)
            # remaining ones
            remaining_columns = [5, 6, 8, 14, 15]
            for csv_index in remaining_columns:
                category = data_processed_so_far[
                    remaining_columns.index(csv_index) + (1 if csv_index < 10 else 4)]
                if row[csv_index] in category:
                    value = category[row[csv_index]]
                    category[row[csv_index]] = (value[0] + 1, value[1] + stress_score)

    return data_processed_so_far


def _initialize_data_list() -> List[Dict[str, Tuple[int, float]]]:
    """Return initialized values

    >>> initial = _initialize_data_list()
    >>> all(list(initial[i].keys()) == (constants.IDENTITY_GROUP_OPTIONS_LIST[i] + ['NA']) \
            for i in range(len(initial)))
    True
    """
    data_start = [
        # Initialize age
        {age: (0, 0.0) for age in constants.DEM_AGE + ['NA']},
        # Initialize gender
        {gender: (0, 0.0) for gender in constants.DEM_GENDER + ['NA']},
        # Initialize education
        {edu: (0, 0.0) for edu in constants.DEM_EDU + ['NA']},
        # Initialize employment status
        {employment: (0, 0.0) for employment in constants.DEM_EMPLOYMENT + ['NA']},
        # Initialize country of residence
        {country: (0, 0.0) for country in constants.COUNTRIES + ['NA']},
        # Initialize whether they are an expatriate
        {expat: (0, 0.0) for expat in constants.EXPAT + ['NA']},
        # Initialize marital status
        {marital_status: (0, 0.0) for marital_status in constants.DEM_MARITAL_STATUS + ['NA']},
        # Initialize whether they reside in a high risk group
        {risk_group: (0, 0.0) for risk_group in constants.RISK_GROUP + ['NA']},
        # Initialize isolation status
        {isolation: (0, 0.0) for isolation in constants.DEM_ISOLATION + ['NA']},
        # Initialize adults isolated with participant
        {iso_adults: (0, 0.0) for iso_adults in constants.DEM_ISOLATION_PEOPLE + ['NA']},
        # Initialize children isolated with participant
        {iso_kids: (0, 0.0) for iso_kids in constants.DEM_ISOLATION_PEOPLE + ['NA']}
    ]

    return data_start


def _calc_stress_score(person: List[str]) -> float:
    """Return stress score from a row of the dataset

    Preconditions:
      - len(person) > 144
    """
    # Value added for each response in the survey
    # Depending on the nature of the question we may want to reduce or increase the stress score
    stress_method = [
        # Scale_PSS10_UCLA
        1, 1, 1, -1, -1, 1, -1, -1, 1, 1,
        1, 1, 1,
        # OECD_people
        -1, -1,
        # OECD_institutions
        -1, -1, -1, -1, -1, -1,
        # Corona_concerns
        1, 1, 1, 1, 1,
        # Trust_countrymeasure
        -1,
        # Compliance
        -1, 0, 0, 1, -1, 1,
        # BFF_15
        1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0,
        # Expl_Distress
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        # SPS
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        1, 1, 1, 1, 1, -1
    ]

    # Tuple Consists of:
    # First element is the scale that all the questions in a category are measured upon
    # Second element is number of questions within the same category
    category_tuples = [(5, 10), (5, 3), (11, 2), (11, 6), (6, 5), (11, 1),
                       (6, 6), (6, 15), (6, 25), (6, 10), (6, 15), (6, 6)]
    # List of values from dataset of survey used for calculations
    answer_values = person[21:54] + person[70:109] + person[110:136] + person[137:144]
    # ACCUMULATOR stress_so_far: running sum of stress score
    stress_so_far = 0.0
    # ACCUMULATOR absolute_index: running index to offset the for loop scaling
    absolute_index = 0

    for scale_tuple in category_tuples:
        for _ in range(scale_tuple[1]):
            og_answer = answer_values[absolute_index]
            if og_answer != 'NA' and int(og_answer) <= scale_tuple[0]:
                bounded_answer = ((int(og_answer) - 1) * (4 / (scale_tuple[0] - 1)))
                stress_so_far += bounded_answer * stress_method[absolute_index]
            absolute_index += 1
    return stress_so_far


def _add_age_to_dict(age: int, stress_score: float,
                     data: List[Dict[str, Tuple[int, float]]]) -> None:
    """Add the age to the corresponding key in the dictionary

    Preconditions:
      - 18 <= age <= 110
      - len(data[0]) == len(constants.DEM_AGE)
      - all(key in constants.DEM_AGE for key in data[0])
    """
    key = constants.DEM_AGE[(age - 15) // 10] if age < 65 else '65+'
    data[0][key] = (data[0][key][0] + 1, data[0][key][1] + stress_score)


def _add_isolation_to_dict(isolation_people: str, dict_index: int, stress_score: float,
                           data: List[Dict[str, Tuple[int, float]]]) -> None:
    """Adds the isolation adults / kids to the corresponding key in the dictionary

    Preconditions:
      - 0 <= isolation_people <= 110
      - dict_index in {9, 10}
      - all(key in constants.DEM_ISOLATION_PEOPLE for key in data[dict_index])
    """
    category = data[dict_index]
    if isolation_people == 'NA':
        category['NA'] = (category['NA'][0] + 1, category['NA'][1] + stress_score)
    else:
        num_dependents = int(isolation_people)
        key = str(num_dependents) if num_dependents < 10 else \
            constants.DEM_ISOLATION_PEOPLE[(num_dependents - 11) // 10 + 11]
        category[key] = (category[key][0] + 1, category[key][1] + stress_score)


def _add_country_to_dict(country: str, stress_score: float,
                         data: List[Dict[str, Tuple[int, float]]]) -> None:
    """Adds the country to the corresponding key in the dictionary

    Preconditions:
      - all(key in constants.COUNTRIES for key in data[4])
    """
    category = data[4]
    if country == {'China', 'Taiwan'}:
        value = category['China']
        category['China'] = (value[0] + 1, value[1] + stress_score)
    elif country == 'Côte dIvoire':  # '' is displayed correctly, don't worry
        value = category['Côte d’Ivoire']
        category['Côte d’Ivoire'] = (value[0] + 1, value[1] + stress_score)
    else:
        if country in category:
            value = category[country]
            category[country] = (value[0] + 1, value[1] + stress_score)


def _add_expat_to_dict(expat: str, stress_score: float,
                       data: List[Dict[str, Tuple[int, float]]]) -> None:
    """Adds the expatriation status to the corresponding key in the dictionary

    Preconditions:
      - all(key in constants.EXPAT for key in data[5])
    """
    category = data[5]
    if expat == 'yes':
        value = category['Yes']
        category['Yes'] = (value[0] + 1, value[1] + stress_score)
    elif expat == 'no':
        value = category['No']
        category['No'] = (value[0] + 1, value[1] + stress_score)


def _add_marital_to_dict(marital_status: str, stress_score: float,
                         data: List[Dict[str, Tuple[int, float]]]) -> None:
    """Adds the marital status to the corresponding key in the dictionary

    Preconditions:
      - all(key in constants.DEM_MARITAL_STATUS for key in data[6])
    """
    category = data[6]
    if marital_status == 'Other or would rather not say':
        value = category['Other/would rather not say']
        category['Other/would rather not say'] = (value[0] + 1, value[1] + stress_score)
    else:
        if marital_status in category:
            value = category[marital_status]
            category[marital_status] = (value[0] + 1, value[1] + stress_score)


def _regulate_na(data: List[Dict[str, Tuple[int, float]]]) -> List[Dict[str, Tuple[int, float]]]:
    """Add the score and population for NA to all other identities in the identity group

    Preconditions:
      - all(list(id_group.keys())[-1] == 'NA' for id_group in data)

    >>> sample_data = [{'id1': (10, 5), 'id2': (14, 29), 'NA': (3, 15)}]
    >>> expected_data = [{'id1': (13, 20), 'id2': (17, 44)}]
    >>> _regulate_na(sample_data) == expected_data
    True
    """
    regulated_data = []

    for i in range(len(data)):
        regulated_data.append({})
        na_population, na_score = data[i]['NA']
        if na_score != 0.0:
            identity_list = list(data[i].keys())[:-1]  # pop 'NA'
            for identity in identity_list:
                regulated_data[i][identity] = (data[i][identity][0] + na_population,
                                               data[i][identity][1] + na_score)
        else:
            regulated_data[i] = {k: data[i][k] for k in list(data[i])[:-1]}  # ignore NA

    return regulated_data


def _calculate_data_average(data: List[Dict[str, Tuple[int, float]]]) -> List[Dict[str, float]]:
    """Calculate the average anxiety score for every identity group in the data.

    Preconditions:
      - all(all(id_group[id][0] > 0 for id in id_group) for id_group in data)

    >>> sample_data = [{'id1_1': (10, 5), 'id1_2': (3, 15)}, {'id2_1': (5, 10), 'id2_2': (15, 3)}]
    >>> expected_data = [{'id1_1': 0.5, 'id1_2': 5.0}, {'id2_1': 2.0, 'id2_2': 0.2}]
    >>> _calculate_data_average(sample_data) == expected_data
    True
    """
    average_data = []

    for i in range(len(data)):
        average_data.append({})
        for identity in data[i]:
            if data[i][identity][0] != 0:
                average_data[i][identity] = data[i][identity][1] / data[i][identity][0]
            else:
                average_data[i][identity] = 0.0

    return average_data


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'csv', 'json', 'os.path', 'constants'],
        'allowed-io': ['read_csv_file', 'process_data', 'load_json_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
