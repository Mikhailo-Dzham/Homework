def count_unique_contacts(n, phone_numbers):
    unique_contacts = set(phone_numbers)
    return len(unique_contacts)

n = int(input())
phone_numbers = input().strip().split()

print(count_unique_contacts(n, phone_numbers))

