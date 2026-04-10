import datetime

def read_file(filename: str):
    """Зчитує дані з .txt файлу"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip().split(",") for line in lines]

def filter_product_data(data, product_name: str):
    """Фільтрує дані по конкретному товару"""
    return [
        (name.strip(), datetime.datetime.strptime(date.strip(), "%Y-%m-%d"), float(price.strip()))
        for name, date, price in data if name.strip().lower() == product_name.lower()
    ]

def get_last_month_changes(product_data):
    """Повертає зміни ціни за останній місяць"""
    today = datetime.datetime.today()
    one_month_ago = today - datetime.timedelta(days=30)
    return [(date, price) for _, date, price in product_data if date >= one_month_ago]

if __name__ == "__main__":
    filename = "products.txt"   # файл з даними
    product_name = "Молоко"     # товар, який хочемо перевірити

    data = read_file(filename)
    product_data = filter_product_data(data, product_name)
    changes = get_last_month_changes(product_data)

    print(f"Зміни ціни на {product_name} за останній місяць:")
    for date, price in changes:
        print(f"{date.date()} — {price} грн")
