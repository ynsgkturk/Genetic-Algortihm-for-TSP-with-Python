import os
import pandas as pd


def read_scenario(path, scenario_number):
    """
    Reads coordinates of subareas from the given scenario csv.
    Args:
        scenario_number (int): The number of the case to read.
        path (str): The path to the case files.
    Returns:
        Subareas: list of coordinates of subareas if the case exists, None otherwise.
    """
    # Set the file names
    csv_file_name = os.path.join(path, f"scenario_{scenario_number}.csv")

    # Check if the files exist
    if not os.path.exists(csv_file_name):
        # print(f"scenario_{case_number} doesn't exist")
        return None

    # Read the data from the CSV file
    df = pd.read_csv(csv_file_name)
    
    # Convert and return the dataframe to a list of tuples
    return df.to_records(index=False).tolist()


def main():
    case_number = 3
    path = 'case_generator/scenarios'
    result = read_scenario(path, case_number)
    if result is not None:
        print("x,  y,  z")
        for i in range(len(result)):
            print(result[i])

        print(len(result))
    else:
        print(f"scenario_{case_number} doesn't exist!")


if __name__ == '__main__':
    main()
