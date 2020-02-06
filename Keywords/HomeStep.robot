*** Settings ***
Library     ../Step/HomeSteps.py

*** Keywords ***
click more to navigate to
    [Arguments]    ${number}
    click more to item      ${number}

close current pointing page
    close page

quit all pages
    restart pages

