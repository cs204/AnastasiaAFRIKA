def main():
    v = input("Сколько футов:")
    result = feet2meter(v)
    print(f"Это будет {result:.2f} метров.")

def feet2meter(v):
    v = v[:-2]  # Удаляем последние два символа "ft"
    return round(float(v) * 0.3048, 2)


main()
