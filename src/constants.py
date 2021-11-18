""" The file storing all the constants """

BINARY = [
    'Yes',
    'No'
]

DEM_GENDER = [
    "Male",
    "Female",
    "Other / would rather not say",
]

DEM_EDU = [
    'None',
    'Up to 6 years of school',
    'Up to 9 years of school',
    'Up to 12 years of school',
    'Some College, short continuing education or equivalent',
    'College degree, bachelor, master',
    'PhD/Doctorate'
]

DEM_EMPLOYMENT = [
    'Not employed',
    'Student',
    'Part time employed',
    'Full time employed',
    'Self-employed',
    'Retired'
]

COUNTRY = [line.replace('\n', '') for line in open("data/list_of_countries.txt").readlines()]
