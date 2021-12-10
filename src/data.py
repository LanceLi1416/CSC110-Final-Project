""" The file to save and extract data from the dataset """
import csv
import json

from typing import Dict, List, Tuple

import src.constants as constants

REAL_DATA = "../data/COVIDiSTRESS June 17.csv"
TEST_DATA = "../data/sample_data.csv"


def calc_stress_score(person: List[str]) -> float:
    """Return stress score from a row of the dataset"""
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
                bounded_answer = ((int(og_answer) - 1) * (4 / (scale_tuple[0] - 1))) - 2
                stress_so_far += bounded_answer * stress_method[absolute_index]
                # print(f'og: {og_answer}, bounded: {bounded_answer}, scale: {scale_tuple[0]}')
            absolute_index += 1
    return stress_so_far


def initialize_data_list() -> List[Dict[str, Tuple[int, float]]]:
    """Return initialized values"""
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


def read_csv_file(file_name: str, file_encoding='ISO-8859-1') -> List[Dict[str, Tuple[int, float]]]:
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
    """
    # ACCUMULATOR data_processed_so_far: the running list of
    data_processed_so_far = initialize_data_list()

    file = open(file_name, encoding=file_encoding)
    reader = csv.reader(file)

    # This line reads the first row of the csv file, which contains the headers.
    # The result is a list of strings.
    _ = next(reader)
    # This list comprehension reads each remaining row of the file,
    # where each row is represented as a list of strings.
    # The header row is *not* included in this list.
    for row in reader:
        stress_score = calc_stress_score(row)

        csv_index = 4
        category = data_processed_so_far[csv_index - 4]
        age = int(row[csv_index])
        if 18 <= age <= 24:
            category['18-24'] = (category['18-24'][0] + 1, category['18-24'][1] + stress_score)
        elif 25 <= age <= 34:
            category['25-34'] = (category['25-34'][0] + 1, category['25-34'][1] + stress_score)
        elif 35 <= age <= 44:
            category['35-44'] = (category['35-44'][0] + 1, category['35-44'][1] + stress_score)
        elif 45 <= age <= 54:
            category['45-54'] = (category['45-54'][0] + 1, category['45-54'][1] + stress_score)
        elif 55 <= age <= 64:
            category['55-64'] = (category['55-64'][0] + 1, category['55-64'][1] + stress_score)
        elif 65 <= age:
            category['65+'] = (category['65+'][0] + 1, category['65+'][1] + stress_score)

        for csv_index in range(16, 18):
            category = data_processed_so_far[csv_index - 7]
            if row[csv_index] == 'NA':
                category['NA'] = (category['NA'][0] + 1, category['NA'][1] + stress_score)
                break
            num_dependents = int(row[csv_index])
            if num_dependents == 0:
                category['0'] = (category['0'][0] + 1, category['0'][1] + stress_score)
            elif num_dependents == 1:
                category['1'] = (category['1'][0] + 1, category['1'][1] + stress_score)
            elif num_dependents == 2:
                category['2'] = (category['2'][0] + 1, category['2'][1] + stress_score)
            elif num_dependents == 3:
                category['3'] = (category['3'][0] + 1, category['3'][1] + stress_score)
            elif num_dependents == 4:
                category['4'] = (category['4'][0] + 1, category['4'][1] + stress_score)
            elif num_dependents == 5:
                category['5'] = (category['5'][0] + 1, category['5'][1] + stress_score)
            elif num_dependents == 6:
                category['6'] = (category['6'][0] + 1, category['6'][1] + stress_score)
            elif num_dependents == 7:
                category['7'] = (category['7'][0] + 1, category['7'][1] + stress_score)
            elif num_dependents == 9:
                category['9'] = (category['9'][0] + 1, category['9'][1] + stress_score)
            elif num_dependents == 10:
                category['10'] = (category['10'][0] + 1, category['10'][1] + stress_score)
            elif 11 <= num_dependents <= 20:
                category['11-20'] = (category['11-20'][0] + 1, category['11-20'][1] + stress_score)
            elif 21 <= num_dependents <= 30:
                category['21-30'] = (category['21-30'][0] + 1, category['21-30'][1] + stress_score)
            elif 31 <= num_dependents <= 40:
                category['31-40'] = (category['31-40'][0] + 1, category['31-40'][1] + stress_score)
            elif 41 <= num_dependents <= 50:
                category['41-50'] = (category['41-50'][0] + 1, category['41-50'][1] + stress_score)
            elif 51 <= num_dependents <= 60:
                category['51-60'] = (category['51-60'][0] + 1, category['51-60'][1] + stress_score)
            elif 61 <= num_dependents <= 70:
                category['61-70'] = (category['61-70'][0] + 1, category['61-70'][1] + stress_score)
            elif 71 <= num_dependents <= 80:
                category['71-80'] = (category['71-80'][0] + 1, category['71-80'][1] + stress_score)
            elif 81 <= num_dependents <= 90:
                category['81-90'] = (category['81-90'][0] + 1, category['81-90'][1] + stress_score)
            elif 91 <= num_dependents <= 100:
                category['91-100'] = (
                    category['91-100'][0] + 1, category['91-100'][1] + stress_score)
            elif 101 <= num_dependents <= 110:
                category['101-110'] = (
                    category['101-110'][0] + 1, category['101-110'][1] + stress_score)

        remaining_columns = [5, 6, 8, 9, 10, 12, 14, 15]
        for csv_index in remaining_columns:
            category = data_processed_so_far[remaining_columns.index(csv_index) + 1]

            if row[csv_index] == 'NA':
                category['NA'] = (category['NA'][0] + 1, category['NA'][1] + stress_score)
            elif 'would rather not say' in row[csv_index].lower():
                if 'Other/would rather not say' not in category:
                    category['Other/would rather not say'] = (0, 0)
                category['Other/would rather not say'] = (
                    category['Other/would rather not say'][0] + 1,
                    category['Other/would rather not say'][1] + stress_score
                )
            elif row[csv_index] not in category:
                continue
            else:
                value = category[row[csv_index]]
                category[row[csv_index]] = (value[0] + 1, value[1] + stress_score)
    return data_processed_so_far


def regulate_na(data: List[Dict[str, Tuple[int, float]]]) -> List[Dict[str, Tuple[int, float]]]:
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
            # regulated_data[i] = data[i]
            regulated_data[i] = {k: data[i][k] for k in list(data[i])[:-1]}

    return regulated_data


def calculate_data_average(data: List[Dict[str, Tuple[int, float]]]) -> List[Dict[str, float]]:
    average_data = []

    for i in range(len(data)):
        average_data.append({})
        for identity in data[i]:
            if data[i][identity][0] != 0:
                average_data[i][identity] = data[i][identity][1] / data[i][identity][0]
            else:
                average_data[i][identity] = 0.0

    return average_data


def process_data(input_file_name: str, output_file_name: str,
                 input_encoding='ISO-8859-1', output_encoding='utf-8') -> None:
    """Process the data, then store it in a json file for future reference"""
    data = calculate_data_average(regulate_na(read_csv_file(input_file_name, input_encoding)))
    with open(output_file_name, 'w', encoding=output_encoding) as json_file:
        json.dump(data, json_file)


def load_json_data(file_name: str, file_encoding='utf-8') -> List[Dict[str, float]]:
    with open(file_name, 'r', encoding=file_encoding) as json_file:
        data = json.load(json_file)
    return data


def calculate_extrema(data: List[Dict[str, float]]) -> Tuple[float, float]:
    min_so_far, max_so_far = 0, 0

    for identity_group in data:
        min_so_far = min_so_far + min(identity_group.values())
        max_so_far = max_so_far + max(identity_group.values())

    return min_so_far / 11, max_so_far / 11
