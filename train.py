import argparse

from tensorflow.python.keras.optimizers import Adam

from losses import heatmap_loss, offset_loss
from models import posenet


def get_arguments():
    _parser = argparse.ArgumentParser()
    _parser.add_argument("--input_shape", default=(224, 224, 3), type=tuple)
    _parser.add_argument("--epochs", default=100, type=int)
    _parser.add_argument("--batch_size", default=32, type=int)
    _args = _parser.parse_args()
    return _args


def main():
    args = get_arguments()
    input_shape = args.input_shape
    model = posenet(input_shape=input_shape)
    model.compile(optimizer=Adam(), loss=[heatmap_loss, offset_loss])


if __name__ == '__main__':
    main()
