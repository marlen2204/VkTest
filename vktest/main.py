import argparse
from fio_runner import FioRunner
from plotter import Plotter


def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Тестирование производительности блочного устройства")
    parser.add_argument("--name", required=True, help="Имя теста")
    parser.add_argument("--filename", required=True, help="Путь до файла для тестирования")
    parser.add_argument("--output", required=True, help="Путь до PNG файла с графиком")
    args = parser.parse_args()

    # Создание экземпляра для выполнения тестов
    fio_runner = FioRunner(args.name, args.filename)

    # Генерация данных
    print("Запуск тестов fio...")
    results = fio_runner.run_tests()

    # Построение графика
    print("Построение графика...")
    plotter = Plotter(args.output)
    plotter.plot_latency_vs_iodepth(results)


if __name__ == "__main__":
    main()
