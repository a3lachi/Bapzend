import os
import sqlite3
from PIL import Image

# # Connect to the SQLite database
# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()


# # Get the list of image files in the folder
# folder_path = './backend/data/images/'
# image_files = os.listdir(folder_path)

# # Iterate through the list of image files and insert them into the table
# for i, filename in enumerate(image_files):
#     # Open the image file and convert it to binary data
#     with open(os.path.join(folder_path, filename), 'rb') as f:
#         image_data = f.read()

#     # Insert the image data into the table
#     c.execute('''INSERT INTO images (id, filename, data)
#                  VALUES (?, ?, ?)''', (i+1, filename, image_data))

# # Commit the changes to the database and close the connection
# conn.commit()
# conn.close()

folder_path = './media/images/'
image_files = os.listdir(folder_path)

s=[]
for a in image_files : 
    s.append(''.join(a.split('vb9')))

nn = []
for a in s :
    l = ''.join(a.split('#'))
    nn.append(''.join(l.split('®')))


print(sorted(s))



dir_path = './media/images'

# loop over all files in the directory
for filename in os.listdir(dir_path):
    a = ''.join(filename.split('™'))

    os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, a))
