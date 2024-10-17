# import pathlib
from pathlib import Path


class 경로다루기(Path):
    def __init__(self, 경로):
        super().__init__(경로)

    def 현재경로확인(self):
        현재경로 = self.cwd()
        print(현재경로)
        return 현재경로


#     def asdf(self):

#     # 메소드
#     # 필드


# Path Creation  경로를 만들라   인스턴스
# Path.cwd()†
# Path.home()†
# : New in 3.5
# Path(*pathsegments)
# Combining
# .joinpath(*other)
# path / *other
# Conversion
# .as_posix()
# .as_uri()
# .relative_to(*other)
# .with_name(name)
# .with_stem(stem): New in 3.9
# .with_suffix(suffix)
# File/Folder iteration
# .iterdir()†
# .glob(pattern)†
# .rglob(pattern)†
# Pathlib Cheat Sheet
# File/Folder information
# .group()†
# .lstat()†
# .owner()†
# .stat()†
# Properties
# .anchor
# .drive
# .name
# .parent
# .parents
# .parts
# .root
# .stem
# .suffix
# .suffixes
# Boolean methods
# .exists()†
# .is_absolute()
# .is_block_device()†
# .is_char_device()†
# .is_dir()†
# .is_fifo()†
# .is_file()
# .is_mount()†
# : New in 3.7
# .is_reserved()
# .is_relative_to(*other): New in 3.9
# .is_socket()†
# .is_symlink()†
# .match(glob_pattern)
# .samefile(other_path)†
# : New in 3.5
# Utility functions
# .chmod(mode)†
# .expanduser()†
# : New in 3.5
# .lchmod(mode)†
# .link_to(target)†
# .mkdir(mode=0o777, parents=False, exist_ok=False)†
# .open(mode=’r’, buffering=-1, encoding=None,
# errors=None, newline=None)†
# .read_bytes()†
# : New in 3.5
# .read_text(encoding=None, errors=None)†
# : New in 3.5
# .readlink()†
# : New in 3.9
# .rename(target)†
# .replace(target)†
# .resolve(strict=False)†
# : New in 3.6: The strict argument (pre-3.6 behavior is strict).
# .rmdir()†
# .symlink_to(target, target_is_directory=False)†
# .touch(mode=0o666, exist_ok=True)†
# .unlink(missing_ok=False)†
# .write_bytes(data)†
# : New in 3.5
# .write_text(data, encoding=None, errors=None)†
# : New in 3.5
# Learn more at https://docs.python.org/3/library/pathlib.html
