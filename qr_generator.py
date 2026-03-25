import qrcode
from datetime import datetime  # for logging timestamp

def generate_qr_code():
    print("Welcome to the QR-Code Generator!")

    # Feature 2: Prevent empty input
    while True:
        data = input("Please enter text or URL: ").strip()
        if data != "":
            break
        print("Error: Input cannot be empty! Please try again.\n")

    filename = input("Enter the image filename (e.g., code.png): ").strip()
    if not filename.endswith('.png'):
        filename += '.png'

    # Create QR-Code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    # Feature 1: Save history to file
    with open("history.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {data} -> saved as: {filename}\n")

    print(f"Success! QR-Code saved as '{filename}'.")
    print("Input has been logged in history.txt.")

if __name__ == "__main__":
    generate_qr_code()