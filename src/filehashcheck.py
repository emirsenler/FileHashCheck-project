import hashlib
import argparse
import os
import json
import time
import logging
from colorama import Fore, Style, init

init(autoreset=True)  # Colorama renk sıfırlama

logging.basicConfig(filename="hashcheck.log", level=logging.INFO, format='%(asctime)s - %(message)s')

def calculate_hash(filepath, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

def process_file(filepath, algorithms, ref_hashes, rename_by):
    result = {
        "File": filepath,
        "Size (bytes)": os.path.getsize(filepath),
        "Hashes": {}
    }

    for algo in algorithms:
        hash_value = calculate_hash(filepath, algo)
        result["Hashes"][algo.upper()] = hash_value
        print(f"{algo.upper()}: {Fore.CYAN}{hash_value}{Style.RESET_ALL}")

        ref = ref_hashes.get(algo)
        if ref:
            match = (ref.lower() == hash_value)
            result[f"{algo.upper()}_MATCH"] = match
            status = f"{'UYUMLU' if match else 'UYUŞMUYOR'}"
            color = Fore.GREEN if match else Fore.RED
            print(f"{color}🟢 {algo.upper()} karşılaştırması: {status}{Style.RESET_ALL}")

    if rename_by in result["Hashes"]:
        ext = os.path.splitext(filepath)[1]
        new_name = result["Hashes"][rename_by].lower() + ext
        new_path = os.path.join(os.path.dirname(filepath), new_name)
        os.rename(filepath, new_path)
        print(f"📛 Dosya yeniden adlandırıldı: {new_name}")
        result["Renamed"] = new_name

    logging.info(json.dumps(result))
    return result

def main():
    parser = argparse.ArgumentParser(description="FileHashCheck – Gelişmiş Dosya Bütünlüğü Aracı")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--filepath", help="Hash'i hesaplanacak tek dosya")
    group.add_argument("--dir", help="Taranacak klasör")

    parser.add_argument("--algos", nargs='*', default=["md5", "sha1", "sha256"], help="Kullanılacak hash algoritmaları")
    parser.add_argument("--sha256", help="Referans SHA256")
    parser.add_argument("--md5", help="Referans MD5")
    parser.add_argument("--sha1", help="Referans SHA1")
    parser.add_argument("--export", help="Sonuçları JSON olarak dışa aktar")
    parser.add_argument("--rename-by-hash", choices=["md5", "sha1", "sha256"], help="Dosyayı belirtilen hash'e göre yeniden adlandır")

    args = parser.parse_args()

    start_time = time.time()
    all_results = []

    ref_hashes = {
        "md5": args.md5,
        "sha1": args.sha1,
        "sha256": args.sha256
    }

    if args.filepath:
        if not os.path.isfile(args.filepath):
            print("❌ Dosya bulunamadı.")
            return
        result = process_file(args.filepath, args.algos, ref_hashes, args.rename_by_hash or "")
        all_results.append(result)

    elif args.dir:
        if not os.path.isdir(args.dir):
            print("❌ Klasör bulunamadı.")
            return

        for root, _, files in os.walk(args.dir):
            for file in files:
                full_path = os.path.join(root, file)
                print(f"\n🔍 {full_path} taranıyor...")
                try:
                    result = process_file(full_path, args.algos, ref_hashes, args.rename_by_hash or "")
                    all_results.append(result)
                except Exception as e:
                    print(f"⚠️ Hata: {e}")

    if args.export:
        with open(args.export, "w") as f:
            json.dump(all_results, f, indent=4)
        print(f"\n📄 Sonuçlar '{args.export}' dosyasına yazıldı.")

    print(f"\n⏱️ İşlem süresi: {time.time() - start_time:.2f} saniye")

if __name__ == "__main__":
    main()
