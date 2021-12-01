def usd_to_vnd():
    usd = input("Please enter USD: ")
    if usd:
        usd = int(usd)
        vnd = usd*22
        print(f"{usd}USD = {vnd}k VND")

def main():
    usd_to_vnd()

if __name__ == "__main__":
    main()
