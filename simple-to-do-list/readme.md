# Simple In-Memory To-Do (CLI)

_A tiny command-line to-do list that keeps tasks **in memory** (no files, no menus).  
Type tasks line by line; press **Enter on an empty line** to finish and print the list._

---

## English

### What this script does
- Reads tasks from standard input, one per line.
- Stops when you press **Enter** on an empty line.
- Prints a **numbered** to-do list.
- Everything is **in memory only** (no persistence).

### Requirements
- Python 3.7+ (works on Windows/macOS/Linux)

### How to run
1) Save the code as `todo_simple.py`:
```python
# Simple in-memory to-do list (no files, no menus)
# Type tasks one by one; press Enter on an empty line to finish.

todos = []  # this will store tasks in memory

print("Enter tasks (press Enter on an empty line to finish):")
while True:
    task = input("Task: ").strip()
    if not task:           # stop when the input is empty
        break
    todos.append(task)     # store the task in the list

# Print the result
print("\nYour To-Do List:")
for i, t in enumerate(todos, start=1):   # enumerate gives (index, value)
    print(f"{i}. {t}")
```

2) Run it:
```bash
python todo_simple.py
```

### Example session
```
Enter tasks (press Enter on an empty line to finish):
Task: Buy milk
Task: Finish homework
Task: Read 10 pages
Task:
Your To-Do List:
1. Buy milk
2. Finish homework
3. Read 10 pages
```

### Limitations
- No edit/delete/mark-done while running.
- No data saved to disk (list is lost when the program exits).

### Future versions (ideas)
- Interactive loop (add/list/done/del/clear).
- JSON persistence (`todo.json`).
- Due dates, priorities, tags.
- Pretty table output.
- Unit tests and packaging (`pipx` runnable CLI).

---

## Tiếng Việt

### Script này làm gì?
- Nhập các task từ bàn phím, mỗi dòng một task.
- Dừng khi bạn nhấn **Enter** trên dòng trống.
- In danh sách công việc theo **thứ tự đánh số**.
- Dữ liệu chỉ **lưu trong bộ nhớ** (không ghi file).

### Yêu cầu
- Python 3.7+ (Windows/macOS/Linux đều chạy được)

### Cách chạy
1) Lưu code thành `todo_simple.py` (như ở phần English).
2) Chạy:
```bash
python todo_simple.py
```

### Ví dụ chạy
```
Enter tasks (press Enter on an empty line to finish):
Task: Mua sữa
Task: Làm bài tập
Task: Đọc 10 trang sách
Task:
Your To-Do List:
1. Mua sữa
2. Làm bài tập
3. Đọc 10 trang sách
```

### Hạn chế
- Không chỉnh sửa/xóa/đánh dấu hoàn thành trong lúc chạy.
- Không lưu dữ liệu ra file (thoát là mất danh sách).

### Phiên bản sau (gợi ý phát triển)
- Vòng lặp tương tác (add/list/done/del/clear).
- Lưu ra JSON (`todo.json`).
- Thêm hạn chót, độ ưu tiên, tag.
- In bảng đẹp mắt.
- Viết test và đóng gói thành CLI cài bằng `pipx`.

---

## License
Public domain / CC0-like intent. Reuse freely.