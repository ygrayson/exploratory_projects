# exception.py
# Qianbo Yin


try:
    for i in range(5):
        print(1.0 / (3-i))
except Exception:
    print("Got an error", Exception)
