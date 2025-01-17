# rans-dio
Created for educational purposes.

<h1 align="left">Basic ransomware with python</h1>

###

<p align="left">This program is an educational ransomware example that demonstrates file encryption and decryption. It uses the cryptography library to simulate how files can be encrypted and secured. This implementation is strictly for educational purposes to understand cryptography concepts and should never be used maliciously.</p>

###

<h4 align="left">What the Program Does:<br>Key Generation:<br><br>The program generates a cryptographic key and saves it in a file named chave.key. This key is required to encrypt and decrypt files.<br>File Encryption:<br><br>A specified file is encrypted, and its original content is replaced with an encrypted version. Without the key, the file content cannot be recovered.<br>File Decryption:<br><br>A file previously encrypted by the program can be decrypted using the stored key.<br>Menu Options:<br><br>The program provides a simple menu:<br><br>* Option 1: Generate the encryption key.<br>* Option 2: Encrypt a file.<br>* Option 3: Decrypt a file.<br>* Option 4: Exit the program.This program is an educational ransomware example that demonstrates file encryption and decryption. It uses the cryptography library to simulate how files can be encrypted and secured. This implementation is strictly for educational purposes to understand cryptography concepts and should never be used maliciously.</h4>

###

<h2 align="left">How to Set Up and Run the Program:</h2>

###

<h4 align="left">Clone or Download the Project: Ensure the program (meu_programa.py) and the requirements file (requirements.txt) are in the same directory.<br><br>Create a Virtual Environment (Optional but Recommended):<br><br>bash<br>Copiar<br>Editar<br>python -m venv venv<br>source venv/bin/activate   # For Windows: venv\Scripts\activate<br>Install the Required Libraries: Install the cryptography library by running:<br><br>pip install -r requirements.txt<br>The requirements.txt file should contain: cryptography<br><br>Run the Program:<br><br>Execute the script using Python:<br><br>python meu_programa.py<br><br>Menu Options:<br><br>Follow the on-screen menu:<br>Generate the key (Option 1).<br>Encrypt a file (Option 2).<br>Decrypt a file (Option 3).<br>Exit (Option 4).</h4>

###
