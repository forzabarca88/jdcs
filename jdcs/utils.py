import os
import jdcs.config as config

PLACEHOLDER_TEXT = '''
Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. 
Duis mollis, est non commodo luctus laoreet rutrum faucibus dolor auctor.
'''


def placeholder_text(multiplier=1):
    return ''.join(PLACEHOLDER_TEXT for i in range(multiplier))


def get_all_files_in_dir(os_dir_join_args, base_dir=config.BASE_DIR, file_filter=None):
    os.chdir(base_dir)
    dir = os.path.join(*os_dir_join_args)
    files = os.listdir(path=dir)
    if file_filter:
        files = [os.path.join(dir, file)
                 for file in files if file.find(file_filter) >= 0]
    return files


def send_email(sender, receiver, subject, body):
    pass


def contact_admin(sender, body, subject='New message received'):
    receiver = config.ADMIN_EMAIL_ADDRESS
    return send_email(sender, receiver, subject, body)

def add_email_to_db(db_model, sender_name, sender, receiver, subject, body):
    db_model.sender_name = sender_name.data
    db_model.sender = sender.data
    db_model.receiver = receiver
    db_model.subject = subject
    db_model.body = body.data
    db_model.sent = False
    try:
        db_model.commit()
        return True
    except Exception as e:
        print(e)
        return False
