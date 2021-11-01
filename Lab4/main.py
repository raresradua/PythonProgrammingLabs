"""
    Laboratory 4 - Python Programming
"""
import os
import sys

def ex_1(path_to_directory="test_dir_ex1_and_ex2"):
    """
        Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.

        Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din
        directorul dat ca parametru.

        :return: lista sortata cu elemente unice, elementele sunt extensiile fisierelor
    """
    # extensions = set()
    # for file in os.listdir(path_to_directory):
    #     if os.path.isfile(os.path.join(path_to_directory, file)) and len(file.split(".")) > 1:
    #         extensions.add(file.split(".")[1]) - no 'set' comprehension

    if os.path.isdir(os.path.abspath(path_to_directory)):
        extensions = {file.split(".")[1] for file in os.listdir(path_to_directory)
                      if os.path.isfile(os.path.join(path_to_directory, file)) and len(file.split(".")) > 1
                      }
    return sorted(extensions)


def ex_2(path_to_directory="test_dir_ex1_and_ex2", path_to_file="test_dir_ex1_and_ex2/A_dir_test_ex2/ex_2.txt"):
    """
    Să se scrie o funcție ce primește ca argumente două căi: director si fișier.

    Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a
    fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

    :return:
    """
    for file in os.listdir(path_to_directory):
        if os.path.isfile(os.path.join(path_to_directory, file)) and file.startswith("A"):
            try:
                f = open(path_to_file, "at")
                f.write(os.path.join(os.path.abspath(path_to_directory), file))
                f.write("\n")
                f.close()
            except Exception as e:
                print(str(e), type(e))


def ex_3(my_path="test_dir_ex1_and_ex2/test_4_dir/test_file_ex_3.txt"):
    """
    Să se scrie o funcție ce primește ca parametru un string my_path.

    Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
    Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
    sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea
    extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.

    :return:
    """
    if os.path.isfile(os.path.abspath(my_path)) and os.path.exists(os.path.abspath(my_path)):
        try:
            f = open(my_path, "rt")
            last_characters = f.read()[-20:]
            f.close()
            return f'Last 20 characters of file {os.path.basename(my_path)}: "{last_characters}". There are {len(last_characters)} characters'
        except Exception as e:
            print(str(e), type(e))

    elif os.path.isdir(os.path.abspath(my_path)) and os.path.exists(os.path.abspath(my_path)):
        extensions = []
        for _, _, files in os.walk(os.path.abspath(my_path)):
            for file in files:
                if len(file.split(".")) > 1:
                    extensions.append(file.split(".")[1])

        print(extensions)
        tuple_list = [(ext, extensions.count(ext)) for ext in set(extensions)]
        tuple_list.sort(reverse=True, key=lambda t: t[1])
        return tuple_list

    else:
        print("File/Directory does not exist")


def ex_4():
    """
        Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la
        linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

        :return:
    """
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: main.py path_to_directory")

        path_to_directory = sys.argv[1]
        if os.path.isdir(os.path.abspath(path_to_directory)):
            extensions = [file.split(".")[1] for file in os.listdir(path_to_directory)
                          if os.path.isfile(os.path.join(path_to_directory, file)) and len(file.split(".")) > 1
                          ]
        extensions = list(filter(lambda ext: extensions.count(ext) == 1, extensions))
        extensions.sort()
        return extensions

    except ValueError as e:
        print(e)


def ex_5(target, to_search):
    """
    Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o
    listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar
    in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă
    target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.

    :param target: path to a file or directory
    :param to_search: string that you want to search within files
     :return: list of the files that contain the string to_search
    """

    try:
        if not os.path.isdir(os.path.abspath(target)) and not os.path.isfile(
                os.path.abspath(target)) and not os.path.exists(os.path.abspath(target)):
            raise ValueError(f"{os.path.basename(target)} is not a file or a directory or does not exist!")

        files_target = list()

        if os.path.isfile(os.path.abspath(target)):
            f = open(os.path.abspath(target), "r")
            if to_search in f.read():
                files_target.append(os.path.basename(os.path.abspath(target)))
            f.close()
        elif os.path.isdir(os.path.abspath(target)):
            for root, dirs, files in os.walk(os.path.abspath(target)):
                for file in files:
                    f = open(os.path.abspath(os.path.join(root, file)), "r")
                    if to_search in f.read():
                        files_target.append(os.path.basename(os.path.abspath(file)))
                    f.close()
        return files_target
    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)


def callback_func_ex_6(exception):
    print(f"Custom exception handler: {exception}")


def ex_6(target, to_search, callback_func):
    """
    Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că
    primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fear eroare apărută în
    procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru

    :param target: path to a file or directory
    :param to_search: string that you want to search within files
     :param callback_func: callback function that is called when a Exception is raised/catched
     :return: list of files that contain the to_search string
    """
    files_target = list()
    try:
        if not os.path.isdir(os.path.abspath(target)) and not os.path.isfile(
                os.path.abspath(target)) and not os.path.exists(os.path.abspath(target)):
            raise ValueError(f"{os.path.basename(target)} is not a file or a directory or does not exist!")

        if os.path.isfile(os.path.abspath(target)):
            f = open(os.path.abspath(target), "r")
            if to_search in f.read():
                files_target.append(os.path.basename(os.path.abspath(target)))
            f.close()
        elif os.path.isdir(os.path.abspath(target)):
            for root, _, files in os.walk(os.path.abspath(target)):
                for file in files:
                    f = open(os.path.abspath(os.path.join(root, file)), "r")
                    if to_search in f.read():
                        files_target.append(os.path.basename(os.path.abspath(file)))
                    f.close()
        return files_target
    except ValueError as e:
        callback_func(e)
    except Exception as e:
        callback_func(e)


def ex_7(path_to_file):
    """
    Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si
    returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea
    fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False
    daca se poate citi din/scrie in fisier.

    :param path_to_file: path to a file
    :return: dictionary with the full path, size, extension, if it is readable, if it can be writable for the given file
    """
    try:
        if not os.path.isfile(os.path.abspath(path_to_file)):
            raise ValueError("Not a path to a file.")

        info = dict()
        info["full_path"] = os.path.abspath(path_to_file)
        info["file_size"] = str(os.path.getsize(os.path.abspath(path_to_file))) + " bytes"
        info["file_extension"] = os.path.splitext(os.path.abspath(path_to_file))[1] \
            if len(os.path.splitext(os.path.abspath(path_to_file))) > 1 else ""
        info["can_read"] = os.access(os.path.abspath(path_to_file), os.R_OK)
        info["can_write"] = os.access(os.path.abspath(path_to_file), os.W_OK)

        return info

    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)


def ex_8(dir_path):
    """
    Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un
    director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina
    directorului dir_path.

    :param dir_path: path to a directory on the disk
    :return: list of the absolute path to files of the directory given
    """
    try:
        if not os.path.isdir(os.path.abspath(dir_path)):
            raise ValueError("Not a path to a directory.")

        files = [os.path.abspath(file) for file in os.listdir(os.path.abspath(dir_path))
                 if os.path.isfile(os.path.abspath(os.path.join(dir_path, file)))]

        return files
    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)
