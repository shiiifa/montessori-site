import re

# Read the file
with open('images.html', 'r') as f:
    content = f.read()

# List of images to remove from the array
images_to_remove = [
    'im5.jpeg', 'im7.jpeg', 'im16.jpeg', 'im81.jpeg', 
    'im84.jpeg', 'im94.jpeg', 'im97.jpeg', 'im99.jpeg', 
    'im100.jpeg', 'im104.jpeg', 'im105.jpeg'
]

# Remove each image from the array - handle both cases
for img in images_to_remove:
    # Pattern 1: remove from middle/end with comma before
    pattern1 = r", './image/" + re.escape(img) + r"'"
    content = re.sub(pattern1, '', content)
    
    # Pattern 2: remove from start with comma after
    pattern2 = r"'./image/" + re.escape(img) + r"', "
    content = re.sub(pattern2, '', content)

# Change cover photo from im99.jpeg to im89.jpeg
content = content.replace('url(./image/im99.jpeg)', 'url(./image/im89.jpeg)')

# Write back
with open('images.html', 'w') as f:
    f.write(content)

print('Gallery fixed successfully!')
print('- Removed 11 broken images from the gallery')
print('- Changed cover photo to im89.jpeg')
