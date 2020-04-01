import requests
import click


@click.command()
@click.argument('url')
@click.argument('filename', type=click.Path())
def download_file(url, filename):
    print(f"Downloading from {url} to {filename}")
    response = requests.get(url)
    with open(filename, "wb") as ofile:
        ofile.write(response.content)


# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# file_name = "data/raw/iris.csv"
if __name__ == "__main__":
    download_file()
