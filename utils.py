import os

PLACEHOLDER_TEXT = '''
Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. 
Duis mollis, est non commodo luctus laoreet rutrum faucibus dolor auctor.
'''
def placeholder_text(multiplier=1):
    return ''.join(PLACEHOLDER_TEXT for i in range(multiplier))

def get_all_files_in_dir(os_dir_join_args, file_filter=None):
    dir = os.path.join(*os_dir_join_args)
    files = os.listdir(path=dir)
    if file_filter:
        files = [os.path.join(dir, file) for file in files if file.find(file_filter) >= 0]
    return files