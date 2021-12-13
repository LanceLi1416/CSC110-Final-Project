# -*- coding: <UTF-8> -*-
"""Your Anxiety During COVID-19: constants

Module Description
==================
This is a constant pool of the project, defining constants that are used universally across the
project, such as the individual identities of each identity group, the colours used for the
graphical user interface and the paths of resources files. RUNNING THIS FILE TAKES NO EFFECT. IT
SHOULD ONLY BE IMPORTED.

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

PLEASE DO NOT MAKE ANY CHANGES TO THIS FILE.
"""
import os
import platform

from PyQt5.QtGui import QColor

# Global constants ---------------------------------------------------------------------------------
TITLE = 'Your Anxiety During COVID-19'
NUMBER_OF_IDENTITIES = 11
IDENTITY_NAMES = ['Age', 'Gender', 'Education', 'Employment Status', 'Country of Residence',
                  'Expatriate', 'Marital status', 'Risk Group', 'Current Situation',
                  'Isolation Adult', 'Isolation Children']

# Options for identity groups ----------------------------------------------------------------------
DEM_AGE = [
    '18-24',
    '25-34',
    '35-44',
    '45-54',
    '55-64',
    '65+'
]

DEM_GENDER = [
    "Male",
    "Female",
    "Other/would rather not say",
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

# COUNTRY = [line.replace('\n', '') for line in open("data/list_of_countries.txt").readlines()]
COUNTRIES = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'The Bahamas', 'Bahrain', 'Bangladesh',
    'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile',
    'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the',
    'Costa Rica', 'Côte d’Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt',
    'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji',
    'Finland', 'France', 'Gabon', 'The Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada',
    'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland',
    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait',
    'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
    'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
    'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Federated States of',
    'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (Burma)',
    'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
    'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea',
    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
    'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
    'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
    'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Sudan, South', 'Suriname', 'Sweden',
    'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
    'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

EXPAT = [
    'Yes',
    'No'
]

DEM_MARITAL_STATUS = [
    'Single',
    'Married/cohabiting',
    'Divorced/widowed',
    'Other/would rather not say'
]

RISK_GROUP = [
    'Yes',
    'No',
    'Not sure'
]

DEM_ISOLATION = [
    'Life carries on as usual',
    'Life carries on with minor changes',
    'Isolated',
    'Isolated in medical facility of similar location'
]

DEM_ISOLATION_PEOPLE = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '11-20',
    '21-30',
    '31-40',
    '41-50',
    '51-60',
    '61-70',
    '71-80',
    '81-90',
    '91-100',
    '101-110'
]

IDENTITY_GROUP_OPTIONS_LIST = [
    DEM_AGE,
    DEM_GENDER,
    DEM_EDU,
    DEM_EMPLOYMENT,
    COUNTRIES,
    EXPAT,
    DEM_MARITAL_STATUS,
    RISK_GROUP,
    DEM_ISOLATION,
    DEM_ISOLATION_PEOPLE,
    DEM_ISOLATION_PEOPLE
]

# File paths ---------------------------------------------------------------------------------------
TEST_DATA_CSV_FILE = os.path.join(os.path.dirname(__file__), 'data/sample_data.csv')
REAL_DATA_CSV_FILE = os.path.join(os.path.dirname(__file__), 'data/COVIDiSTRESS June 17.csv')

TEST_DATA_JSON_FILE = os.path.join(os.path.dirname(__file__), 'data/sample_data.json')
REAL_DATA_JSON_FILE = os.path.join(os.path.dirname(__file__), 'data/real_data.json')

IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'resources/img/')

# Colours ------------------------------------------------------------------------------------------
PLOT_FOREGROUND = QColor(180, 147, 243, 255)
PLOT_BACKGROUND = QColor(255, 255, 255, 255)
FOREGROUND_COLOR = QColor(0, 0, 0, 255)
BACKGROUND_COLOR = QColor(245, 240, 224, 255)

GAUGE_TEXT_COLOR = QColor(0, 0, 0, 255)
GAUGE_NEEDLE_COLOR = QColor(0, 0, 0, 255)
GAUGE_SCALE_TEXT_COLOR = QColor(0, 0, 0, 198)
GAUGE_BIG_SCALE_COLOR = QColor(0, 0, 0, 255)
GAUGE_FINE_SCALE_COLOR = QColor(0, 0, 0, 255)

WHITE = QColor(255, 255, 255, 255)
RED = QColor(205, 86, 75)
YELLOW = QColor(205, 152, 59)
BLUE = QColor(103, 190, 224)

GAUGE_SCALE_POLYGON_GRAD_COLOR = [[.10, RED], [.25, YELLOW], [.50, BLUE]]
GAUGE_CENTER_COVER_GRAD_COLOR = [[0, QColor(35, 40, 3, 255)],
                                 [0.16, QColor(30, 36, 45, 255)],
                                 [0.225, QColor(36, 42, 54, 255)],
                                 [0.423963, QColor(19, 23, 29, 255)],
                                 [0.580645, QColor(45, 53, 68, 255)],
                                 [0.792627, QColor(59, 70, 88, 255)],
                                 [0.935, QColor(30, 35, 45, 255)],
                                 [1, QColor(35, 40, 3, 255)]]
GAUGE_BACKGROUND_GRAD_COLOR = [
    [0, WHITE]
]

# Fonts
TITLE_FONT_PATH = 'resources/fonts/Galgony.ttf'
TITLE_FONT_NAME = 'Galgony'
TITLE_FONT_SIZE = 50 if platform.system() == 'Darwin' else 40
BODY_FONT_PATH = 'resources/fonts/made_tommy/MADE TOMMY Regular_PERSONAL USE.otf'
BODY_FONT_NAME = 'MADE TOMMY'
BODY_FONT_SIZE = 16 if platform.system() == 'Darwin' else 11
GAUGE_FONT_PATH = 'resources/fonts/made_tommy/MADE TOMMY Regular_PERSONAL USE.otf'
GAUGE_FONT_NAME = 'MADE TOMMY'

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'os', 'platform', 'PyQt5.QtGui'],
        'allowed-io': [],
        'max-line-length': 100,
        # 'disable': ['R1705', 'C0200']
        # E0611 (no-name-in-module): python_ta fails to find PyQt5 modules even if they exist
        'disable': ['R1705', 'C0200', 'E0611']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
