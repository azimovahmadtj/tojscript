from colorama import Fore, Style, init
init()
import re
import sys
import os

# 🎨 Цвета
colors = {
    "сабз": Fore.GREEN,
    "сурх": Fore.RED,
    "зард": Fore.YELLOW,
    "кабуд": Fore.BLUE,
    "норинҷӣ": Fore.LIGHTYELLOW_EX,
    "reset": Style.RESET_ALL
}

def toj_print(*args):
    text = ""
    color = ""
    for arg in args:
        if isinstance(arg, str):
            clean = arg.strip("/")
            if clean in colors:
                color = colors[clean]
                continue
        text += str(arg) + " "
    if color:
        print(color + text.strip() + colors["reset"])
    else:
        print(text.strip())

def brb(a, b): return a == b
def nbr(a, b): return a != b

def fakt(n):
    n = int(n)
    if n < 0: print("Хато: адад бояд мусбат бошад"); exit()
    result = 1
    for i in range(1, n + 1): result *= i
    return result

def fibonachi(n):
    n = int(n)
    if n <= 0: print("Хато: адад бояд > 0 бошад"); exit()
    a, b = 0, 1
    for _ in range(n - 1): a, b = b, a + b
    return b

def musb(x): return abs(int(x))

def darozi(x):
    try: return len(x)
    except: print("Хато: дарозӣ танҳо барои сатр ё рӯйхат аст"); exit()

def ilova(arr, x): arr.append(x); return arr
def pok(arr, i): return arr[i]
def калон(s): return str(s).upper()
def хурд(s): return str(s).lower()
def min_tj(*args): return min(*args)
def max_tj(*args): return max(*args)

def toq(*args):
    """Ададҳои тоқ — нечётные числа из аргументов"""
    result = [x for x in args if isinstance(x, (int, float)) and int(x) % 2 != 0]
    if not result: return []
    return result if len(result) != 1 else result[0]

def juft(*args):
    """Ададҳои ҷуфт — чётные числа из аргументов"""
    result = [x for x in args if isinstance(x, (int, float)) and int(x) % 2 == 0]
    if not result: return []
    return result if len(result) != 1 else result[0]

# ── ГРАФИКА (tkinter) ──────────────────────────────────────
_tk_root = None
_tk_canvas = None
_tk_colors = {
    "сабз": "green", "сурх": "red", "зард": "yellow",
    "кабуд": "blue", "норинҷӣ": "orange", "сафед": "white",
    "сиёҳ": "black", "бунафш": "purple", "садафӣ": "pink",
}

def _get_color(c):
    c = str(c).strip("/")
    return _tk_colors.get(c, c)

def экран(width=500, height=500, sarlavha="TojScript графика"):
    """Создать окно: экран(500, 500, "Номи тиреза")"""
    global _tk_root, _tk_canvas
    try:
        import tkinter as tk
        _tk_root = tk.Tk()
        _tk_root.title(sarlavha)
        _tk_canvas = tk.Canvas(_tk_root, width=width, height=height, bg="white")
        _tk_canvas.pack()
    except Exception as e:
        print("Хато (графика):", e)

def ранг(x, y, size, color="/сабз/", height=None):
    """Прямоугольник: ранг(x, y, андоза, "/сабз/")"""
    if _tk_canvas is None: print("Хато: аввал экран() фаро биёр"); return
    h = height if height else size
    _tk_canvas.create_rectangle(x, y, x+size, y+h, fill=_get_color(color), outline="")

def доира(x, y, radius, color="/сурх/"):
    """Круг: доира(x, y, радиус, "/сурх/")"""
    if _tk_canvas is None: print("Хато: аввал экран() фаро биёр"); return
    _tk_canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=_get_color(color), outline="")

def хат(x1, y1, x2, y2, color="/сиёҳ/", width=2):
    """Линия: хат(x1, y1, x2, y2, "/сиёҳ/")"""
    if _tk_canvas is None: print("Хато: аввал экран() фаро биёр"); return
    _tk_canvas.create_line(x1, y1, x2, y2, fill=_get_color(color), width=width)

def матн(x, y, text, color="/сиёҳ/", size=14):
    """Текст: матн(x, y, "Салом!", "/сиёҳ/")"""
    if _tk_canvas is None: print("Хато: аввал экран() фаро биёр"); return
    _tk_canvas.create_text(x, y, text=str(text), fill=_get_color(color), font=("Arial", size))

