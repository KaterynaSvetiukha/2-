import csv
import os

flag = False

try:
    with open("лаба 11.csv","r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ",")
        print("Country Name: 2015 [YR2015]")

        for row in reader:
            print(row['Country Name'], ': ', row["2015 [YR2015]"])

except FileNotFoundError:
    print("Файл лаба 11.csv не знайдено!")

try:
    csvfile = open("лаба 11.csv","r")
    reader = csv.DictReader(csvfile, delimiter = ",")

    max_value = None
    min_value = None
    max_country = ""
    min_country = ""

    for row in reader:
            try:
                value = int(row["2015 [YR2015]"])

                if max_value is None or value > max_value:
                    max_value = value
                    max_country = row["Country Name"]

                if min_value is None or value < min_value:
                    min_value = value
                    min_country = row["Country Name"]
            except:
                continue

            print(f"Max value = {max_value} in {max_country}")
            print(f"Min value = {min_value} in {min_country}")

            with open("new_lab11.csv","w", newline='', encoding='utf-8') as csvfile2:
                writer = csv.writer(csvfile2, delimiter = ",")
                writer.writerow(["Country Name", "2015 [YR2015]"])
                writer.writerow([max_value, max_country])
                writer.writerow([min_value, min_country])

except FileNotFoundError:
    print("Файл лаба 11.csv не знайдено!")
