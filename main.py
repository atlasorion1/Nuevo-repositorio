def test_login(user, password):
    if user == "admin" and password == "1234":
        print("Successful")
    else:
        print("Failed")

test_login("admin1", "1234")
test_login("user", "0000")
