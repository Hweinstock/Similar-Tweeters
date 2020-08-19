#!/usr/bin/env python3

from args_parser import prepare_args
from analyze import generate_data
from model import run_model
from data_balancer import balance_data

if __name__ == "__main__":
    parser = prepare_args()
    args = parser.parse_args()

    if args.dataset is None:
        print("Analyzing Files...")
        csv_file = generate_data(args)
        if not args.dont_balance:
            csv_file = balance_data(csv_file)

    else:
        csv_file = balance_data(args.dataset)

    run_model(args, csv_file)

