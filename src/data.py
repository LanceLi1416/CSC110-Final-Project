""" The file to save and extract data from the dataset """
import csv


def calc_stress_score(person: list) -> int:
    """Return stress score from a row of the dataset"""
    # Value added for each response in the survey
    reg_row = [-2, -1, 0, 1, 2]
    # Depending on the nature of the question we may want to reduce or increase the stress score
    stress_method = [1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
                     1, 1, 1, 1, -1, -1, 0, 0, 1, -1, 1, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0,
                     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1]

    # Tuple Consists of:
    # First element is the scale that all the questions in a category are measured upon
    # Second element is number of questions within the same category
    category_tuples = [(5, 10), (5, 3), (11, 2), (11, 6), (6, 5), (12, 1),
                    (6, 6), (6, 15), (6, 25), (6, 10), (6, 15), (6, 6)]
    # List of values from dataset of survey used for calculations
    answer_values = person[21:54] + person[70:143]
    # ACCUMULATOR stress_so_far: running sum of stress score
    stress_so_far = 0
    # ACCUMULATOR index: running index
    absolute_index = 0

    for scale_tuple in category_tuples:
        answer_val = int(answer_values[absolute_index])
        if answer_val != 'NA' and answer_val != '99':

            interval = 1 / len(reg_row)
            answer_decimal = answer_val / scale_tuple[0]

            answer_index = int(answer_decimal // interval)
            stress_so_far += reg_row[answer_index]

    return stress_so_far

    # for survey in survey_scale:
    #     for _ in range(survey[1] - 1):
    #         if answer_values[index] != 'NA' and answer_values[index] != '99':
    #             print(answer_values[index], survey[0])
    #             print(int(((int(answer_values[index]) / survey[0]) * 100) // 20))
    #             stress += reg_row[int(((int(answer_values[index]) / survey[0]) * 100) // 20) - 1] \
    #                       * stress_method[index]
    #         index += 1
    # return stress


def process_country() -> dict[str, tuple[int, int]]:
    """Return country values for data_dict"""
    countries_dict = {}
    with open('../data/list_of_countries.txt') as file_2:
        for country in file_2:
            countries_dict[country] = (0, 0)
    return countries_dict


def initialize_data_list() -> list[dict[str, tuple[int, int]]]:
    """Return initialized values"""
    countries = process_country()
    data_start = [
        # Initialize age
        {'18-24': (0, 0),
         '25-34': (0, 0),
         '35-44': (0, 0),
         '45-54': (0, 0),
         '55-64': (0, 0),
         '65+': (0, 0),
         'NA': (0, 0)},
        # Initialize gender
        {'Male': (0, 0),
         'Female': (0, 0),
         'Other': (0, 0),
         'NA': (0, 0)},
        # Initialize education
        {'None': (0, 0),
         'Up to 6 years of school': (0, 0),
         'Up to 9 years of school': (0, 0),
         'Up to 12 years of school': (0, 0),
         'Some College, short continuing education or equivalent': (0, 0),
         'College degree, bachelor, master': (0, 0),
         'PhD/Doctorate': (0, 0),
         'Uninformative response': (0, 0),
         'NA': (0, 0)},
        # Initialize employment status
        {'Not employed': (0, 0),
         'Student': (0, 0),
         'Part time employed': (0, 0),
         'Full time employed': (0, 0),
         'Self-employed': (0, 0),
         'Retired': (0, 0),
         'NA': (0, 0)
         },
        # Initialize country of residence
        countries,
        # Initialize whether they are an expatriate
        {'yes': (0, 0),
         'no': (0, 0),
         'NA': (0, 0)
         },
        # Initialize marital status
        {'Single': (0, 0),
         'Married/cohabiting': (0, 0),
         'Divorced/widowed': (0, 0),
         'Other or would rather not say': (0, 0),
         'Uninformative response': (0, 0),
         'NA': (0, 0)},
        # Initialize whether they reside in a high risk group
        {'yes': (0, 0),
         'no': (0, 0),
         'not sure': (0, 0),
         'NA': (0, 0)},
        # Initialize isolation status
        {'Life carries on as usual': (0, 0),
         'Life carries on with minor changes': (0, 0),
         'Isolated': (0, 0),
         'Isolated in medical facility of similar location': (0, 0),
         'NA': (0, 0)},
        # Initialize adults isolated with participant
        {'0': (0, 0),
         '1': (0, 0),
         '2': (0, 0),
         '3': (0, 0),
         '4': (0, 0),
         '5': (0, 0),
         '6': (0, 0),
         '7': (0, 0),
         '8': (0, 0),
         '9': (0, 0),
         '10': (0, 0),
         '11-20': (0, 0),
         '21-30': (0, 0),
         '31-40': (0, 0),
         '41-50': (0, 0),
         '51-60': (0, 0),
         '61-70': (0, 0),
         '71-80': (0, 0),
         '81-90': (0, 0),
         '91-100': (0, 0),
         '101-110': (0, 0),
         'NA': (0, 0)},
        # Initialize children isolated with participant
        {'0': (0, 0),
         '1': (0, 0),
         '2': (0, 0),
         '3': (0, 0),
         '4': (0, 0),
         '5': (0, 0),
         '6': (0, 0),
         '7': (0, 0),
         '8': (0, 0),
         '9': (0, 0),
         '10': (0, 0),
         '11-20': (0, 0),
         '21-30': (0, 0),
         '31-40': (0, 0),
         '41-50': (0, 0),
         '51-60': (0, 0),
         '61-70': (0, 0),
         '71-80': (0, 0),
         '81-90': (0, 0),
         '91-100': (0, 0),
         '101-110': (0, 0),
         'NA': (0, 0)}]
    return data_start


def read_csv_file() -> list[dict[str, tuple[int, int]]]:
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
    the first being the total stress_score that has been added to them,
    and the second being the population (or number of people) that have added their score to it
    """
    # ACCUMULATOR data_processed_so_far: the running list of
    data_processed_so_far = initialize_data_list()

    with open("../data/COVIDiSTRESS June 17.csv") as file:
        reader = csv.reader(file)

        # This line reads the first row of the csv file, which contains the headers.
        # The result is a list of strings.
        header = next(reader)

        # This list comprehension reads each remaining row of the file,
        # where each row is represented as a list of strings.
        # The header row is *not* included in this list.
        for row in reader:
            # Collect all attributes of each row (participant)
            stress_score = calc_stress_score(row)
            # Update the data dictionary
            for i in range(len(data_processed_so_far)):
                category = data_processed_so_far[i]
                index = i + 4

                if i == 0:
                    age = int(row[index])
                    # age_range_tuple = category[row[index]]

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
                    else:
                        category['NA'] = (category['NA'][0] + 1, category['NA'][1] + stress_score)

                elif i == 9 or i == 10:
                    num_dependents = int(row[index])
                    num_dependents_tuple = category[row[index]]

                    if num_dependents == 0:
                        category['0'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    if num_dependents == 1:
                        category['1'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 2:
                        category['2'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 3:
                        category['3'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 4:
                        category['4'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 5:
                        category['5'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 6:
                        category['6'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 7:
                        category['7'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 9:
                        category['9'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif num_dependents == 10:
                        category['10'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 11 <= num_dependents <= 20:
                        category['11-20'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 21 <= num_dependents <= 30:
                        category['21-30'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 31 <= num_dependents <= 40:
                        category['31-40'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 41 <= num_dependents <= 50:
                        category['41-50'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 51 <= num_dependents <= 60:
                        category['51-60'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 61 <= num_dependents <= 70:
                        category['61-70'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 71 <= num_dependents <= 80:
                        category['71-80'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 81 <= num_dependents <= 90:
                        category['81-90'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 91 <= num_dependents <= 100:
                        category['91-100'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    elif 101 <= num_dependents <= 110:
                        category['101-110'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                    else:
                        category['NA'] = (num_dependents_tuple[0] + 1, num_dependents_tuple[1] + stress_score)
                else:
                    print(i, category, row[index], data_processed_so_far[i])
                    value = category[row[index]]
                    category[row[index]] = (value[0] + 1, value[1] + stress_score)

    return data_processed_so_far
