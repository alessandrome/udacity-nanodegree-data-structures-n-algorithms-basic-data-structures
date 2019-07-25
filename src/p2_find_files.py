import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    file_list = []
    if os.path.exists(path):
        if os.path.isfile(path) and path.endswith(suffix):
            file_list.append(path)
        elif os.path.isdir(path):
            list_dir = os.listdir(path)
            for el in list_dir:
                el_path = os.path.join(path, el)
                file_list += find_files(suffix, el_path)
    return file_list


# List printing show original strings with escape characters (eg: backslash [\] is escaped [\\])
print(find_files('.c', './p2_testdir'))  # Return list of .c files in p2_test directory (and its subdirectories)
print(find_files('.h', './p2_testdir'))  # Return list of .h files in p2_test directory (and its subdirectories)
print(find_files('.gitkeep', './p2_testdir'))  # Return list of .gitkeep files in p2_test directory (and its subdirectories)
print(find_files('.avi', './p2_testdir'))  # Return give an empty array
print(find_files('', './p2_testdir'))  # Return an array with ALL files present in the directory
print(find_files('', './invalid/path'))  # Return an empty array with invalid path
print(find_files('.c', './p2_testdir/t1.c'))  # Return list with the passed path because it is a valid path and a file that respect the suffix filter
print(find_files('.h', './p2_testdir/t1.c'))  # Return empty list because it is a valid path and a file but that doesn't respect the suffix filter
