# -*- coding: <UTF-8> -*-
"""Your Anxiety During COVID-19: user

Module Description
==================
this file defines the User class -- a class that stores the user's information. It also provides an
interface for calculating the user's ranking in a specific identity group.

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
from typing import Dict, List

from src import constants


# TODO: pacify python_ta by changing all of the instance attributes into a big big list
class User:
    """ The class storing the user's input

    Instance Attributes:
      - dem_age: the user's age group
      - dem_gender: the user's gender
      - dem_edu: the user's education level
      - dem_employment: the user's employment status
      - country: the user's country of residence
      - dem_expat: whether the user is currently living outside what they consider home country
      - dem_marital_status: the user's marital status
      - dem_risk_group: whether the user or any of close relations (family, close friends) are in a
                        high-risk group for Coronavirus
      - dem_isolation: the user's current isolation situation
      - dem_isolation_adults: the number of adults staying together  in the same place as the user
      - dem_isolation_kids: the number of children under the age of 12 staying together in the same
                            place as the user
      - _anxiety_score = the estimated anxiety score, calculated based on the given data

    Representation Invariants:
      - self.dem_age in constants.DEM_AGE
      - self.dem_gender in constants.DEM_GENDER
      - self.dem_edu in constants.DEM_EDU
      - self.dem_employment in constants.DEM_EMPLOYMENT
      - self.country in constants.COUNTRIES
      - self.dem_expat in constants.EXPAT
      - self.dem_marital_status in constants.DEM_MARITAL_STATUS
      - self.dem_risk_group in constants.RISK_GROUP
      - self.dem_isolation in constants.DEM_ISOLATION
      - self.dem_isolation_adults in constants.DEM_ISOLATION_PEOPLE
      - self.dem_isolation_kids in constants.DEM_ISOLATION_PEOPLE
    """
    # Age
    # - int
    #     - 18 - 24
    #     - 25 - 34
    #     - 35 - 44
    #     - 45 - 54
    #     - 55 - 64
    #     - 65+
    #     - NA
    dem_age: str
    # Gender
    # - str
    #     - Male
    #     - Female
    #     - Other/would rather not say
    #     - NA
    dem_gender: str
    # What best describes your level of education?
    # - str
    #     - None
    #     - Up to 6 years of school
    #     - Up to 9 years of school
    #     - Up to 12 years of school
    #     - Some College, short continuing education or equivalent
    #     - College degree, bachelor, master
    #     - PhD/Doctorate
    #     - Uninformative response
    #     - NA
    dem_edu: str
    # Employment status
    # - str
    #     - Not employed
    #     - Student
    #     - Part time employed
    #     - Full time employed
    #     - Self-employed
    #     - Retired
    #     - NA
    dem_employment: str
    # Country of residence
    # - str
    #     - See list_of_countries.txt
    country: str
    # Are you currently living outside of what you consider your home country?
    # - bool
    #     - NA
    #     - True  (Yes)
    #     - False (No)
    dem_expat: str
    # Marital status
    # - str
    #     - Single
    #     - Married/cohabiting
    #     - Divorced/widowed
    #     - Other or would rather not say
    #     - Uninformative response
    #     - NA
    dem_marital_status: str
    # Are you or any of your close relations (family, close friends) in a high-risk group for
    # Coronavirus? (e.g. pregnant, elderly or due to a pre-existing medical condition)
    # - str
    #     - yes
    #     - no
    #     - not sure
    #     - NA
    dem_risk_group: str
    # What best describes your current situation?
    # - str
    #     - Life carries on as usual
    #     - Life carries on with minor changes
    #     - Isolated
    #     - Isolated in medical facility of similar location
    #     - NA
    dem_isolation: str
    # If in relative isolation, how many other adults are staying together in the same place as you
    # are?
    # - int
    #     - 0 - 110
    dem_isolation_adults: str
    # If in relative isolation, how many children under the age of 12 are staying together in the
    # same place as you are?
    # - int
    #     - 0 - 110
    dem_isolation_kids: str

    # The estimated anxiety score, calculated based on the given data
    _anxiety_score: float

    def __init__(self, age: int, gender: str, edu: str, employment: str, country: str, expat: str,
                 marital_status: str, risk_group: str, isolation: str, isolation_adults: int,
                 isolation_kids: int) -> None:
        self.set_age(age)
        self.dem_gender = gender
        self.dem_edu = edu
        self.dem_employment = employment
        self.country = country
        self.dem_expat = expat
        self.dem_marital_status = marital_status
        self.dem_risk_group = risk_group
        self.dem_isolation = isolation
        self.set_isolation_adults(isolation_adults)
        self.set_isolation_kids(isolation_kids)
        self._anxiety_score = -100.0

    def set_age(self, age: int) -> None:
        """Update the age of the user

        Preconditions:
          - 18 <= age <= 110

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10)
        >>> user.dem_age
        '18-24'
        >>> user.set_age(45)
        >>> user.dem_age
        '45-54'
        >>> user.set_age(44)
        >>> user.dem_age
        '35-44'
        >>> user.set_age(95)
        >>> user.dem_age
        '65+'
        """
        if age < 65:
            self.dem_age = constants.DEM_AGE[(age - 15) // 10]
        else:
            self.dem_age = constants.DEM_AGE[-1]

    def set_isolation_adults(self, isolation_adults: int) -> None:
        """Update the Dem_isolation_adults of the user.

        Preconditions:
          - 0 <= isolation_adults <= 110

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10)
        >>> user.dem_isolation_adults
        '10'
        >>> user.set_isolation_adults(30)
        >>> user.dem_isolation_adults
        '21-30'
        """
        if isolation_adults <= 10:
            self.dem_isolation_adults = str(isolation_adults)
        else:
            self.dem_isolation_adults = constants.DEM_ISOLATION_PEOPLE[
                (isolation_adults - 11) // 10 + 11]

    def set_isolation_kids(self, isolation_kids: int) -> None:
        """Update the Dem_isolation_adults of the user.

        Preconditions:
          - 0 <= isolation_adults <= 110

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10)
        >>> user.dem_isolation_kids
        '10'
        >>> user.set_isolation_kids(30)
        >>> user.dem_isolation_kids
        '21-30'
        """
        if isolation_kids <= 10:
            self.dem_isolation_kids = str(isolation_kids)
        else:
            self.dem_isolation_kids = constants.DEM_ISOLATION_PEOPLE[
                (isolation_kids - 11) // 10 + 11]

    def estimate_anxiety_score(self, data: List[Dict[str, float]]) -> None:
        """Calculates the anxiety score of the user from the given data.

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10)
        >>> sample_data = [{'18-24': 15}, {'Other/would rather not say': 10}, {'None': 15}, \
                    {'Not employed': 20}, {'Canada': 10}, {'No': 5}, {'Single': 20}, \
                    {'No': 5}, {'Life carries on as usual': 5}, {'10': 25}, {'10': 35} ]
        >>> user.estimate_anxiety_score(sample_data)
        >>> user.get_anxiety_score() == 15
        True
        """
        self._anxiety_score = (data[0][self.dem_age] +
                               data[1][self.dem_gender] +
                               data[2][self.dem_edu] +
                               data[3][self.dem_employment] +
                               data[4][self.country] +
                               data[5][self.dem_expat] +
                               data[6][self.dem_marital_status] +
                               data[7][self.dem_risk_group] +
                               data[8][self.dem_isolation] +
                               data[9][self.dem_isolation_adults] +
                               data[10][self.dem_isolation_kids]
                               ) / 11

    def get_anxiety_score(self) -> float:
        """Returns the anxiety score of the user"""
        return self._anxiety_score


def get_user_percentage(user: User, id_group: str, data: List[Dict[str, float]]) -> float:
    """Returns the user's ranking in the population with the selected identity group.

    Preconditions:
      - id_group in constants.IDENTITY_GROUP_NAMES
    """
    id_index = constants.IDENTITY_GROUP_NAMES.index(id_group)

    lowest_score = 0
    highest_score = 0

    for i in range(len(data)):
        if i != id_index:
            # print(id_group, constants.IDENTITY_GROUP_OPTIONS_LIST[i])
            lowest_score = lowest_score + min(data[i].values())
            highest_score = highest_score + max(data[i].values())
        else:
            if id_group == 'Age':
                attr = user.dem_age
            elif id_group == 'Gender':
                attr = user.dem_gender
            elif id_group == 'Education':
                attr = user.dem_edu
            elif id_group == 'Employment Status':
                attr = user.dem_employment
            elif id_group == 'Country of Residence':
                attr = user.country
            elif id_group == 'Expatriate':
                attr = user.dem_expat
            elif id_group == 'Marital status':
                attr = user.dem_marital_status
            elif id_group == 'Risk Group':
                attr = user.dem_risk_group
            elif id_group == 'Current Situation':
                attr = user.dem_isolation
            elif id_group == 'Isolation Adult':
                attr = user.dem_isolation_adults
            elif id_group == 'Isolation Children':
                attr = user.dem_isolation_kids
            else:
                attr = 0

            lowest_score = lowest_score + data[i][attr]
            highest_score = highest_score + data[i][attr]

    lowest_score, highest_score = lowest_score / 11, highest_score / 11

    delta_score = highest_score - lowest_score
    delta_user = user.get_anxiety_score() - lowest_score

    return delta_user / delta_score * 100


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['src'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
