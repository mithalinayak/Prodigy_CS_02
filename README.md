# Image Encryption and Decryption

This project provides a graphical user interface (GUI) application that allows users to encrypt and decrypt images using a simple XOR-based encryption algorithm. The application is built using Python with the help of the `tkinter`, `matplotlib`, and `OpenCV` libraries.

## Features

- **Image Selection**: Users can select an image from their file system to encrypt or decrypt.
- **Encryption**: Encrypts the selected image using a key generated based on a seed.
- **Decryption**: Decrypts the encrypted image using the same key to recover the original image.
- **Save Images**: Encrypted and decrypted images can be saved in various formats (JPEG, PNG, BMP).
- **User-Friendly GUI**: The interface is designed with `tkinter` for easy navigation and use.

## Requirements

- Python 3.x
- The following Python packages are required:
  - `tkinter`
  - `matplotlib`
  - `opencv-python`
  - `numpy`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/image-encryption-decryption.git
   cd image-encryption-decryption
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```bash
     source myenv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python Image_Encryption.py
   ```

## Usage

1. **Choose an Image**: Click the "Choose" button to select an image from your file system.
2. **Encrypt the Image**: Click the "Encrypt" button to encrypt the selected image.
3. **Decrypt the Image**: Click the "Decrypt" button to decrypt the encrypted image.
4. **Save the Image**: After encryption or decryption, click the "Save" button to save the image in the desired format.
5. **Exit the Application**: Click the "EXIT" button to close the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- This project uses the [OpenCV](https://opencv.org/) library for image processing.
- The GUI is built with the `tkinter` library.
