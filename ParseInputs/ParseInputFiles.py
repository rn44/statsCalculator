import csv


# def ClassFactory(class_name, dictionary):
#     return type(class_name, (object,), dictionary)


class ParseInputFiles:
    data = []

    def __init__(self):
        self.data = []

    def parse(self, filepath):
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                self.data.append(row)
                # print(row)
        if not self.data:
            raise Exception('List is empty.')
        else:
            return self.data
