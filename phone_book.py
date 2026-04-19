phone_book = {
    "Sahil": "9876543210",
    "Rahul": "9123456780",
    "Anita": "9988776655"
}

print("Phone book:", phone_book)

search_name = "Rahul"

if search_name in phone_book:
    print("Phone number of", search_name, "is", phone_book[search_name])
else:
    print(search_name, "not found")

phone_book["Priya"] = "9012345678"
print("Updated phone book:", phone_book)
