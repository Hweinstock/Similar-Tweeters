#!/usr/bin/env python3

from text_model.config_files.args_parser import prepare_args
from text_model.analyzer.analyze import generate_data
from text_model.analyzer.model.model import run_model
from text_model.analyzer.model.data_balancer import balance_data

if __name__ == "__main__":
    parser = prepare_args()
    args = parser.parse_args()

    if args.dataset is None:
        print("Analyzing Files...")
        csv_file = generate_data(args)

    else:
        csv_file = args.dataset

    if not args.dont_balance:
        csv_file = balance_data(csv_file)

    run_model(args, csv_file)

