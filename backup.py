import dropbox
import dotenv
import os
import time

dotenv.load_dotenv()

dbx = dropbox.Dropbox(os.getenv('DROPBOX_ACCESS_TOKEN'))

with open('database.db', 'rb') as f:
    print('uploading to', dbx.users_get_current_account().email) # type: ignore

    dbx.files_upload(f.read(), f'/sqlite-backups/backup-{round(time.time() * 1000)}.db')

    print('done')
