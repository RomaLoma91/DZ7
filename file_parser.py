import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVE = []
GZ_ARCHIVE = []
TAR_ARCHIVE = []
MY_OTHER = [] #TODO:Can be a problem!!!

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVE,
    'GZ': GZ_ARCHIVE,
    'TAR': TAR_ARCHIVE,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)
            continue
        ext = get_extension(item.name)
        full_name = folder / item.name
        if not ext:
            MY_OTHER.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_for_scan = sys.argv[1]

    print(f'Start in folder:{folder_for_scan}')
    input()
    scan(Path(folder_for_scan))
    print(f"Image jpeg: {JPEG_IMAGES}")
    print(f"Image jpg: {JPG_IMAGES}")
    print(f"Image png: {PNG_IMAGES}")
    print(f"Image svg: {SVG_IMAGES}")
    print(f"Video avi: {AVI_VIDEO}")
    print(f"Video mp4: {MP4_VIDEO}")
    print(f"Video mov: {MOV_VIDEO}")
    print(f"Video mkv: {MKV_VIDEO}")
    print(f"Document doc: {DOC_DOCUMENT}")
    print(f"Document docx: {DOCX_DOCUMENT}")
    print(f"Document txt: {TXT_DOCUMENT}")
    print(f"Document pdf: {PDF_DOCUMENT}")
    print(f"Documet xlsx: {XLSX_DOCUMENT}")
    print(f"Document pptx: {PPTX_DOCUMENT}")
    print(f"Audio mp3: {MP3_AUDIO}")
    print(f"Audio ogg: {OGG_AUDIO}")
    print(f"Audio wav: {WAV_AUDIO}")
    print(f"Audio amr: {AMR_AUDIO}")
    print(f"Arcives zip: {ZIP_ARCHIVE}")
    print(f"Arcives gz: {GZ_ARCHIVE}")
    print(f"Archives tar: {TAR_ARCHIVE}")
    print('*' * 25)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
