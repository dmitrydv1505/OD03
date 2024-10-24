# OD03
 OD03.  Алгоритмы сортировки


Оценка сложности каждого алгоритма сортировки:

1. **Пузырьковая сортировка (Bubble Sort):**

   - **Временная сложность:** O(n²) в худшем и среднем случаях. В лучшем случае (если массив уже отсортирован) сложность может быть оптимизирована до O(n) с помощью флага, который проверяет, были ли произведены обмены в текущем проходе.
   - **Пространственная сложность:** O(1) дополнительной памяти, так как сортировка выполняется на месте.

2. **Быстрая сортировка (Quick Sort):**

   - **Временная сложность:** O(n log n) в среднем случае. В худшем случае, например, при выборе первого или последнего элемента в качестве опорного для уже отсортированного массива, сложность может вырасти до O(n²). Однако использование рандомизации или выбора среднего элемента помогает избежать худшего случая.
   - **Пространственная сложность:** O(log n) на стеке вызовов рекурсии в среднем, если использовать оптимальный подход.

3. **Сортировка выбором (Selection Sort):**

   - **Временная сложность:** O(n²) во всех случаях (худший, средний и лучший), так как необходимо пройти по массиву и найти минимальный элемент для каждой позиции.
   - **Пространственная сложность:** O(1) дополнительной памяти, так как сортировка выполняется на месте.

4. **Сортировка вставками (Insertion Sort):**

   - **Временная сложность:** O(n²) в худшем и среднем случаях. В лучшем случае (если массив уже отсортирован) сложность составляет O(n), так как не требуется сдвигов.
   - **Пространственная сложность:** O(1) дополнительной памяти, так как сортировка выполняется на месте.

**Оценка:**

- Пузырьковая и выбором сортировки имеют одинаковую временную сложность O(n²), но пузырьковая сортировка может быть немного улучшена в лучших случаях. Оба алгоритма неэффективны для больших массивов.
- Быстрая сортировка является одной из наиболее эффективных по времени, с временной сложностью O(n log n) в среднем, но требует более внимательного подхода для предотвращения худших случаев.
- Сортировка вставками может быть эффективной для почти отсортированных массивов или небольших наборов данных, благодаря лучшей временной сложности O(n) в лучшем случае.