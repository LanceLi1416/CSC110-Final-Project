""" The file storing all the constants """
from enum import Enum
from PyQt5.QtGui import QColor

# Global constants ---------------------------------------------------------------------------------
NUMBER_OF_IDENTITIES = 11
IDENTITY_GROUP_NAMES = ['Age', 'Gender', 'Education', 'Employment Status', 'Country of Residence',
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
    'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
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
TEST_DATA_CSV_FILE = 'data/sample_data.csv'
REAL_DATA_CSV_FILE = 'data/COVIDiSTRESS June 17.csv'

TEST_DATA_JSON_FILE = 'data/sample_data.json'
REAL_DATA_JSON_FILE = 'data/real_data.json'

# Colours ------------------------------------------------------------------------------------------
PLOT_COLOR = QColor(198, 198, 198, 255)

GAUGE_TEXT_COLOR = QColor(255, 255, 255, 255)
GAUGE_SCALE_TEXT_COLOR = QColor(198, 198, 198, 198)
GAUGE_BIG_SCALE_COLOR = QColor(0, 0, 0, 255)
GAUGE_FINE_SCALE_COLOR = QColor(0, 0, 0, 255)

# Fonts
GAUGE_FONT_PATH = 'fonts/Orbitron/Orbitron-VariableFont_wght.ttf'
GAUGE_FONT_NAME = 'Orbitron'
