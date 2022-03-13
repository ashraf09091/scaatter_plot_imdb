import json
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file
from utils import get_top_movies

app = Flask(__name__, template_folder='template')


# Home page
@app.route('/', methods=['GET'])
def get_page():
    return render_template('view.html')


# To Get list of top 250 Movies
@app.route('/list', methods=['GET'])
def get_movie_list():
    # Get data from API
    data = get_top_movies()
    items = []

    # Process data for Ajax Request
    for data_dict in data:
        itm = {
            'title': data_dict,
            'ratings': list(data[data_dict].keys())[0],
            'votes': list(data[data_dict].values())[0],
        }
        items.append(itm)
    return json.dumps(items)


@app.route('/sactter', methods=['GET'])
def get_imdb_plots():
    # Get data from API
    data = get_top_movies()

    # Process data to create a scatter plot
    for data_dict in data.values():
        x = data_dict.keys()
        y = data_dict.values()
        plt.scatter(x, y, c="blue")

    # Label for X and Y axis
    plt.xlabel("Ratings")
    plt.ylabel("Votes")

    # Save the scatter plot image
    plt.savefig('scatterplot.jpg', bbox_inches='tight', dpi=150)
    return send_file('scatterplot.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()
