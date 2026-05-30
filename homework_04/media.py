from dataclasses import dataclass, asdict, astuple
from typing import Tuple, Dict, List, Type, Set, Any, Optional, Self
from datetime import date, time
from enum import StrEnum

type Resolution = Tuple[int, int]
type FPS = int
type Duration = time
type Bitrate = int
type ColorDepth = int
type AspectRatio = Tuple[int, int]
type FileProperties = Dict[str, Any]
type FileTypes = Dict[Type[File], Set[FileFormat]]


class FileFormat(StrEnum):
    AVI = ".avi"
    MP3 = ".mp3"
    MOV = ".mov"
    TXT = ".txt"
    JPG = ".jpg"
    GIF = ".gif"

    @classmethod
    def add(cls, name: str) -> None:
        setattr(cls, name.upper(), f".{name.lower()}")

    @classmethod
    def from_suffix(cls, suffix: str) -> Self:
        clean_suffix = f".{suffix.lstrip('.')}".lower()

        try:
            return cls(clean_suffix)
        except ValueError:
            raise ValueError(
                f"Расширение '{suffix}' не поддерживается классом {cls.__name__}"
            )


@dataclass(kw_only=True)
class File:
    name: str
    format: FileFormat
    size: Optional[int] = None
    creation_date: Optional[date] = date.today()
    owner: Optional[str] = None
    content: Optional[bytes] = None

    @property
    def properties(self) -> FileProperties:
        return asdict(self)

    @properties.setter
    def properties(self, file_props: FileProperties) -> None:
        for key, value in file_props.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"Поле '{key}' не существует")

    def copy(self) -> Self:
        return type(self)(**self.properties)

    def rename(self, new_name: str) -> Self:
        self.properties.name = new_name
        return self


@dataclass
class AudioFile(File):
    bitrate: Optional[Bitrate] = None
    duration: Optional[Duration] = None


@dataclass
class VideoFile(File):
    resolution: Optional[Resolution] = None
    duration: Optional[Duration] = None
    color_depth: Optional[ColorDepth] = None
    frame_rate: Optional[FPS] = None


@dataclass
class ImageFile(File):
    resolution: Optional[Resolution] = None
    color_depth: Optional[ColorDepth] = None


RESERVED_FILE_TYPES: FileTypes = {
    AudioFile: {FileFormat.MP3},
    ImageFile: {FileFormat.JPG, FileFormat.GIF},
    VideoFile: {FileFormat.MOV, FileFormat.AVI},
}
