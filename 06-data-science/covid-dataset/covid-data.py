import csv
import os

folder_name = "solution"
file_name = "tobacco_data.txt"


def make_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def get_tobacco_patiens():
    with open('covid-data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        tobacco_patients = []
        for row in csv_reader:
            if row['TOBACCO'] == '1':
                tobacco_patients.append(row)
        return tobacco_patients


def get_median_age(patients):
    ages = []
    for patient in patients:
        ages.append(int(patient['AGE']))
    ages.sort()
    if len(ages) % 2 == 0:
        median_age = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2
    else:
        median_age = ages[len(ages) // 2]
    return median_age


def get_median_age_tobacco_patients():
    tobacco_patients = get_tobacco_patiens()
    median_age = get_median_age(tobacco_patients)
    return median_age


def get_porcent_of_tobacco_patients():
    with open('covid-data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        total_patients = 0
        tobacco_patients = 0
        for row in csv_reader:
            total_patients += 1
            if row['TOBACCO'] == '1':
                tobacco_patients += 1
        return tobacco_patients / total_patients * 100


if __name__ == "__main__":
    make_folder(folder_name)
    porcent = f'{get_porcent_of_tobacco_patients():.2f}'
    median_age = f'{get_median_age_tobacco_patients():.0f}'
    with open(f'{folder_name}/{file_name}', 'w') as file:
        file.write(
            f'{porcent}% of patients are tobacco users and the median age is {median_age} years old')

