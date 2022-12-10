import os
from pathlib import Path
import sys, shutil
from threading import Thread

EXTENSIONS = {
    "images": ('.jpeg', '.png', '.jpg', '.svg'),
    "video": ('.avi', '.mp4', '.mov', '.mkv'),
    "documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    "audio": ('.mp3', '.ogg', '.wav', '.amr'),
    "archives": ('.zip', '.gz', '.tar')
}


def clean(folder: Path) -> None:
    for file in folder.iterdir():
        files = []

        if file.is_file():
            sort_files(file, folder)

            if file.endswith(EXTENSIONS['images']):
                file_1 = shutil.move(os.path.join(folder), file_destination)
                files.append(file_1)
                print(f'Image moved to "images": {files}')
            elif file.endswith(EXTENSIONS['video']):
                file_2 = shutil.move(os.path.join(folder), file_destination)
                files.append(file_2)
                print(f'Video moved to "videos":{files}')
            elif file.endswith(EXTENSIONS['documents']):
                file_3 = shutil.move(os.path.join(folder), file_destination)
                files.append(file_3)
                print(f'Document moved to "documents":{files}')
            elif file.endswith(EXTENSIONS['audio']):
                file_4 = shutil.move(os.path.join(folder), file_destination)
                files.append(file_4)
                print(f'Audio moved to "audio":{files}')
            elif file.endswith(EXTENSIONS['archives']):
                file_5 = shutil.move(os.path.join(folder), file_destination)
                files.append(file_5)
                print(f'Archive moved to "archives":{files}')
            sort_files(file, folder)

        elif file.name not in EXTENSIONS.keys():
            sub_folder = file
            if not os.listdir(sub_folder):
                sub_folder.rmdir()
                return
            clean(sub_folder)

        for _ in files:
            thread = Thread(target=clean)
            thread.start()


def sort_files(file: Path, folder: Path) -> None:
    for folder_name, extensions in EXTENSIONS.items():
        if file.suffix in extensions:
            new_folder = folder.joinpath(folder_name)
            new_folder.mkdir(exist_ok=True)
            new_file_name = normalize(file.name.removesuffix(file.suffix))
            new_file = file.rename(new_folder.joinpath(new_file_name + file.suffix))

            if folder_name == 'archives':
                archive_unpack(new_folder, new_file)

            break

    else:
        new_file_name = normalize(file.name.removesuffix(file.suffix))

        file.rename(folder.joinpath(new_file_name + file.suffix))


def normalize(file_name: str) -> str:
    file.name = file.name.lower()
    new_file_name = normalize(file.name.removesuffix(file.suffix))
    file.rename(new_folder.joinpath(new_file_name + file.suffix))
    return file_name


def archive_unpack(folder: Path, file: Path):
    archive_folder = folder.joinpath(file.name.removesuffix(file.suffix))
    archive_folder.mkdir(exist_ok=True)
    shutil.unpack_archive(folder.joinpath(file), archive_folder)
    print("Archive file unpacked successfully.")


def main():
    if len(sys.argv) < 2:
        print('Enter path to folder, which should be cleaned:')
        exit()

    root_folder = Path(sys.argv[1])
    # it pass to my folder, downloads.

    if (not root_folder.exists()) and (not root_folder.is_dir()):
        print('Path incorrect')
        exit()

    clean(root_folder)


if __name__ == "__main__":
    main()
    print('it is done')
    exit()
    
