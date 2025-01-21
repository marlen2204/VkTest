
## 🚀 Тестирование производительности блочного устройства

Этот проект предназначен для выполнения тестов производительности блочного устройства с использованием утилиты fio. В результате тестирования строится график зависимости задержки (latency) от глубины очереди (iodepth) для операций randread и randwrite.

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/marlen2204/blktest/main/images/output_1gb.png" alt="График" style="width: 80%; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0px 4px 6px rgba(0,0,0,0.2); transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)';" onmouseout="this.style.transform='scale(1)';">
</div>

---

## ✅ Функциональность
1. ⚙️ Запуск тестов производительности с помощью fio.
2. 📊 Сбор данных о задержке (latency) для операций randread и randwrite.
3. 📈 Построение графика зависимости latency от iodepth.

---

## 🛠️ Требования
- 🐍 Python 3.7+
- 🧾 Poetry (управление зависимостями)
- 💾 fio (установленный в системе)

---

## 📥 Как использовать

### 🛠️ Клонирование репозитория
Склонируйте репозиторий в локальную директорию:
```bash
git clone https://github.com/marlen2204/blktest.git
```
Затем перейдите в папку `src`.

---

### 📦 Установка зависимостей

Используйте Poetry для установки всех зависимостей проекта:

1. ✅ Убедитесь, что Poetry установлен:
```bash 
poetry --version
```
Если Poetry не установлен, выполните:
```bash 
pip install poetry
```

2. 🔧 Установите зависимости проекта:
```bash 
poetry install
```

3. Установите fio:

#### 🐧 Linux
```bash
apt install fio
```

#### 🍎 MacOS
```bash
brew install fio
```

#### 🪟 Windows
Скачайте fio: [https://github.com/axboe/fio/releases](https://github.com/axboe/fio/releases).  
Добавьте путь к исполняемому файлу fio.exe в переменную PATH.

---

### 📝 Создание тестового файла

Перед запуском тестов создайте тестовый файл, который будет использоваться для проверки производительности.

#### 🐧 Linux / 🍎 MacOS
```bash
dd if=/dev/urandom of=testfile bs=1M count=1024
```

#### 🪟 Windows
Создайте файл размером 1 ГБ с помощью PowerShell:
```bash
fsutil file createnew testfile 1073741824
```

---

## ▶️ Запуск проекта
Для выполнения тестов и построения графика используйте следующую команду:

**Запуск через Poetry:**

```bash
poetry run python main.py --name=mytest --filename=testfile --output=output.png
```

#### Параметры:
- 🏷️ `--name` — имя теста (например, mytest).
- 📁 `--filename` — путь до файла, на котором будет выполняться тестирование (например, testfile).
- 📊 `--output` — имя выходного файла с графиком (например, output.png).

---

## 💡 Особенности запуска на macOS и Windows

- 🍎 **macOS**: Поскольку `libaio` недоступен, используется `posixaio`.
- 🪟 **Windows**: Используется `windowsaio`.
- 🐧 **Linux**: Используется `libaio`.

Эти изменения применяются автоматически в зависимости от операционной системы.

---

## 📈 Результат

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/marlen2204/blktest/main/images/output_1gb.png" alt="График" style="width: 80%; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0px 4px 6px rgba(0,0,0,0.2); transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)';" onmouseout="this.style.transform='scale(1)';">
</div>

---

## 📬 Контакты

- ✨ **Автор**: Марина Слобожанинова
- ✉️ **Email**: slobozhaninovaw@gmail.com
- 🐙 **GitHub**: [https://github.com/marlen2204](https://github.com/marlen2204)

