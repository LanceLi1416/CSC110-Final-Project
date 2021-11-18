from dataclasses import dataclass


@dataclass
class User:
    """ The class storing the user's input """

    # Age
    # - int
    # - QComboBox
    #     - 18
    #     - ...
    #     - 110
    Dem_age = 0

    # Gender
    # - str
    # - QComboBox
    #     - Male
    #     - Female
    #     - Other/would rather not say
    #     - NA
    Dem_gender = "Other / would rather not say"

    # What best describes your level of education?
    # - str
    # - QComboBox
    #     - None
    #     - Up to 6 years of school
    #     - Up to 9 years of school
    #     - Up to 12 years of school
    #     - Some College, short continuing education or equivalent
    #     - College degree, bachelor, master
    #     - PhD/Doctorate
    #     - Uninformative response
    #     - NA
    Dem_edu = "None"

    # What best describes your mother's level of education?
    # - str
    # - QComboBox
    #     - None
    #     - Up to 6 years of school
    #     - Up to 9 years of school
    #     - Up to 12 years of school
    #     - Some College, short continuing education or equivalent
    #     - College degree, bachelor, master
    #     - PhD/Doctorate
    #     - Uninformative response
    #     - NA
    Dem_edu_mom = "None"

    # Employment status
    # - str
    # - QComboBox
    #     - Not employed
    #     - Student
    #     - Part time employed
    #     - Full time employed
    #     - Self-employed
    #     - Retired
    #     - NA
    Dem_employment = "Not employed"

    # Country of residence
    # - str
    # - QComboBox
    #     - See list_of_countries.txt
    Country = "Afghanistan"

    # Are you currently living outside of what you consider your home country?
    # - bool
    # - QComboBox
    #     - NA
    #     - True  (Yes)
    #     - False (No)
    Dem_Expat = False

    # State / province
    # - str
    # - QLineEdit
    Dem_state = ""

    # Marital statue
    # - str
    # - QComboBox
    #     - Single
    #     - Married/cohabiting
    #     - Divorced/widowed
    #     - Other or would rather not say
    #     - Uninformative response
    #     - NA
    Dem_maritalstatus = "Single"

    # Number dependents (i.e. family members relying on you for support. Usually children)
    # - int
    # - QComboBox
    #     - 0 - 110
    Dem_dependents = 0

    # Are you or any of your close relations (family, close friends) in a high-risk group for
    # Coronavirus? (e.g. pregnant, elderly or due to a pre-existing medical condition)
    # - str
    # - QComboBox
    #     - yes
    #     - no
    #     - not sure
    #     - NA
    Dem_riskgroup = 'no'

    # What best describes your current situation?
    # - str
    # - QComboBox
    #     - Life carries on as usual
    #     - Life carries on with minor changes
    #     - Isolated
    #     - Isolated in medical facility of similar location
    #     - NA
    Dem_islolation = ""

    # If in relative isolation, how many other adults are staying together in the same place as
    # you are?
    # - int
    # - QComboBox
    #     - 0 - 110
    Dem_isolation_adults = 0

    # If in relative isolation, how many children under the age of 12 are staying together in
    # the same place as you are?
    # - int
    # - QComboBox
    #     - 0 - 110
    Dem_isolation_kids = 0
