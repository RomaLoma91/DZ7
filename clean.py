from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize

def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return None
    filename.unlink()

def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')

    def main(folder: Path) -> None:
        parser.scan(folder)
        for file in parser.JPEG_IMAGES:
            handle_media(file, folder / 'images' / 'JPEG')
        for file in parser.JPG_IMAGES:
            handle_media(file, folder / 'images' / 'JPG')
        for file in parser.PNG_IMAGES:
            handle_media(file, folder / 'images' / 'PNG')
        for file in parser.SVG_IMAGES:
            handle_media(file, folder / 'images' / 'SVG')
        for file in parser.AVI_VIDEO:
            handle_media(file, folder / 'video' / 'AVI')
        for file in parser.MP4_VIDEO:
            handle_media(file, folder / 'video' / 'MP4')
        for file in parser.MOV_VIDEO:
            handle_media(file, folder / 'video' / 'MOV')
        for file in parser.MKV_VIDEO:
            handle_media(file, folder / 'video' / 'MKV')
        for file in parser.DOC_DOCUMENT:
            handle_media(file, folder / 'document' / 'DOC')
        for file in parser.DOCX_DOCUMENT:
            handle_media(file, folder / 'document' / 'DOCX')
        for file in parser.TXT_DOCUMENT:
            handle_media(file, folder / 'document' / 'TXT')
        for file in parser.PDF_DOCUMENT:
            handle_media(file, folder / 'document' / 'PDF')
        for file in parser.XLSX_DOCUMENT:
            handle_media(file, folder / 'document' / 'XLSX')
        for file in parser.PPTX_DOCUMENT:
            handle_media(file, folder / 'document' / 'PPTX')
        for file in parser.MP3_AUDIO:
            handle_media(file, folder / 'audio' / 'MP3')
        for file in parser.OGG_AUDIO:
            handle_media(file, folder / 'audio' / 'OGG')
        for file in parser.WAV_AUDIO:
            handle_media(file, folder / 'audio' / 'WAV')
        for file in parser.AMR_AUDIO:
            handle_media(file, folder / 'audio' / 'AMR')
        for file in parser.ZIP_ARCHIVE:
            handle_media(file, folder / 'archive' / 'ZIP')
        for file in parser.GZ_ARCHIVE:
            handle_media(file, folder / 'archive' / 'GZ')
        for file in parser.TAR_ARCHIVE:
            handle_media(file, folder / 'archive' / 'TAR')
        for file in parser.MY_OTHER:
            handle_media(file, folder / 'MY_OTHER')
        for folder in parser.FOLDERS[::-1]:
            handle_folder(folder)
    if __name__ == '__main__':
        folder_for_scan = Path(sys.argv[1])
        main(folder_for_scan.resolve())