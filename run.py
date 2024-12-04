import zlib
import gzip
import bz2
import lzma


def compress_with_zlib(data):
    return zlib.compress(data)


def compress_with_gzip(data):
    return gzip.compress(data)


def compress_with_bz2(data):
    return bz2.compress(data)


def compress_with_lzma(data):
    return lzma.compress(data)


def run_compression_loop(file_path):
    with open(file_path, 'rb') as f:
        original_data = f.read()

    algorithms = {
        'zlib': (compress_with_zlib, '.zlib'),
        'gzip': (compress_with_gzip, '.gz'),
        'bz2': (compress_with_bz2, '.bz2'),
        'lzma': (compress_with_lzma, '.xz'),
    }

    compressed_files = {}

    for name, (func, extension) in algorithms.items():
        compressed_data = func(original_data)
        compressed_files[name] = compressed_data
        output_filename = f'compressed_with_{name}{extension}'
        with open(output_filename, 'wb') as result:
            result.write(compressed_data)
        print(f"{name}: Compressed size = {len(compressed_data)} bytes, saved as {output_filename}")

    return compressed_files


# Run the loop
compressed_results = run_compression_loop('data.txt')
