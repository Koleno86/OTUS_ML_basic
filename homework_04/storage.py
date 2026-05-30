from media import File, FileFormat
from utils import define_file_type
from typing import Protocol, Type
from pathlib import Path, PurePath, PurePosixPath

# from abc import ABC, abstractmethod

"""
class Storage[TPath: (str, Path)](ABC):
    @abstractmethod
    def read(self, path: TPath) -> File: ...

    @abstractmethod
    def save(self, path: TPath, file: File) -> bool: ...

    @abstractmethod
    def delete(self, path: TPath, file: File) -> bool: ...
"""


class Storage[TPath: PurePath](Protocol):
    def read(self, path: TPath) -> File: ...
    def save(self, path: TPath, file: File) -> bool: ...
    def delete(self, path: TPath, file: File) -> bool: ...


class S3Storage(Storage[PurePosixPath]):
    def read(self, path: PurePosixPath) -> File:
        print("ok", path)

        # return File()

    def save(self, path: PurePosixPath, file: File) -> bool:
        print(path, file, "is saved")
        return True

    def delete(self, path: PurePosixPath, file: File) -> bool:
        print(path, file, "is deleted")
        return True


class SMBShare(Storage[Path]):
    def read(self, path: Path) -> File:
        print(path.is_file(), path.is_dir())
        if path.is_file():
            content: bytes = path.read_bytes()
            size: int = len(content)
            file_format: FileFormat = FileFormat.from_suffix(path.suffix)
            file_type: Type[File] = define_file_type(file_format)

            return file_type(
                name=path.name,
                format=file_format,
                size=size,
                content=content,
            )

    def save(self, path: Path, file: File) -> bool:
        print(path, file, "is saved")
        return True

    def delete(self, path: Path, file: File) -> bool:
        print(path, file, "is deleted")
        return True
