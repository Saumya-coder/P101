import dropbox
import os 
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
       

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token='sl.BHktzvhd1Z2pO3k9qdd_G1NzZe-2ZaWpupsxMFAFEaf7M4OKxbfKDSB74YkqGlHHFwYl4ZxzBHzW7pnL5iVpiByvkq4-3PjcPhB2eqDio2JFBSP9va1ERlr72gmZWGLQCYzrkII'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Moved!!!")

if __name__ == '__main__':
    main()