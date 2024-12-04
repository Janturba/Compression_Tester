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
        'zlib': compress_with_zlib,
        'gzip': compress_with_gzip,
        'bz2': compress_with_bz2,
        'lzma': compress_with_lzma,
    }
    
    compressed_files = {}
    
    for name, func in algorithms.items():
        compressed_data = func(original_data)
        compressed_files[name] = compressed_data
        print(f"{name}: Compressed size = {len(compressed_data)} bytes")
    
    return compressed_files

# Run the loop
compressed_results = run_compression_loop('yourfile.txt')
