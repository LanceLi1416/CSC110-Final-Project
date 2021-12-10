""" The file storing all the constants """
from enum import Enum


# Identity group indexing in processed list---------------------------------------------------------
class Identities(Enum):
    AGE = 0,
    GENDER = 1,
    EDU = 2,
    EMPLOYMENT = 3,
    COUNTRY = 4,
    EXPAT = 5,
    MARITAL_STATUS = 6,
    RISK_GROUP = 7,
    ISOLATION = 8,
    ISOLATION_ADULTS = 9,
    ISOLATION_KIDS = 10


# Options for identity groups ----------------------------------------------------------------------
BINARY = [
    'Yes',
    'No'
]

TERNARY = [
    'Yes',
    'No',
    'Not sure'
]

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
    'PhD / Doctorate'
]

DEM_EMPLOYMENT = [
    'Not employed',
    'Student',
    'Part time employed',
    'Full time employed',
    'Self-employed',
    'Retired'
]

DEM_MARITALSTATUS = [
    'Single',
    'Married/cohabiting',
    'Divorced/widowed',
    'Other/would rather not say'
]

DEM_ISLOLATION = [
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

# COUNTRY = [line.replace('\n', '') for line in open("data/list_of_countries.txt").readlines()]
COUNTRIES = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'The Bahamas', 'Bahrain',
             'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
             'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
             'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic',
             'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the',
             'Congo, Republic of the', 'Costa Rica', 'Côte d’Ivoire', 'Croatia', 'Cuba', 'Cyprus',
             'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
             'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
             'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon',
             'The Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala',
             'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland',
             'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
             'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo',
             'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
             'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia',
             'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
             'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
             'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
             'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman',
             'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
             'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
             'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
             'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
             'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
             'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Sudan, South', 'Suriname', 'Sweden',
             'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo',
             'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu',
             'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
             'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen',
             'Zambia', 'Zimbabwe'
             ]

TEST_DATA_CSV_FILE = 'data/sample_data.csv'
REAL_DATA_CSV_FILE = 'data/COVIDiSTRESS June 17.csv'

TEST_DATA_JSON_FILE = 'data/sample_data.json'
READ_DATA_JSON_FILE = 'data/read_data.json'
