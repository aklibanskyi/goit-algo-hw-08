import heapq

def min_cost_to_connect_cables(cables):
    """
    Знаходить мінімальні витрати на об'єднання мережевих кабелів.
    Використовує мінімальну купу (min-heap) для вибору двох найменших кабелів на кожному кроці.
    """
    # Якщо кабелів немає або він лише один, об'єднувати нічого не потрібно
    if not cables:
        return 0
    if len(cables) == 1:
        return 0
        
    # Перетворюємо звичайний список на купу (це робиться in-place)
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first_shortest = heapq.heappop(cables)
        second_shortest = heapq.heappop(cables)
        
        # Витрати на їх з'єднання — це сума їхніх довжин
        current_connection_cost = first_shortest + second_shortest
        total_cost += current_connection_cost
        
        # Додаємо новий (об'єднаний) кабель назад у купу
        heapq.heappush(cables, current_connection_cost)
        
    return total_cost

# --- Тестування алгоритму ---
if __name__ == "__main__":
    test_cables_1 = [5, 4, 2, 8]
    test_cables_2 = [1, 2, 3, 4, 5]
    
    print("--- Результати обчислення мінімальних витрат ---")
    
    cost1 = min_cost_to_connect_cables(test_cables_1.copy())
    print(f"Кабелі: {test_cables_1} -> Мінімальні витрати: {cost1}")
    # Очікуваний хід: 
    # 1. 2+4 = 6 (залишились 5, 6, 8)
    # 2. 5+6 = 11 (залишились 8, 11)
    # 3. 8+11 = 19
    # Загальні витрати = 6 + 11 + 19 = 36
    
    cost2 = min_cost_to_connect_cables(test_cables_2.copy())
    print(f"Кабелі: {test_cables_2} -> Мінімальні витрати: {cost2}")
    # Очікувані витрати: 33
