from pathlib import Path

import cv2
import click
import numpy as np


def convert_image(file_path: Path) -> Path:
    click.echo(f'Processing {file_path}')
    input_file = cv2.imread(str(file_path), cv2.IMREAD_UNCHANGED)  # convert images to signed double
    ir = input_file[:, :, 0]
    green = input_file[:, :, 1]
    red = input_file[:, :, 2]

    ir_mat = np.float32(ir)

    g_mat = np.float32(green)
    g_mat = cv2.subtract(g_mat, ir_mat * .8)

    r_mat = np.float32(red)
    r_mat = cv2.subtract(r_mat, ir_mat + .65)

    output = cv2.normalize(
        cv2.merge((g_mat, r_mat, ir_mat * .6)),
        dst=None,
        alpha=255,
        beta=0,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_8UC1,
    )

    new_file_path = file_path.with_name(f'converted_{file_path.name}')
    is_converted = cv2.imwrite(str(new_file_path), output)
    if not is_converted:
        raise FileNotFoundError(f'Could not convert image {file_path}')

    click.echo(click.style(f'Successfully converted image: {new_file_path}\n', fg='green'))
    return new_file_path


def process_files(file_path: Path) -> None:
    if file_path.is_dir():
        for file in file_path.iterdir():
            process_files(file)

    if file_path.is_file():
        convert_image(file_path)
    else:
        click.echo(click.style(f'The {file_path} will be skipped, because it is not a file.', fg='red'))


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def cli(files: tuple[str, ...]) -> None:
    for file in files:
        process_files(Path(file))


if __name__ == '__main__':
    cli()
