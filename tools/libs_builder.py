"""Libs file builder"""
import hashlib
import json
import lzma
from pathlib import Path
import lzma as xz
import click


def __read_metadata__(fp):
    return [i.split(' ') for i in Path(fp).read_text().split('\n') if i]


def __read_libs__(fp):
    print("Opening the file:", fp)
    return Path(fp).read_bytes()


def __remove_ig_file_header__(file_data):
    return file_data[0xC2:]


def __is_file_header_present__(d):
    if d[:0x4] == b'\x00\x01\xc0P':  # IG libs header
        return True
    else:
        return False


def __is_file_ready_to_process__(d):
    if d[:0x04] == b"\x7fELF":  # ELF file header
        return True
    else:
        return False


def __parse_metadata__(meta: list, workdir_path: Path):
    parsed_meta = []
    last_offset = 0
    for i, lib in enumerate(meta):
        lib_path = lib[0]
        lib_size = int(lib[1])
        lib_hash = lib[2]
        parsed_meta.append({
            "name": lib_path,
            "path": str(workdir_path.joinpath(lib_path)),
            "hash": lib_hash,
            "size": lib_size,
            "start_addr": last_offset,
            "end_addr": last_offset + lib_size})
        last_offset += lib_size
    return parsed_meta


def __extract_lib__(lib_info, file_data):
    lib_data = file_data[lib_info["start_addr"]:lib_info["end_addr"]]
    lib_path = Path(lib_info['path'])
    calculated_hash = hashlib.sha256(lib_data)
    if lib_info['hash'] == calculated_hash.hexdigest():
        lib_path.parent.mkdir(parents=True, exist_ok=True)
        lib_path.write_bytes(lib_data)
        print('Successfully extracted lib: {}'.format(lib_info["path"]))
        return True
    else:
        print('Invalid hash lib digest! Failed to extract lib : {}'.format(lib_path))
        return False


def __generate_header__(raw_libs_packed_size, archive_size):
    size_b = raw_libs_packed_size.to_bytes(4, 'little')
    size_a = archive_size.to_bytes(4, 'little')

    header = bytes([  # Header for .spo file format
        0x00, 0x01, 0xC0, 0x50, 0x01, 0xAF, 0xAB, 0x05, 0x1F, 0x00, 0x00, 0x00,
        0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x6C, 0x69, 0x62, 0x73, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x61, 0x6E, 0x6F, 0x6E,
        0x00, 0x00, 0x00, 0x00, size_b[0], size_b[1], size_b[2], size_b[3], 0x59, 0x09, 0xF4, 0xBE,
        0xDC, 0x82, 0xF1, 0x78, 0x02, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, size_b[0], size_b[1], size_b[2], size_b[3],
        size_a[0], size_a[1], size_a[2], size_a[3],
        0x01, 0xA0
    ])

    return header


@click.group()
def cli():
    pass


@cli.command()
@click.option('--libs_dir', default="./extracted_libs/x86", help='Path to libs folder')
@click.option('--metadata_json', default="./extracted_libs/metadata.json", help='Path to metadata.json file')
def build_libs(libs_dir: str, metadata_json: str):
    """
    Rebuilds the extracted libraries into libs.spo.

    Warning!
    Different versions of libs.<ext> file format are used from version to version of Instagram,
    so this tool may become obsolete at any time and will need to be modified for the new file format!
    """
    print("Rebuilding lib.spo file. The results will be available in ./packed_files folder.")

    workdir_path = Path('./packed_files')  # Creating workdir folder
    workdir_path.mkdir(exist_ok=True, parents=True)

    libs_dir = Path(libs_dir)
    old_metadata = json.load(open(metadata_json))

    new_metadata = []

    packed_libs = bytes()

    for lib in old_metadata:
        lib_name = lib["name"]
        lib_path = libs_dir.joinpath(Path(lib_name).name)
        lib_data = lib_path.read_bytes()
        lib_hash = hashlib.sha256(lib_data).hexdigest()
        lib_size = str(len(lib_data))

        new_metadata.append([lib_name, lib_size, lib_hash])
        packed_libs += lib_data

    compressed_file = xz.compress(packed_libs,
                                  format=lzma.FORMAT_XZ,
                                  check=lzma.CHECK_NONE,
                                  preset=9)

    packed_size = len(packed_libs)
    archive_size = len(compressed_file)
    header = __generate_header__(packed_size, archive_size)

    workdir_path.joinpath('libs.spo').write_bytes(header + compressed_file)
    workdir_path.joinpath('metadata.txt').write_text('\n'.join([' '.join(i) for i in new_metadata]) + '\n')


@cli.command()
@click.option('--libs_file', default="./ig_source/assets/lib/libs.spo", help='Path to libs.spo file')
@click.option('--metadata_file', default="./ig_source/assets/lib/metadata.txt", help='Path to metadata.txt file')
def extract_libs(libs_file, metadata_file):
    """
    Extract libraries from libs. <extension> from x86 version of Instagram APK.
    """
    workdir_path = Path('./extracted_libs')
    workdir_path.mkdir(exist_ok=True, parents=True)

    data = __read_libs__(libs_file)
    metadata = __read_metadata__(metadata_file)
    if __is_file_header_present__(data):
        data = __remove_ig_file_header__(data)
        print("\nSaving a cleaned-up version of a file in ./file_without_header.bin", )
        workdir_path.joinpath("file_without_header.bin").write_bytes(data)
    if not __is_file_ready_to_process__(data):
        print("\nThe program cannot recognize the file type! \n"
              "It looks like Instagram has updated its way of storing libraries \n"
              "This file may have been compressed in some way, unpack "
              "it if compression is present on a file without a header \n."
              "This tool only supports the x86 version of IG, "
              "if you try to process the arm version with it, it will fail. \n"
              "You can also try to manually determine the type of data obfuscation method used and get rid of it. \n"
              "Or you can try use the binwalk tool maybe it can help too. ")
    else:
        parsed_metadata = __parse_metadata__(metadata, workdir_path)
        results = list(map(lambda x: __extract_lib__(x, data), parsed_metadata))
        print("Saving metadata to json file for further repacking.")
        json.dump(parsed_metadata, workdir_path.joinpath("metadata.json").open("w"), ensure_ascii=False,
                  indent=5)
        print("Successfully extracted libs count:", results.count(True))
        print("Number of unsuccessfully retrieved libraries:", results.count(False))


if __name__ == '__main__':
    cli()
