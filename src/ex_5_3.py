"""ex_5_3.py
This module contains an entry point that:

- creates a CLI that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

def process_data(infile, outfile):
    # Load data from the input file
    data = np.loadtxt(infile, delimiter=",")

    # Shift and scale the data
    mean = np.mean(data)
    std_dev = np.std(data)
    processed_data = (data - mean) / std_dev

    # Save the processed data to the output file using numpy routines
    np.savetxt(outfile, processed_data, delimiter=",")

if __name__ == "__main__":
    # Create your argument parser object here.
    parser = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")
    parser.add_argument("infile", help="Input filename for the data to be processed")
    parser.add_argument("outfile", help="Output filename for the processed data")
    args = parser.parse_args()

    # Call the process_data function with the provided arguments
    process_data(args.infile, args.outfile)
