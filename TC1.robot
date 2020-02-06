*** Settings ***
Library         SeleniumLibrary
Resource    ./Keywords/Login.robot
Resource    ./Keywords/HomeStep.robot
Resource    ./Keywords/GetConfig.robot
Test Teardown    quit all pages

*** Test Cases ***
Navigate to 1
    [Tags]    odd
    ${LOGIN URL}=   get url
    ${NAME}     get username
    ${PASSWORD}     get pass
    ${ItemNumber}   BuiltIn.evaluate    2
    Navigate to     ${LOGIN URL}
    Login to      ${NAME}     ${PASSWORD}
    Navigate to home
    click more to navigate to       ${ItemNumber}
    sleep    5s

Navigate to 2
    [Tags]    even      prime
    ${LOGIN URL}=   get url
    ${NAME}     get username
    ${PASSWORD}     get pass
    ${ItemNumber}   BuiltIn.evaluate    2
    Navigate to     ${LOGIN URL}
    Login to      ${NAME}     ${PASSWORD}
    Navigate to home
    click more to navigate to       ${ItemNumber}
    sleep    5s

Navigate to 3
    [Tags]    odd       prime
    ${LOGIN URL}=   get url
    ${NAME}     get username
    ${PASSWORD}     get pass
    ${ItemNumber}   BuiltIn.evaluate    2
    Navigate to     ${LOGIN URL}
    Login to      ${NAME}     ${PASSWORD}
    Navigate to home
    click more to navigate to       ${ItemNumber}
    sleep    5s

Navigate to 4
    [Tags]    even      composite
    ${LOGIN URL}=   get url
    ${NAME}     get username
    ${PASSWORD}     get pass
    ${ItemNumber}   BuiltIn.evaluate    2
    Navigate to     ${LOGIN URL}
    Login to      ${NAME}     ${PASSWORD}
    Navigate to home
    click more to navigate to       ${ItemNumber}
    sleep    5s

Navigate to 5
    [Tags]    odd       prime
    ${LOGIN URL}=   get url
    ${NAME}     get username
    ${PASSWORD}     get pass
    ${ItemNumber}   BuiltIn.evaluate    2
    Navigate to     ${LOGIN URL}
    Login to      ${NAME}     ${PASSWORD}
    Navigate to home
    click more to navigate to       ${ItemNumber}
    sleep    5s