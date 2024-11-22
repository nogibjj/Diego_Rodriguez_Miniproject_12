import pandas as pd
from mylib.lib import (
    log_func,
    scatter_plot,
    generate_general_markdown,
    summary_statistics,
)
import os

file = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
x_log = "Log GDP per capita (constant 2010 US$)"
x = "GDP per capita (constant 2010 US$)"
y = "Mortality rate, infant (per 1,000 live births)"
title = "Log GDP and Under-5 Mortality"
plot = "plot.png"


def png_scatter_plot():
    df = pd.read_csv(file)
    df = log_func(df, x_log)
    scatter_plot(df, x_log, y, title, plot)


def table_markdown_file():
    df = pd.read_csv(file)
    df = log_func(df, x_log)
    print(summary_statistics(df, x).to_frame().reset_index())
    generate_general_markdown(df, x, y)


def test_main():
    "Checking files"
    assert os.path.isfile("images/plot.png")
    assert os.path.isfile("Data_summary.md")


if __name__ == "__main__":
    png_scatter_plot()
    table_markdown_file()
    test_main()
