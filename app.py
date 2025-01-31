import os
from flask import Flask, request, jsonify

app = Flask(__name__)
BASE_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
SPECIES_DATA_DIR = os.path.join(BASE_DATA_DIR, "mmaforays")
UPLOADS_DIR = os.path.join(BASE_DATA_DIR, "uploads")


@app.route('/')
def hello_world():  # put application's code here
    return SPECIES_DATA_DIR

@app.route("/list_csv_files", methods=["GET"])
def list_csv_files():
    """List CSV files in a directory."""
#    directory = request.args.get("directory", "MMAforays")
#    if directory == "MMAforays":
    directory_path = SPECIES_DATA_DIR
#    else:
#        directory_path = UPLOADS_DIR
#    directory_path = os.path.join(Config.BASE_DATA_DIR, directory)
    csv_files = [f for f in os.listdir(directory_path) if f.endswith(".csv")]
    return jsonify({"files": csv_files}), 200

if __name__ == '__main__':
    app.run()
