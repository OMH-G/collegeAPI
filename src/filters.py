# Imports
import json
import os

# Engineering Colleges Filter
def processing(data,searchfor,present):
    output = []
    for i in range(len(data)):
        stateCheck = data[i][searchfor].replace(" ", '').lower()
        if stateCheck == present:
            output.append(data[i])
    return output

def engineering_colleges_by_state(state):

    with open(os.path.join(os.getcwd(), "data", "allEngineeringColleges.json")) as file:
        data = json.load(file)
    
    return processing(data,'state',state)


def engineering_colleges_by_city(city):

    with open(os.path.join(os.getcwd(), "data", "allEngineeringColleges.json")) as file:
        data = json.load(file)
    return processing(data,'city',city)


# Medical Colleges Filter
def medical_colleges_by_state(state):

    with open(os.path.join(os.getcwd(), "data", "allMedicalColleges.json")) as file:
        data = json.load(file)
    return processing(data,'state',state)


def medical_colleges_by_city(city):

    with open(os.path.join(os.getcwd(), "data", "allMedicalColleges.json")) as file:
        data = json.load(file)
    return processing(data,'city',city)

# Management Colleges Filter
def management_colleges_by_state(state):

    with open(os.path.join(os.getcwd(), "data", "allManagementColleges.json")) as file:
        data = json.load(file)
    return processing(data,'State',state)


def management_colleges_by_city(city):

    with open(os.path.join(os.getcwd(), "data", "allManagementColleges.json")) as file:
        data = json.load(file)
    return processing(data,'City',city)
