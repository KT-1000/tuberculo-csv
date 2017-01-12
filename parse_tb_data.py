import csv


def csv_reader(file_obj):
    """
    Read a csv file
    :param file_obj:
    :return:
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    :param file_obj:
    :return:
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["country"] + '\t' + line["e_pop_num"])


def csv_writer(data,path):
    """
    Write data to CSV file path.
    :param file_obj:
    :return:
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def csv_dict_writer(path, fieldnames, data):
    """
    Write a CSV file using csv.DictWriter.
    :param path:
    :param fieldnames:
    :param data:
    :return:
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    # csv_path = "data/TB_data_dictionary_2017-01-12.csv"
    # csv_path = "data/TB_burden_countries_2017-01-12.csv"
    # with open(csv_path, "r") as f_obj:
    #     csv_dict_reader(f_obj)
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nicklosville".split(","),
            "Dedric,Medhurst,Steidemannberg".split(",")]
    path = "data/patients.csv"
    # csv_writer(data, path)
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    csv_dict_writer(path, fieldnames, my_list)
