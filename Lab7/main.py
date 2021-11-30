"""
    Laboratory 7 - Python Programming
"""
import hashlib
import json
import os
import random
import sys
import time
import zipfile


def ex_1(a, b):
    """
    1. Write a program that will write the minutes passed from the start, every x seconds, where x is random chosen
    at each iteraton (from the inteval [a, b] , where a, b are arguments). The program will run infinitely.

    """
    start = time.time()
    x = random.randint(a, b) if a <= b else random.randint(b, a)
    while True:
        minutes = (time.time() - start) / 60
        print(minutes)
        time.sleep(x)


def ex_2_first(n):
    """
    2. Write two functions to check if a number is prime, and check which of them is more time-efficient.
    """
    if n < 2:
        print(f"%d is not prime" % n)
    elif n == 2:
        print(f"%d is prime" % n)
    else:
        ok = 0
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                ok = 1
                print(f"%d is not prime" % n)
                break
    if not ok:
        print(f"%d is prime" % n)


def ex_2_second(n):
    prime = list()
    if n == 2:
        pass
    elif n < 2:
        prime = [n]
    else:
        prime = [n for i in range(2, n // + 1) if n % i == 0]

    if len(prime) > 0:
        print(f"%d is not prime" % n)
    else:
        print(f"%d is prime" % n)


def ex_3(first_path, second_path):
    """
    3. Write a function that will receive as parameters  two strings representing file paths and will return True if
    the files are identical or False otherwise.
    """
    if os.path.getsize(first_path) != os.path.getsize(second_path):
        return False
    file1 = open(first_path, "rt")
    file2 = open(second_path, "rt")
    chunksize = 5
    chunk1 = file1.read(chunksize)
    chunk2 = file2.read(chunksize)
    while chunk1 or chunk2:
        if chunk1 != chunk2:
            break
        chunk1 = file1.read(chunksize)
        chunk2 = file2.read(chunksize)
        chunksize += 5
    file1.close()
    file2.close()
    if chunk1 == chunk2:
        return True
    return False


def ex_4(path_to_dir):
    """
    Write a script that receives a directory as argument and creates a JSON file with data about all the files in
    that directory. For each file, the following information will be displayed: file_name, md5_file, sha256_file,
    size_file (in bytes), time when the file was created (human-readable) and the absolute path to the file.

    :return:
    """

    def hash_calculator(content, mode):
        if mode == "md5":
            return hashlib.md5(content).hexdigest()
        if mode == "sha256":
            return hashlib.sha256(content).hexdigest()

    if not os.path.isdir(os.path.abspath(path_to_dir)):
        return "path is not to a directory"
    else:
        info = {}
        id = 0
        for root, dirs, files in os.walk(path_to_dir):
            for file in files:
                try:
                    if os.path.isfile(os.path.join(root, file)):
                        with open(os.path.join(root, file), "rb") as f:
                            chunksize = 4096
                            content = ""
                            infos_read = f.read(chunksize)
                            content += str(infos_read)[2:-1]
                            while infos_read:
                                content += str(infos_read)[2:-1]
                                chunksize += 4096
                                infos_read = f.read(chunksize)

                            content = str.encode(content)
                            info[id] = {
                                "file_name": f.name,
                                "md5_file": hash_calculator(content, mode="md5"),
                                "sha256_file": hash_calculator(content, mode="sha256"),
                                "size_file": os.path.getsize(os.path.join(root, file))
                            }
                        id += 1
                except PermissionError:
                    print("No read permissions for " + os.path.join(root, file), file=sys.stderr)
                    continue
                except MemoryError:
                    print(os.path.join(root, file) + " is too big", file=sys.stderr)
                    continue
                except OSError:
                    print("Couldn't open file " + os.path.join(root, file), file=sys.stderr)
                    continue
        with open("info.json", "wt") as fp:
            infos_read = json.dumps(info, indent=4)
            fp.write(infos_read)


def ex_5(a_path, ext):
    """
    Write a function that receives two parameters: a_path and ext. The script will add all files from the a_path
    folder that have the extension ext to a zip archive named the.zip.

    :param a_path: path to a folder
    :param ext: extension of a file
    :return:  the.zip archive created containing all files in the a_path folder that have extension ext
    """
    if not os.path.isdir(a_path):
        return "Path is not to a directory."

    zip_file = zipfile.ZipFile("the.zip", "w", zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(a_path):
        for file in files:
            file_name = os.path.join(root, file)
            if os.path.splitext(file_name)[1] == ext:
                zip_file.write(file_name)
    zip_file.close()


def ex_6(x=1):
    """
    6. Write a script that writes the day of the week for the New Year Day, for the last x years (x is given as argument).

    :param x: last x years
    :return: Day of the week for the last x years
    """

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    this_year = 2021
    print(f"1 January %(year)d: %(day)s" % {"year": this_year,
                                            "day": days[int((time.strptime(f"1 Jan %d" % this_year, "%d %b %Y")).tm_wday)]
                                            })

    while x - 1:
        this_year -= 1
        print(f"1 January %(year)d: %(day)s" % {"year": this_year,
                                                "day": days[int((time.strptime(f"1 Jan %d" % this_year, "%d %b %Y")).tm_wday)]
                                                })
        x -= 1


def ex_7():
    """
    Write a script to simulate loto 6/49 draw (numbers extraction). The output should be a list of six numbers
    between 1 and 49 representing the winning combination.

    :return: list containing the 6-number winning combination
    """
    return "Winning combination is " + str(random.sample([i for i in range(1, 50)], 6))


def ex_8(a_path, to_hextract):
    """
    Write a function that receives two parameters: a_path and to_hextract. If a_path is a valid zip archive and
    to_hextract  is a file inside the arhive the function will return the md5 digest for unzipped content of
    to_hextract and None otherwise.

    :return:
    """
    if zipfile.is_zipfile(os.path.abspath(a_path)):
        zip_file = zipfile.ZipFile(os.path.abspath(a_path))
        for i in zip_file.infolist():
            if to_hextract in i.filename:
                zip_file.extract(i.filename)
                with open(i.filename, "rb") as f:
                    digest = hashlib.md5(f.read()).hexdigest()
                zip_file.close()
                return "MD5 digest: " + digest
        zip_file.close()
        return None
    else:
        return None


if __name__ == "__main__":
    n = int(input("Input number: "))
    list_of_functions = [ex_2_first, ex_2_second]
    times = {}
    for f in list_of_functions:
        start = time.time()
        f(n)
        print("Function %s finished in %d seconds\n" % (str(f)[10:len(str(f)) - 16], time.time() - start))
        times[str(f)[10:len(str(f)) - 16]] = time.time() - start

    times_rev = [(v, k) for (k, v) in times.items()]
    times_rev.sort(key=lambda el: el[0])
    print("The more efficient one is: %s" % times_rev[0][1])
