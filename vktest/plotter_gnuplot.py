import os
import subprocess


class Plotter:
    def __init__(self, output_file):
        self.output_file = output_file

    def plot_latency_vs_iodepth(self, results):
        """
        Создает PNG-график зависимости latency от iodepth с помощью gnuplot.
        """
        # Создаем два отдельных файла для чтения и записи
        randread_file = "randread.dat"
        randwrite_file = "randwrite.dat"

        with open(randread_file, "w") as f_read, open(randwrite_file, "w") as f_write:
            for rw, data in results.items():
                if data:
                    if rw == "randread":
                        for iodepth, latency in data:
                            f_read.write(f"{iodepth} {latency}\n")
                    elif rw == "randwrite":
                        for iodepth, latency in data:
                            f_write.write(f"{iodepth} {latency}\n")

        gnuplot_script = "plot_script.gp"
        with open(gnuplot_script, "w") as f:
            f.write(f"""
            set terminal pngcairo size 1024,768 enhanced font 'Arial,10'
            set output '{self.output_file}'

            set title 'Зависимость задержки от глубины очереди (IODEPTH)'

            set xlabel 'Глубина очереди (IODEPTH)'
            set ylabel 'Средняя задержка (Latency, мс)'

            set grid xtics ytics

            set key title "Тип операции"
            set key top left box

            set logscale x 2

            plot "{randread_file}" using 1:($2/1000) with linespoints title "Чтение (randread)", \
                 "{randwrite_file}" using 1:($2/1000) with linespoints title "Запись (randwrite)"
            """)

        try:
            subprocess.run(["gnuplot", gnuplot_script], check=True)
            print(f"График успешно сохранен в {self.output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка выполнения gnuplot: {e}")
#        finally:
#           os.remove(randread_file)
#           os.remove(randwrite_file)
#           os.remove(gnuplot_script)
