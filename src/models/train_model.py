from data.preprocess import read_processed_data
import click

from random_forest import RandomForestModel
import sys

sys.path.append('src')


@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True, dir_okay=False))
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
def main(input_file, output_file):
    print('Training model')

    dframe = read_processed_data(input_file)
    model = RandomForestModel()
    model.train(dframe)
    model.save(output_file)


if __name__ == '__main__':
    main()
