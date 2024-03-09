import csv
import argparse
from collections import defaultdict

# parse cmd
arg_parser = argparse.ArgumentParser(prog='csv_parser.py', description='This is the function parses csv file')
arg_parser.add_argument('-i', nargs=1, type=str, required=True, metavar='input_file_path', dest='input', help='input csv file')
arg_parser.add_argument('-s', nargs='+', type=str, metavar='show_columns', dest='show', help='show the target columns')
arg_parser.add_argument('-o', nargs=1, type=str, metavar='output_file_name', dest='output_file', help='the output file that contains the target data')
arg_parser.add_argument('-p', action='store_const', const=True, default=False, dest='print', help='if print the target csv values on the screen')
args = arg_parser.parse_args()

# public function

def get_columns_from_csv_file(input_file_path, target_columns):
    
    with open(input_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='|')
        columns = defaultdict(list) 
        for row in csv_reader:
            for key, value in row.items():
                columns[key].append(value)
    
    if not target_columns:
        return columns
    else:
        target_columns_output = defaultdict(list)
        for col in target_columns:
            target_columns_output[col] = columns[col]
        return target_columns_output


def print_target_columns(target_cols_dict):

    # headers:
    # target_cols_dict.keys() # list of str
    key_list = target_cols_dict.keys()
    row_content = '|'.join(key_list)
    result = row_content + '\n'
    row_content = ''

    #data:
    target_value_list = list()
    for key in key_list:
        target_value_list.append(target_cols_dict[key])

    value_zip_list = list(zip(*target_value_list))

    for value in value_zip_list:
        per_line = '|'.join(value)
        row_content = per_line + '\n'
        result += row_content
    
    print (result)



def csv_writer(target_cols_dict, output_path):
    # headers:
    # target_cols_dict.keys() # list of str
    key_list = target_cols_dict.keys()
    row_content = '|'.join(key_list)
    # print(row_content)
    result = row_content + '\n'
    row_content = ''

    #data:
    target_value_list = list()
    for key in key_list:
        target_value_list.append(target_cols_dict[key])

    value_zip_list = list(zip(*target_value_list))

    for value in value_zip_list:
        per_line = '|'.join(value)
        row_content = per_line + '\n'
        result += row_content
    
    with open(output_path, "w") as ouput_file:
        ouput_file.write(result)
        ouput_file.close()


class csvFile:
    def __init__(self, input_file_path) -> None:
        self.file_path = input_file_path
        self.time_list = get_columns_from_csv_file(self.file_path, 'Time')
    

# main
#  python3 csv_parser_script_ver.py -i test.csv -s Time key-1 key-3 -o ./output.csv          

csv_f = csvFile('./'.join( args.input))

if (args.print):
    print_target_columns(get_columns_from_csv_file(csv_f.file_path, args.show))



if (args.output_file):
    csv_writer(get_columns_from_csv_file(csv_f.file_path, args.show), *args.output_file)


