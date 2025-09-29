#WAP to detect spam if containing following keywords "make a lot of money", "buy now", "click this", "subscribe this"
text = input("Enter the text: ")
spam_keywords = ["make a lot of money", "buy now", "click this", "subscribe this"]
for keyword in spam_keywords:
    if keyword in text.lower():
        print("This text is detected as spam.")
        break
else:
    print("This text is not spam.")