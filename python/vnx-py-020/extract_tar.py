# vnx-py-020 eval target
import tarfile
import os

# TRIGGERS: extractall() without path validation - zip slip vulnerability
def extract_archive_bad(archive_path, dest_dir):
    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(dest_dir)

# Also triggers: extractall() without members filter
def extract_user_archive(upload_path, output_dir):
    tf = tarfile.open(upload_path)
    tf.extractall(output_dir)
    tf.close()

# Safe alternative (Python 3.12+):
# tar.extractall(dest_dir, filter='data')
#
# Or manually validate:
# for member in tar.getmembers():
#     if os.path.abspath(os.path.join(dest_dir, member.name)).startswith(os.path.abspath(dest_dir)):
#         tar.extract(member, dest_dir)
