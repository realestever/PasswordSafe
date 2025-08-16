# Password Safe
Attempt at a simple password safe

## Commands
**view** - lists stored user and password combinations  
**add** - add new user and password combination  
**q** - quit  

## Notes
Using Fernet symmetric encryption from the cryptography library. Salt is stored in a bin file for decryption retrieval. This is _not_ secure and only for learning 
