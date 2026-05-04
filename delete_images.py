import os

files_to_delete = [
    'im5.jpeg',
    'im7.jpeg',
    'im16.jpeg',
    'im81.jpeg',
    'im84.jpeg',
    'im94.jpeg',
    'im97.jpeg',
    'im99.jpeg',
    'im100.jpeg',
    'im104.jpeg',
    'im105.jpeg',
    'prim.jpeg'
]

image_dir = 'image'

for filename in files_to_delete:
    filepath = os.path.join(image_dir, filename)
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Deleted: {filename}")
        else:
            print(f"Not found: {filename}")
    except Exception as e:
        print(f"Error deleting {filename}: {e}")

print("Done!")
