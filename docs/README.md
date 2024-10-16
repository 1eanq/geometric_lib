# Описание решения
Вычисления производятся с помощью следующих формул:

## Площадь
- Круг: S = πR²
- Квадрат: S = a²

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b

  # Примеры использования
```
//Принимает радиус круга, возвращает площадь круга
def area(r):
  return math.pi * r * r
```

```
circle.area(3)
```
```
7.065
```
---
```
// Принимает сторону квадрата, возвращает площадь квадрата
def area(a):
    return a * a
```
  ```
  square.area(2)
  ```
  ```
  4
  ```
---
```
//Принимает радиус окружности, возвращает длинну окружности
def perimeter(r):
    return 2 * math.pi * r
```
  ```
  circle.perimeter(3)
  ```
  ```
  18.8496
  ```
---
```
// Принимает сторону квадрата, возвращает периметр квадрата
def perimeter(a):
    return 4 * a
```
  ```
  square.perimeter(2)
  ```
  ```
  8
  ```

# Изменения
```
commit ff52139e90414814034a96e9d0322aff5f951959 (HEAD -> main)
Author: leanq <leanqha@gmail.com>
Date:   Wed Oct 2 11:53:37 2024 +0300

    fixed rectangle.py
```

```
commit 6f0239727f4cd94ab28c3dd3d454776fc58347e6
Author: leanq <leanqha@gmail.com>
Date:   Wed Oct 2 11:52:15 2024 +0300

    added triangle.py
```
```
commit 0b5397dca0eb3b59d4b756d684ff1ac825151d1a
Author: leanq <leanqha@gmail.com>
Date:   Wed Oct 2 11:50:35 2024 +0300

    added rectangle.py
```
