import csv
import os

from googletrans import Translator

INPUT_DIR = 'csvs'
OUTPUT_DIR = 'csvs'
COLUMN_LIST = ['fath', 'name']
INPUT_LANGUAGE = 'hindi'

class GoogleTranslator:
    def __init__(self,
                 input_file=None,
                 output_file=None,
                 column_list=COLUMN_LIST,
                 input_language=INPUT_LANGUAGE
                 ):
        # Create Translator object
        self.translator = Translator()

        # define session object
        self.input_file = input_file
        self.output_file = output_file
        self.column_list = COLUMN_LIST
        self.input_language = input_language

        # define translated cells object
        self.translated_cells = {}

    def Start(self):
        with open(self.input_file, mode='r', encoding='utf-8') as input_file:
            lines = csv.reader(input_file, delimiter=',')

            counter = 0
            for line in lines:
                # if header, make new header
                if counter == 0:
                    new_headers = self.MakeNewHeaders(line)
                    self.WriteHeader(new_headers)
                else:
                    print('line %s' % counter)
                    new_row = self.TranslateRow(line)
                    print('     %s' % new_row)
                    self.WriteData(new_row)

                counter += 1
    def WriteHeader(self, data):
        # write data into output csv file
        writer = csv.writer(open(self.output_file, 'w', encoding='utf-8'), delimiter=',', lineterminator='\n')
        writer.writerow(data)

    def WriteData(self, data):
        # write data into output csv file
        writer = csv.writer(open(self.output_file, 'a', encoding='utf-8'), delimiter=',', lineterminator='\n')
        writer.writerow(data)

    def MakeNewHeaders(self, headers):
        self.column_idxs = []

        new_headers = []
        header_idx = 0
        for header in headers:
            new_headers.append(header)
            for column in self.column_list:
                if header == column:
                    new_headers.append(header + '-english')
                    self.column_idxs.append(header_idx)

            header_idx += 1

        return new_headers

    def TranslateRow(self, row):
        # get values for translating
        input_values = []
        column_idx = 0
        for one in row:
            for idx in self.column_idxs:
                if column_idx == idx and one not in self.translated_cells and one not in input_values:
                    input_values.append(one)
                    break
            column_idx += 1

        # get translated values
        translated_values = self.translator.translate(input_values, src=self.input_language, dest='english')

        # add the translated_values into self.translated_cells
        for one in translated_values:
            self.translated_cells[one.origin] = one.text

        # make new row
        new_row = []

        idx = 0
        prev_idx = 0
        for one in self.column_idxs:
            new_row += row[prev_idx:one + 1]
            new_row.append(self.translated_cells[row[one]])

            prev_idx = one + 1
            idx += 1
        new_row += row[prev_idx:]

        return new_row


def main():
    files = os.listdir(INPUT_DIR)

    for file_name in files:
        input_file = INPUT_DIR + '/' + file_name
        output_file = OUTPUT_DIR + '/' + '%s-goog-translate%s' % (os.path.splitext(os.path.basename(file_name))[0], os.path.splitext(os.path.basename(file_name))[1])

        # create a Google Translator object
        google_translator = GoogleTranslator(
            input_file=input_file,
            output_file=output_file,
            column_list=COLUMN_LIST,
            input_language=INPUT_LANGUAGE
        )

        # start translation
        google_translator.Start()

if __name__ == '__main__':
    main()
