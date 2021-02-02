import argparse

from PIL import Image
import pyheif


def conv(image_path):
    split_path = image_path.split(".")
    split_path[-1] = split_path[-1].replace("heic", "png")
    new_name = ".".join(split_path)
    heif_file = pyheif.read(image_path)
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    data.save(new_name, "PNG")


if __name__ == "__main__":
    DESCRIPTION = "Convert image format from HEIC to PNG"
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('Files', metavar='FILE_NAME', type=str, nargs='+',
                        help='a filename for converting')

    args = parser.parse_args()
    for fname in args.Files:
        conv(fname)
        print(f"Converted {fname}")
