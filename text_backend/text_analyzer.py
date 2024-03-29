#!/usr/bin/env python3
from text_analyzer.text_model.config_files.args_parser import prepare_args
from text_analyzer.text_model.analyzer.analyze import generate_data
from text_analyzer.text_model.analyzer.model.model import run_model
from text_analyzer.text_model.analyzer.model.data_balancer import balance_data
import pandas as pd

if __name__ == "__main__":
    parser = prepare_args()
    args = parser.parse_args()

    if args.dataset is None:
        print("Analyzing Files...")
        df = generate_data(args)

    else:
        df = pd.read_csv(args.dataset)

    if not args.dont_balance:
        df = balance_data(df)

    # Remoeve all dead data (temporary)
    df = df.dropna()

    run_model(args, df)

