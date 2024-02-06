import pulp

model = pulp.LpProblem("Task1", pulp.LpMaximize)

x1 = pulp.LpVariable(name="Лимонад", lowBound=0, cat='Integer')
x2 = pulp.LpVariable(name="Фруктовий сік", lowBound=0, cat='Integer')

model += x1 + x2

model += 2 * x1 + 1 * x2 <= 100 # Вода
model += 1 * x1 <= 50           # Цукор
model += 1 * x1 <= 30           # Лимонний сік
model += 2 * x2 <= 40           # Фруктове пюре

model.solve()

print(f'{"Лимонад":20}:', x1.value())
print(f'{"Фруктовий сік":20}:', x2.value())
print(f'{"Всього продуктів":20}:', model.objective.value())