def пок_экран(color="/сафед/"):
    """Очистить экран: пок_экран()"""
    if _tk_canvas is None: return
    _tk_canvas.delete("all")
    _tk_canvas.configure(bg=_get_color(color))

def нишон():
    """Показать окно (вызывать последним): нишон()"""
    if _tk_root is None: print("Хато: аввал экран() фаро биёр"); return
    _tk_root.mainloop()


_input_buffer = []
def toj_input(prompt=""):
    global _input_buffer
    while not _input_buffer:
        line = input(prompt)
        parts = line.split()
        if len(parts) > 1:
            _input_buffer = parts
        else:
            return line.strip()
    return _input_buffer.pop(0)

TOJ_GLOBALS = {
    "toj_print": toj_print, "brb": brb, "nbr": nbr,
    "fakt": fakt, "fibonachi": fibonachi, "musb": musb,
    "darozi": darozi, "ilova": ilova, "pok": pok,
    "калон": калон, "хурд": хурд,
    "min_tj": min_tj, "max_tj": max_tj,
    "тоқ": toq, "ҷуфт": juft,
    # графика
    "экран": экран, "ранг": ранг, "доира": доира,
    "хат": хат, "матн": матн, "пок_экран": пок_экран, "нишон": нишон,
    "toj_input": toj_input, "input": toj_input, "print": print
}

def toj_to_python(code):
    code = re.sub(r'^\s*import\s+tojscript\s*$', '', code, flags=re.MULTILINE)

    translations = {
        "агар": "if", "дигар": "else", "чоп": "toj_print",
        "ворид": "toj_input", "барои": "for", "дар": "in",
        "функсия": "def", "баргардон": "return",
        "бутун": "int", "сатр": "str",
        "брб": "brb", "нбр": "nbr", "факт": "fakt",
        "фибоначи": "fibonachi", "мусб": "musb",
        "дарозӣ": "darozi", "мин": "min_tj", "макс": "max_tj",
        "тоқ": "тоқ", "ҷуфт": "ҷуфт",
        "дар_ҳолати": "while",
        "экран": "экран", "ранг": "ранг", "доира": "доира",
        "хат": "хат", "матн": "матн", "пок_экран": "пок_экран", "нишон": "нишон",
    }

    lines = code.split("\n")
    new_lines = []
    indent = 0

    for line in lines:
        stripped = line.strip()

        # метод-вызовы
        stripped = re.sub(r'(\w+)\.дарозӣ', r'darozi(\1)', stripped)
        stripped = re.sub(r'(\w+)\.калон\(\)', r'калон(\1)', stripped)
        stripped = re.sub(r'(\w+)\.хурд\(\)', r'хурд(\1)', stripped)

        # операторы присваивания *= += -= /=  (уже поддерживаются Python — просто пропускаем без изменений)

        if not stripped:
            continue

        # закрывающие скобки
        while stripped.startswith("}"):
            indent = max(indent - 1, 0)
            stripped = stripped[1:].strip()

        if not stripped:
            continue

        # оғоз() — точка входа
        if stripped.startswith("оғоз()"):
            new_lines.append("    " * indent + "if True:")
            indent += 1
            continue

        # просто открывающая скобка
        if stripped == "{":
            indent += 1
            continue

        # функсия ном(аргументҳо){ → def ном(аргументҳо):
        func_match = re.match(r'^функсия\s+(\w+)\s*\(([^)]*)\)\s*\{?$', stripped)
        if func_match:
            name, args = func_match.group(1), func_match.group(2)
            new_lines.append("    " * indent + f"def {name}({args}):")
            indent += 1
            continue

        # барои м (1..10){ → for м in range(1, 11):
        for_range = re.match(r'^барои\s+(\S+)\s*\((\d+)\.\.(\d+)\)\s*\{?$', stripped)
        if for_range:
            var, start, end = for_range.group(1), int(for_range.group(2)), int(for_range.group(3))
            new_lines.append("    " * indent + f"for {var} in range({start}, {end + 1}):")
            indent += 1
            continue

        # дар_ҳолати(условие){ → while условие:
        while_match = re.match(r'^дар_ҳолати\s*\((.+)\)\s*\{?$', stripped)
        if while_match:
            cond = while_match.group(1)
            new_lines.append("    " * indent + f"while {cond}:")
            indent += 1
            continue

        # перевод остальных ключевых слов
        for toj, py in translations.items():
            if toj in ("тоқ", "ҷуфт", "дар_ҳолати"):
                continue  # уже обработаны выше
            stripped = re.sub(rf'\b{toj}\b', py, stripped)

        # { в конце строки → двоеточие + увеличить отступ
        if "{" in stripped:
            stripped = stripped.replace("{", "").rstrip() + ":"
            new_lines.append("    " * indent + stripped)
            indent += 1
        else:
            new_lines.append("    " * indent + stripped)

    return "\n".join(new_lines)

