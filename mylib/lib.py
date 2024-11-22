import numpy as np
import seaborn.objects as so


def summary_statistics(df, x):
    summary_stats = df[x].describe().round(2)
    return summary_stats


def log_func(df, x):
    if x[:3].lower() == "log" or "Log":
        df[x] = np.log(df[x[4:]])
    elif x[:2].lower() == "ln" or "Ln":
        df[x] = np.log(df[x[3:]])
    return df


def scatter_plot(df, x, y, title, plot="plot.png"):
    my_chart = (
        so.Plot(
            df,
            x=x,
            y=y,
        )
        .add(so.Line(), so.PolyFit(order=2))
        .add(so.Dot())
        .label(title=title)
    )
    chart_path = "static/images/" + plot
    my_chart.save(chart_path)
    return chart_path


def table_format(text):
    table = "| Statistics | Value |\n| ----- | ----- |\n"
    for i in text.split(" "):
        for j in i.split("\n"):
            if j == "Name:":
                return table
            elif j == "":
                pass
            elif j[0].isdigit() and j[-1].isdigit():
                digit = float(j)
                table += f"{digit:.2f} |\n"
            else:
                table += f"| {j} | "


def generate_general_markdown(df, x, y):
    markdown_table1 = summary_statistics(df, x)
    markdown_table2 = summary_statistics(df, y)
    markdown_table1 = table_format(str(markdown_table1))
    markdown_table2 = table_format(str(markdown_table2))

    with open("Data_summary.md", "w", encoding="utf-8") as file:
        file.write(f"### Describe {x}:\n")
        file.write(markdown_table1)
        file.write("\n\n")
        file.write(f"### Describe {y}:\n")
        file.write(markdown_table2)
        file.write("\n\n")
        file.write("![scatter_plot](static/images/plot.png)\n")
    return "Data_summary.md"
