from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from mylib.lib import (
    log_func,
    scatter_plot,
    generate_general_markdown,
    summary_statistics,
)

# from dotenv import load_dotenv
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PLOT_FOLDER = "static/images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PLOT_FOLDER"] = PLOT_FOLDER


@app.route("/", methods=["GET", "POST"])
def input_page():
    if request.method == "POST":
        # Handle file upload and form inputs
        file = request.files["file"]
        x = request.form["x"]
        y = request.form["y"]
        title = request.form["title"]

        # Save uploaded file
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Redirect to dashboard with parameters
        return redirect(
            url_for("dashboard", file_path=file_path, x=x, y=y, title=title)
        )

    return render_template("input_page.html")


@app.route("/dashboard")
def dashboard():
    # Get parameters from URL
    file_path = request.args.get("file_path")
    x = request.args.get("x")
    y = request.args.get("y")
    title = request.args.get("title")

    # Read data and process
    df = pd.read_csv(file_path)
    df = log_func(df, x)

    # Generate plot
    plot_path = os.path.join(app.config["PLOT_FOLDER"], "plot.png")
    scatter_plot(df, x, y, title, "plot.png")

    # Generate summary statistics
    summary_x = summary_statistics(df, x).to_dict().items()
    summary_y = summary_statistics(df, y).to_dict().items()

    return render_template(
        "dashboard.html",
        plot_path=plot_path,
        summary_x=summary_x,
        summary_y=summary_y,
        x=x,
        y=y,
    )


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PLOT_FOLDER, exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