def fix_file(filename):
    """Исправляет кодировку файла — конвертирует в UTF-8"""
    if not os.path.isabs(filename):
        filename = os.path.join(os.getcwd(), filename)
    if not os.path.exists(filename):
        print(f"Хато: файл '{filename}' не найден")
        sys.exit(1)

    with open(filename, "rb") as f:
        raw = f.read()

    # Пробуем все возможные кодировки
    decoded = None
    for enc in ["utf-8-sig", "utf-8", "cp1251", "cp1252", "iso-8859-1", "windows-1252"]:
        try:
            decoded = raw.decode(enc)
            break
        except Exception:
            continue

    if decoded is None:
        # Последняя попытка — игнорируем ошибки
        decoded = raw.decode("utf-8", errors="replace")

    # Сохраняем как UTF-8
    with open(filename, "w", encoding="utf-8") as f:
        f.write(decoded)
    print(f"✓ Файл '{os.path.basename(filename)}' конвертирован в UTF-8")

def run(filename):
    """Запуск .toj или .py файла"""
    # Если путь не абсолютный — ищем относительно текущей папки
    if not os.path.isabs(filename):
        filename = os.path.join(os.getcwd(), filename)

    if not os.path.exists(filename):
        print(f"Хато: файл '{filename}' не найден")
        sys.exit(1)

    # Автоопределение кодировки через chardet
    with open(filename, "rb") as f:
        raw = f.read()
    try:
        import chardet
        detected = chardet.detect(raw)
        enc = detected.get("encoding") or "utf-8"
    except ImportError:
        enc = "utf-8"
    try:
        code = raw.decode(enc)
    except Exception:
        try:
            code = raw.decode("utf-8", errors="replace")
        except Exception:
            print("Хато: не удалось прочитать файл")
            sys.exit(1)

    # Всегда запускаем как TojScript (работает с .py и .toj)
    python_code = toj_to_python(code)
    try:
        exec(python_code, {**TOJ_GLOBALS})
    except Exception as e:
        print("Хато:", e)

import base64 as _b64, tempfile as _tmp, subprocess as _sp

_VSIX_DATA = "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"

def install_extension():
    try:
        vsix_bytes = _b64.b64decode(_VSIX_DATA)
        tmp = _tmp.NamedTemporaryFile(suffix=".vsix", delete=False)
        tmp.write(vsix_bytes)
        tmp.close()
        result = _sp.run(["code", "--install-extension", tmp.name], capture_output=True, text=True)
        os.unlink(tmp.name)
        if result.returncode == 0:
            print("TojScript подсветка установлена!")
        else:
            print("VS Code не найден. Установи вручную: toj --get-extension")
    except Exception as e:
        print("Хато:", e)

def get_extension():
    try:
        vsix_bytes = _b64.b64decode(_VSIX_DATA)
        path = os.path.join(os.getcwd(), "tojlang.vsix")
        with open(path, "wb") as f:
            f.write(vsix_bytes)
        print("Файл сохранён:", path)
        print("Установи: code --install-extension tojlang.vsix")
    except Exception as e:
        print("Хато:", e)

def _auto_install_extension():
    """Автоустановка подсветки при первом запуске"""
    import tempfile
    flag = os.path.join(tempfile.gettempdir(), ".toj_ext_installed")
    if os.path.exists(flag):
        return
    try:
        result = _sp.run(["code", "--version"], capture_output=True, timeout=5)
        if result.returncode == 0:
            install_extension()
            open(flag, 'w').close()
    except Exception:
        pass

def main():
    _auto_install_extension()
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            print("TojScript 1.0.9")
            return
        if sys.argv[1] == "--fix" and len(sys.argv) > 2:
            fix_file(sys.argv[2])
            return
        if sys.argv[1] == "--install-extension":
            install_extension()
            return
        if sys.argv[1] == "--get-extension":
            get_extension()
            return
        run(sys.argv[1])
    else:
        # ищем main.toj в текущей папке
        default = os.path.join(os.getcwd(), "main.toj")
        if os.path.exists(default):
            run(default)
        else:
            print("Хато: укажи файл. Пример: toj main.toj")

if __name__ == "__main__":
    main()