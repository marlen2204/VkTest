import subprocess
import json
from config import IODEPTH_VALUES, FIO_BASE_PARAMS


class FioRunner:
    def __init__(self, test_name, filename):
        self.test_name = test_name
        self.filename = filename

    def _run_fio_command(self, rw, iodepth):
        """
        Выполняет команду fio и возвращает среднюю задержку.
        """
        fio_command = [
            "/usr/bin/fio",
            f"--name={self.test_name}",
            f"--filename={self.filename}",
            f"--rw={rw}",
            f"--iodepth={iodepth}",
            *FIO_BASE_PARAMS
        ]

        try:
            result = subprocess.run(fio_command, capture_output=True, text=True, check=True)
            fio_output = json.loads(result.stdout)
            if rw == "randread":
                latency = fio_output["jobs"][0]["read"]["clat_ns"]["mean"]
            elif rw == "randwrite":
                latency = fio_output["jobs"][0]["write"]["clat_ns"]["mean"]
            else:
                raise ValueError(f"Неизвестный тип операции: {rw}")
            return latency
        except subprocess.CalledProcessError as e:
            print(f"Ошибка выполнения fio для {rw} с iodepth={iodepth}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON-вывода fio: {e}")
            return None

    def run_tests(self):
        """
        Запускает fio для операций randread и randwrite и собирает результаты.
        """
        results = {"randread": [], "randwrite": []}

        for rw in results.keys():
            for iodepth in IODEPTH_VALUES:
                print(f"Запуск fio: {rw}, iodepth={iodepth}")
                latency = self._run_fio_command(rw, iodepth)
                if latency is not None:
                    results[rw].append((iodepth, latency))

        return results
