import datetime
import os

base_path = 'moonshine-iconpack/'


def get_files() -> list:
    return os.listdir(base_path)


def print_files_with_date(files: list) -> None:
    for file in files:
        print(file, datetime.datetime.fromtimestamp(
            os.path.getmtime(f'{base_path}{file}')))


def rename_files(files: list) -> None:
    for file in files:
        date = datetime.datetime.fromtimestamp(
            os.path.getmtime(f'{base_path}/{file}')).strftime("%Y-%m-%d")
        if date not in file:
            os.rename(f'{base_path}/{file}', f'{base_path}/{date}-{file}')


if __name__ == '__main__':
    files = get_files()
    rename_files(files)
    print_files_with_date(files)
