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

def get_tree_sum(root):
    """
    Знаходить суму всіх значень у дереві за допомогою рекурсії.
    """
    # Базовий випадок рекурсії: якщо вузла не існує, його сума дорівнює 0
    if root is None:
        return 0
    
    # Сума дерева = значення поточного вузла + сума лівої гілки + сума правої гілки
    return root.val + get_tree_sum(root.left) + get_tree_sum(root.right)

# --- Тестування Завдання 2 ---
if __name__ == "__main__":
    # Створюємо дерево та додаємо ті самі значення
    root = Node(50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    
    print("--- Підрахунок суми значень дерева ---")
    total_sum = get_tree_sum(root)
    print(f"Сума всіх значень у дереві: {total_sum}") # Очікується 350 (50+30+20+40+70+60+80)
