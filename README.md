# Project: QR Code Generator in Python

## Project Description

This project is a simple Python script that allows you to easily generate a **QR Code** from any text or URL and save it as an image file.


## Features

* Accepts user input (text or URL)
* Allows custom file naming
* Automatically adds `.png` extension if missing
* Generates high-quality QR codes
* Adjustable size and error correction level
* Optional color customization


## Requirements

Make sure you have Python installed on your system.

You also need to install the `qrcode` library:

```bash
pip install qrcode
```

## How to Run

1. Run the Python script:

```bash
python qr_generator.py
```

2. The program will ask for:

   * A text or URL
   * The output file name (e.g., `code.png`)

3. After execution, the QR code image will be saved in the same directory.


## Code Structure

The script follows these steps:

1. Get input from the user
2. Configure QR Code settings (size, border, error correction)
3. Generate the QR Code
4. Convert it into an image
5. Save the image file


## Customization (Optional)

You can change the QR code colors:

```python
img = qr.make_image(fill_color="blue", back_color="white")
```

You can also adjust size and layout:

```python
box_size=10
border=4
```


## Notes

* If you forget to add `.png` to the filename, the script will automatically append it.
* The more data you input, the larger the QR code becomes.


## Use Cases

* Sharing links quickly
* Digital business cards
* Wi-Fi connection QR codes
* Educational projects


## Author

This project is created for learning and practicing Python.


## License

This project is free to use.
