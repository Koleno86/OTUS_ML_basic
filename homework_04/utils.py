from media import File, FileFormat, RESERVED_FILE_TYPES
from typing import Callable, Dict, Type

type ConvertFn = Callable[[File, FileFormat], File]

CONVERTERS: Dict[FileFormat, Dict[FileFormat, ConvertFn]] = {}


def converter(from_: FileFormat, to_: FileFormat):
    def decorator(convert_fn: ConvertFn):
        if to_ not in CONVERTERS:
            CONVERTERS[to_] = {}

        CONVERTERS[to_][from_] = convert_fn
        return convert_fn

    return decorator


@converter(from_=FileFormat.JPG, to_=FileFormat.GIF)
def jpg_to_gif(file: File) -> File:
    if file.format != FileFormat.JPG:
        raise TypeError("Некорректный входной формат, должен быть JPG")

    gif_file = file.copy()

    ###
    # convertion jpg to gif
    ###

    gif_file.properties = {
        "name": gif_file.name.split(".")[0] + FileFormat.GIF,
        "format": FileFormat.GIF,
    }

    return gif_file


def convert(file: File, new_format: FileFormat) -> File:
    try:
        convert_fn = CONVERTERS[new_format][file.format]

        return convert_fn(file)
    except KeyError:
        raise ValueError(f"Нет доступного конвертера для формата {new_format}")


def define_file_type(file_format: FileFormat) -> Type[File]:
    for file_type, associated_formats in RESERVED_FILE_TYPES.items():
        if file_format in associated_formats:
            return file_type

    return File
    # raise TypeError(f"Нет доступного типа файла для инстанции типа {file_format}")
