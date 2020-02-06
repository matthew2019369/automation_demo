*** Settings ***
Library     ../Config/ConfigReader.py

*** Keywords ***
get username
    ${name}        get name
    [Return]    ${name}

get pass
    ${password}     get password
    [Return]    ${password}

get website
    ${url}      get url
    [Return]    ${url}


