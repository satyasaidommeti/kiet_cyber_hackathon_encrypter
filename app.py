import base64
import io
from flask import Flask, render_template, request
from PIL import Image  # Add this import

app = Flask(__name__)

# Function to encode binary data to Base64
def encode_to_base64(binary_data):
    encoded_bytes = base64.b64encode(binary_data)
    return encoded_bytes.decode()

# Function to decode text from Base64
def decode_from_base64(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text)
    return decoded_bytes

# Function to encrypt text using Caesar Cipher
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Function to decrypt text using Caesar Cipher
def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

@app.route('/', methods=['GET', 'POST'])
def file_encryption():
    original_text = ""
    encrypted_text = ""
    decrypted_text = ""

    if request.method == 'POST':
        uploaded_file = request.files['file']

        if uploaded_file:
            file_contents = uploaded_file.read()
            content_type = uploaded_file.content_type.lower()

            if content_type.startswith('image/'):
                return "Image encryption is not supported on this page. <a href='/image'>Go to Image Encryption</a>"
            elif content_type == 'application/pdf':
                encrypted_text = encode_to_base64(file_contents)
            else:
                file_contents_text = file_contents.decode("utf-8")
                encrypted_text = caesar_cipher_encrypt(file_contents_text, shift=3)

            original_text = file_contents

    return render_template('index.html', original_text=original_text, encrypted_text=encrypted_text, decrypted_text=decrypted_text)

@app.route('/image', methods=['GET', 'POST'])
def image_processing():
    original_image = ""
    processed_image = ""

    if request.method == 'POST':
        uploaded_file = request.files['file']
        operation = request.form.get('operation')  # Added operation choice

        if uploaded_file:
            file_contents = uploaded_file.read()
            content_type = uploaded_file.content_type.lower()

            if not content_type.startswith('image/'):
                return "File is not an image. <a href='/image'>Go to Image Processing</a>"

            if operation == 'encrypt':
                # Encrypt the image here (you can use Pillow or other libraries)
                image = Image.open(io.BytesIO(file_contents))
                processed_image = image.rotate(180)  # Example encryption: rotating the image
                buffered = io.BytesIO()
                processed_image.save(buffered, format="PNG")
                processed_image = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()
                operation == 'grayscale'
                # Convert the image to grayscale
                image = Image.open(io.BytesIO(file_contents))
                processed_image = image.convert('L')  # Convert to grayscale
                buffered = io.BytesIO()
                processed_image.save(buffered, format="PNG")
                processed_image = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()
            elif operation == 'decrypt':
                # Decrypt the image here (you can implement the decryption logic)
                # For example, reversing the encryption process
                # processed_image = ...  # Implement decryption logic here
                pass

    return render_template('image.html', original_image=original_image, processed_image=processed_image)

# Modify the 'image.html' template to include options for encryption, decryption, and grayscale conversion

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
# The modification this is taken from Chatgit and greek for greeks website
