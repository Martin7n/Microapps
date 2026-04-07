#!/usr/bin/env python3

import os
import subprocess
import re
import argparse


def scan_selector(typescan, target):
    typescan = typescan.lower()
    chooser = {
        "a": allport,
        "p": pnscan,
        "v": version_vuln,
        "t": total_scan
    }

    if typescan not in chooser:
        print("\033[1;33mNon valid choice. -- Starting vuln scan (default). --\033[0m")
        return pnscan(target)
    return chooser[typescan](target)

def result_writers(scan_results, filename, target):
    print(f"\033[1;32m-- scan result preparation for {target} -- \033[0m")
    pattern = r'\d+\/[A-Za-z]+\s+open'

    working_dir = os.getcwd()
    file_path = os.path.join(working_dir, filename)

    with open(file_path, "w") as file:
        lines = scan_results.stdout.splitlines()
        [print(f"\033[1;31m--- found open ports @: {line} ---\033[0m") for line in lines if re.search(pattern, line)]
        for line in lines:
            file.writelines(line + "\n")  # Write each line with a newline

    print(f"\033[1;31m--- finished, see: {filename} ---\033[0m")


#scab selections functions:

def total_scan(target):
    pnscan(target)
    allport(target)
    version_vuln(target)
    print(f"\033[1;31m--- All finished! ---\033[0m")




def pnscan(target):
    print(f"\033[1;32m--Started Pn scan on {target} -- \033[0m")
    pn = subprocess.run(
        ['nmap', "-Pn", target, "-vv"],
        capture_output=True, text=True
    )
    result_writers(pn, "pn_scan.txt", target)

def allport(target):
    print(f"\033[1;32m--Started all ports scan: -p1-65535 on {target} -- \033[0m")
    all_p = subprocess.run(
        ['nmap', "-p1-65535", target, "-vv"],
        capture_output=True, text=True
    )
    result_writers(all_p, "all_ports_scan.txt", target)

def version_vuln(target):
    print(f"\033[1;32m-- Started -sV -sC vuln scan on {target} -- \033[0m")
    sv = subprocess.run(
        ['nmap', "-sV", "-sC", target, "-vv"],
        capture_output=True, text=True
    )

    if 'Host seems down' in sv.stdout:
        print('Host seems down. Try all ports?')
        print("[A]ll ports [E]xit")
        user_entry = input("[A]ll ports [E]xit: ")

        if user_entry.lower() == 'a':
            allport(target)
        else:
            return
    else:
        result_writers(sv, "report_vuln.txt", target)

def check_sudo_add_info():
    print("info scan flags/args: \033[1;31m[A]\033[0mLL ports or \033[1;31m[P]\033[0mn, \033[1;31m[V]\033[0muln or \033[1;31m[T]\033[0motal?")
    if os.geteuid() != 0:
        print("\033[1;31mWarning:Please run the script with sudo.\033[0m")
        return False
    return True

def main():
    run_with_sudo = check_sudo_add_info()

    parser = argparse.ArgumentParser(description="Automated Nmap Scanner")
    parser.add_argument("target", help="Target IP to scan")
    parser.add_argument(
        "typescan",
        nargs="?",
        default="p",
        choices=["a", "p", "v", "t"],
        help="Type of scan: 'a' for all ports, 'p' for Pn scan, 'v' for version/vuln scan (default: 'p'), \n 't' for all of them"
    )
    args = parser.parse_args()

    scan_selector(args.typescan, args.target)

if __name__ == "__main__":
    main()

#For global use: place the file in ~/.local/bin and chmod +x mmap.py
