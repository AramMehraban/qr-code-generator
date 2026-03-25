# QR Code Generator in Python

A simple Python script that allows you to easily generate **QR Codes** from any text or URL and save them as image files.



## Features

- Accepts user input (text or URL)
- Allows custom file naming
- Automatically adds `.png` extension if missing
- Generates high-quality QR codes
- Adjustable size and error correction level
- Optional color customization



## Requirements

- Python 3.x
- Install dependencies with:

```bash
pip install -r requirements.txt
```

The main dependency is qrcode[pil], which includes Pillow for image handling.



## How to Run

1. Run the script:

```bash
python qr_generator.py
```

2. Enter the following when prompted:
    - A text or URL
    - The output file name (e.g., code.png)

3. After execution, the QR code image will be saved in the same directory.



## Project Structure

```
qr-code-generator/
│
├─ qr_generator.py
├─ requirements.txt
├─ README.md
└─ .gitignore
```



## Code Structure

1. Get input from the user
2. Configure QR Code settings (size, border, error correction)
3. Generate the QR Code
4. Convert it into an image
5. Save the image file



## Customization (Optional)

- Change QR code colors:

```bash
img = qr.make_image(fill_color="blue", back_color="white")
```

- Adjust size and layout:

```bash
box_size = 10
border = 4
```



## Notes

- If you forget to add .png to the filename, the script will automatically append it.
- The more data you input, the larger the QR code becomes.



## Use Cases
- Sharing links quickly
- Digital business cards
- Wi-Fi connection QR codes
- Educational projects



## Author

Aram Mehraban
  - This project is created for learning and practicing Python.



## License

This project is free to use.




**Extra tips for GitHub:**

1. Add a `requirements.txt` file with:

```bash
qrcode[pil]==7.4.2
```

2. Add a `.gitignore`:
    - pycache/
    *.py[cod]
    *.pyo
    venv/
    .env
    *.png


3. Commit and push:

```bash
git add README.md requirements.txt .gitignore
git commit -m "Add polished README, requirements, and gitignore"
git push origin main
```