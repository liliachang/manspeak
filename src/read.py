import csv

def read_data(path):
    data_list = []
    with open(path, "r") as csvfile:
        data_list = [{k:v for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
    return data_list

if __name__ == '__main__':
    print(read_data("data/accused_clean.csv"))
            
    
