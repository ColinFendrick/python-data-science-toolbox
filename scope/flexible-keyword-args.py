def report_status(**kwargs):
    print("\nBEGIN: REPORT\n")

    for key, value in kwargs.items():
        print(key + ": " + value)

    print("\nEND REPORT")


report_status(name="luke", age='65', status="missing")
report_status(firstName="anakin", affiliation="sith lord", status="deceased")
