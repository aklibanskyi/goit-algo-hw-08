class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """Допоміжна функція для вставки нового вузла в двійкове дерево пошуку."""
    if root is None:
        return Node(key)
    
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

def find_min_value(root):
    """
    Знаходить найменше значення у двійковому дереві пошуку.
    Найменше значення завжди знаходиться в самому лівому вузлі.
    """
    if root is None:
        return None
    
    current = root
    # Рухаємося ліворуч, поки є куди
    while current.left is not None:
        current = current.left
        
    return current.val

# --- Тестування Завдання 1 ---
if __name__ == "__main__":
    # Створюємо дерево та додаємо значення
    root = Node(50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    
    print("--- Пошук мінімуму в дереві ---")
    min_val = find_min_value(root)
    print(f"Найменше значення в дереві: {min_val}")  # Очікується 20
