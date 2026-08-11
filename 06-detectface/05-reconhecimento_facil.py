import face_recognition
from PIL import Image, ImageDraw
import numpy as np

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.

# Load a sample picture and learn how to recognize it.
germano_image = face_recognition.load_image_file("images/germano.png")
germano_face_encoding = face_recognition.face_encodings(germano_image)[0]

# Load a second sample picture and learn how to recognize it.
fernando_image = face_recognition.load_image_file("images/fernando.png")
fernando_image_face_encoding = face_recognition.face_encodings(fernando_image)[0]

# Load a sample picture and learn how to recognize it.
tiago_image = face_recognition.load_image_file("images/tiago.png")
tiago_face_encoding = face_recognition.face_encodings(tiago_image)[0]

# Load a sample picture and learn how to recognize it.
lucas_image = face_recognition.load_image_file("images/lucas.png")
lucas_face_encoding = face_recognition.face_encodings(lucas_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    germano_face_encoding,
    fernando_image_face_encoding,
    tiago_face_encoding,
    lucas_face_encoding
]
known_face_names = [
    "Germano",
    "Fernando",
    "Tiago",
    "Lucas"
]

# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("images/image3.png")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

BOX_PADDING = 20
BOX_COLOR = (0, 255, 0)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    if name == "Unknown":
        continue

    # Aumenta a caixa ao redor do rosto com uma margem
    top -= BOX_PADDING
    right += BOX_PADDING
    bottom += BOX_PADDING
    left -= BOX_PADDING

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=BOX_COLOR, width=3)

    # Draw a label with a name below the face
    left_bbox, top_bbox, right_bbox, bottom_bbox = draw.textbbox((0, 0), name)
    text_width, text_height = right_bbox - left_bbox, bottom_bbox - top_bbox
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=BOX_COLOR, outline=BOX_COLOR)
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")