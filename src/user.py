from typing import Dict, List

import src.constants as constants


class User:
    """ The class storing the user's input """
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
                 isolation_kids: int):
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

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'no', \
                        'Single', 'no', 'Life carries on as usual', 10, 10)
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

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'no', \
                        'Single', 'no', 'Life carries on as usual', 10, 10)
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

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'no', \
                        'Single', 'no', 'Life carries on as usual', 10, 10)
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

    def estimate_anxiety_score(self, data: List[Dict[str, float]]) -> float:
        """Calculates the anxiety score of the user from the given data.

        >>> user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'no', \
                        'Single', 'no', 'Life carries on as usual', 10, 10)
        >>> data = [{'18-24': 15}, {'Other/would rather not say': 10}, {'None': 15}, \
                    {'Not employed': 20}, {'Canada': 10}, {'no': 5}, {'Single': 20}, \
                    {'no': 5}, {'Life carries on as usual': 5}, {10: 25}, {10: 35} ]
        >>> user.estimate_anxiety_score(data) == 15
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
        return self._anxiety_score

    def get_anxiety_score(self) -> float:
        """Returns the anxiety score of the user"""
        return self._anxiety_score


def get_user_percentage(user: User, id_group: str, data: List[Dict[str, float]]) -> float:
    """Returns the user's position in the population with the selected id group. """
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
