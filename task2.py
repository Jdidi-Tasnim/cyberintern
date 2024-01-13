def perform_xor_operation(data, key):
    result = bytearray()
    for byte in data:
        result.append(byte ^ key)
    return bytes(result)

try:
    # take path of image as input
    path = input(r'Enter path of Image : ')

    # taking encryption/decryption key as input
    key = int(input('Enter Key for encryption/decryption of Image : '))

    # validate key range
    if key < 0 or key > 255:
        raise ValueError('Key must be in the range 0 to 255.')

    # print path of image file and key that we are using
    print('The path of file:', path)
    print('Key for encryption/decryption:', key)

    # open file for reading purpose
    fin = open(path, 'rb')

    # storing image data in variable "image"
    image = fin.read()
    fin.close()

    # perform XOR operation on each value of the image data for encryption
    encrypted_data = perform_xor_operation(image, key)

    # create a new file for writing encrypted data
    encrypted_path = path.replace('.jpg', '_encrypted.jpg')
    fin = open(encrypted_path, 'wb')

    # write encrypted data to the new file
    fin.write(encrypted_data)
    fin.close()

    print('Encryption Done. Encrypted file saved as:', encrypted_path)

    # perform XOR operation on each value of the encrypted data for decryption
    decrypted_data = perform_xor_operation(encrypted_data, key)

    # create a new file for writing decrypted data
    decrypted_path = path.replace('.jpg', '_decrypted.jpg')
    fin = open(decrypted_path, 'wb')

    # write decrypted data to the new file
    fin.write(decrypted_data)
    fin.close()

    print('Decryption Done. Decrypted file saved as:', decrypted_path)

except Exception as e:
    print('Error caught:', type(e).__name__, '-', str(e))
