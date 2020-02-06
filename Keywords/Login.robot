*** Settings ***
Library     ../Step/LoginSteps.py

*** Keywords ***
Navigate to
    [Arguments]     ${Url}
    Navigate        ${Url}

Navigate to home
    navigate to homepage

Login to
    [Arguments]    ${Username}      ${Password}
    login    ${Username}        ${Password}
