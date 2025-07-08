# WordPress Login Checker

A simple Python script to check WordPress login credentials from a list of URLs, usernames, and passwords.  

---

## 📄 Format of `domain.txt`

Each line should follow this format:

```
https://site.com/wp-login.php:username:password
```

---

## ▶️ How to run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Then run:
   ```
   python check.py
   ```

3. The script will automatically:
   - Save successful logins to `successful_logins.txt`
   - Save failed attempts to `failed_logins.txt`

---

## 📷 Example Output

Here’s what it looks like in action:

![Sample Output](output.jpg)

---

## ⚠️ Legal Note

This tool is created for **educational and testing purposes only**.  
Use it only on websites you own or have permission to test.

---

## 🧑‍💻 Author

Made by [codebyebrahim]
