# -*- coding: <UTF-8> -*-
"""Your Anxiety During COVID-19: user

Module Description
==================
This file defines the User class -- a class that stores the user's information. It also provides an
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
from typing import Dict, List, Union

import constants


class User:
    """The class storing the user's input

    Instance Attributes:
      - identity: a dictionary of identities, with the key being the name of the identity group, and
                  the value being the actual identity
      - _anxiety_score: the estimated anxiety score, calculated based on the given data

    Representation Invariants:
      - all(key in constants.IDENTITY_GROUP_NAMES for key in self.identity.keys())
      - all(self.identity[list(self.identity.keys())[i]] in
            constants.IDENTITY_GROUP_OPTIONS_LIST[i] for i in range(len(self.identity)))
    """
    # dem_age: Age
    # - int
    #     - 18 - 24
    #     - 25 - 34
    #     - 35 - 44
    #     - 45 - 54
    #     - 55 - 64
    #     - 65+
    #     - NA
    # dem_gender: Gender
    # - str
    #     - Male
    #     - Female
    #     - Other/would rather not say
    #     - NA
    # dem_edu: What best describes your level of education?
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
    # dem_employment: Employment status
    # - str
    #     - Not employed
    #     - Student
    #     - Part time employed
    #     - Full time employed
    #     - Self-employed
    #     - Retired
    #     - NA
    # country: Country of residence
    # - str
    #     - See list_of_countries.txt
    # dem_expat: Are you currently living outside of what you consider your home country?
    # - bool
    #     - NA
    #     - True  (Yes)
    #     - False (No)
    # dem_marital_status: Marital status
    # - str
    #     - Single
    #     - Married/cohabiting
    #     - Divorced/widowed
    #     - Other or would rather not say
    #     - Uninformative response
    #     - NA
    # dem_risk_group: Are you or any of your close relations (family, close friends) in a high-risk
    # group for Coronavirus? (e.g. pregnant, elderly or due to a pre-existing medical condition)
    # - str
    #     - yes
    #     - no
    #     - not sure
    #     - NA
    # dem_isolation: What best describes your current situation?
    # - str
    #     - Life carries on as usual
    #     - Life carries on with minor changes
    #     - Isolated
    #     - Isolated in medical facility of similar location
    #     - NA
    # dem_isolation_adults: If in relative isolation, how many other adults are staying together in
    # the same place as you are?
    # - int
    #     - 0 - 110
    # dem_isolation_kids: If in relative isolation, how many children under the age of 12 are
    # staying together in the same place as you are?
    # - int
    #     - 0 - 110

    identity: Dict[str, str]

    # The estimated anxiety score, calculated based on the given data
    _anxiety_score: float

    def __init__(self, identity: List[Union[int, str]]) -> None:
        """Constructor, initialized the data fields.

        Preconditions:
          - len(identity) == constants.NUMBER_OF_IDENTITIES
        """
        self.identity = {}
        self.set_age(identity[0])
        for i in range(1, 9):
            self.identity[constants.IDENTITY_NAMES[i]] = identity[i]
        self.set_isolation_adults(identity[9])
        self.set_isolation_kids(identity[10])
        self._anxiety_score = 0.0

    def set_age(self, age: int) -> None:
        """Update the age of the user

        Preconditions:
          - 18 <= age <= 110

        >>> user = User([18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10])
        >>> user.identity[constants.IDENTITY_NAMES[0]]
        '18-24'
        >>> user.set_age(45)
        >>> user.identity[constants.IDENTITY_NAMES[0]]
        '45-54'
        >>> user.set_age(44)
        >>> user.identity[constants.IDENTITY_NAMES[0]]
        '35-44'
        >>> user.set_age(95)
        >>> user.identity[constants.IDENTITY_NAMES[0]]
        '65+'
        """
        if age < 65:
            self.identity[constants.IDENTITY_NAMES[0]] = constants.DEM_AGE[(age - 15) // 10]
        else:
            self.identity[constants.IDENTITY_NAMES[0]] = constants.DEM_AGE[-1]

    def set_isolation_adults(self, isolation_adults: int) -> None:
        """Update the Dem_isolation_adults of the user.

        Preconditions:
          - 0 <= isolation_adults <= 110

        >>> user = User([18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10])
        >>> user.identity[constants.IDENTITY_NAMES[9]]
        '10'
        >>> user.set_isolation_adults(30)
        >>> user.identity[constants.IDENTITY_NAMES[9]]
        '21-30'
        """
        if isolation_adults <= 10:
            self.identity[constants.IDENTITY_NAMES[9]] = str(isolation_adults)
        else:
            self.identity[constants.IDENTITY_NAMES[9]] = constants.DEM_ISOLATION_PEOPLE[
                (isolation_adults - 11) // 10 + 11]

    def set_isolation_kids(self, isolation_kids: int) -> None:
        """Update the Dem_isolation_adults of the user.

        Preconditions:
          - 0 <= isolation_adults <= 110

        >>> user = User([18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10])
        >>> user.identity[constants.IDENTITY_NAMES[10]]
        '10'
        >>> user.set_isolation_kids(30)
        >>> user.identity[constants.IDENTITY_NAMES[10]]
        '21-30'
        """
        if isolation_kids <= 10:
            self.identity[constants.IDENTITY_NAMES[10]] = str(isolation_kids)
        else:
            self.identity[constants.IDENTITY_NAMES[10]] = constants.DEM_ISOLATION_PEOPLE[
                (isolation_kids - 11) // 10 + 11]

    def estimate_anxiety_score(self, data: List[Dict[str, float]]) -> None:
        """Calculates the anxiety score of the user from the given data.

        >>> user = User([18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No', \
                        'Single', 'No', 'Life carries on as usual', 10, 10])
        >>> sample_data = [{'18-24': 15}, {'Other/would rather not say': 10}, {'None': 15}, \
                    {'Not employed': 20}, {'Canada': 10}, {'No': 5}, {'Single': 20}, \
                    {'No': 5}, {'Life carries on as usual': 5}, {'10': 25}, {'10': 35} ]
        >>> user.estimate_anxiety_score(sample_data)
        >>> user.get_anxiety_score() == 15
        True
        """
        # ACCUMULATOR: anxiety score
        anxiety = 0

        for i in range(constants.NUMBER_OF_IDENTITIES):
            anxiety = anxiety + data[i][self.identity[constants.IDENTITY_NAMES[i]]]

        self._anxiety_score = anxiety / 11

    def get_anxiety_score(self) -> float:
        """Returns the anxiety score of the user"""
        return self._anxiety_score


def get_user_percentage(user: User, id_group: str, data: List[Dict[str, float]]) -> float:
    """Returns the user's ranking in the population with the selected identity group.

    Preconditions:
      - id_group in constants.IDENTITY_GROUP_NAMES
    """
    id_index = constants.IDENTITY_NAMES.index(id_group)

    lowest_score = 0
    highest_score = 0

    for i in range(len(data)):
        if i != id_index:
            lowest_score = lowest_score + min(data[i].values())
            highest_score = highest_score + max(data[i].values())
        else:
            lowest_score = lowest_score + data[i][user.identity[id_group]]
            highest_score = highest_score + data[i][user.identity[id_group]]

    lowest_score, highest_score = lowest_score / 11, highest_score / 11

    delta_score = highest_score - lowest_score
    delta_user = user.get_anxiety_score() - lowest_score

    return delta_user / delta_score * 100


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'constants'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
