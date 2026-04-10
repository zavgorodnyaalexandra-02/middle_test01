def read_file(filename: str):
    """Зчитує дані з .txt файлу"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip().split(",") for line in lines]
