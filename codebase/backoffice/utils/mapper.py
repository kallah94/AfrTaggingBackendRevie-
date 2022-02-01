"""
Mapper for data from excel sheet
this help to take right input from right row and cell
"""
from dataclasses import dataclass

# Team
TEAM_NAME = 1

# Player and Staff fields columns position
FIRST_NAME = 0
LAST_NAME = 1
AGE = 2
ROLE = 4
NUMBER = 5  # only available for players

# Contract
BEGIN_CONTRACT = 6
END_CONTRACT = 7
STATUS_CONTRACT = 8
STATUS_CONTRACT = 8

# Country for player and staff
COUNTRY = 3



@dataclass
class CountryTemplate:
    country: int = COUNTRY


@dataclass
class PlayerTemplate:
    first_name: int = FIRST_NAME
    last_name: int = LAST_NAME
    age: int = AGE
    country: int = COUNTRY
    role: int = ROLE
    number: int = NUMBER


@dataclass
class StaffTemplate:
    first_name: int = FIRST_NAME
    last_name: int = LAST_NAME
    age: int = AGE
    country: int = COUNTRY
    role: int = ROLE


@dataclass
class ContractTemplate:
    begin_contract: int = BEGIN_CONTRACT
    end_contract: int = END_CONTRACT
    status_contract: int = STATUS_CONTRACT


@dataclass
class TeamTemplate:
    team_name: int = TEAM_NAME
