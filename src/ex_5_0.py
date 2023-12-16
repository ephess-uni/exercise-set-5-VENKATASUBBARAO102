"""ex_5_0.py"""

def line_count(infile):
    with open(infile, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        print(f"Number of lines in {infile}: {num_lines}", end='\n')

if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    count_file = data_directory / "ex_5_4-data.csv"
    line_count(count_file)
