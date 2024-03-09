This is a script that helps to read csv files more easily.


Usage: 
    ```python3 csv_parser.py -h```
        usage: csv_parser.py [-h] -i input_file_path [-s show_columns [show_columns ...]] [-o output_file_name] [-p]

        This is the function parses csv file

        options:
        -h, --help            show this help message and exit
        -i input_file_path    input csv file
        -s show_columns [show_columns ...]
                                show the target columns
        -o output_file_name   the output file that contains the target data
        -p                    if print the target csv values on the screen

    if Linux, can also use shell script to call this python script
    ```sh csv_parser.sh -i test.csv -s Time key-1 key-3 -o ./output.csv```

Example:
    ``` cat test.csv ```
        Time|key-1|key-2|key-3|key-4|key-5
        2023-09-18 02:02:03|11|12|13|14|15
        2023-09-18 02:17:03|21|22|23|24|25
        2023-09-18 02:32:03|31|32|33|34|#5
        2023-09-18 02:47:03|41|42|43|44|45
        2023-09-18 03:02:03|51|52|53|54|55
    
    ```sh csv_parser.sh -i test.csv -s Time key-1 key-3 -o ./output.csv```

    ``` cat output.csv ```
        Time|key-1|key-3
        2023-09-18 02:02:03|11|13   
        2023-09-18 02:17:03|21|23
        2023-09-18 02:32:03|31|33
        2023-09-18 02:47:03|41|43
        2023-09-18 03:02:03|51|53


