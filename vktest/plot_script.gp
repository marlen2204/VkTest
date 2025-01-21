
            set terminal pngcairo size 1024,768 enhanced font 'Arial,10'
            set output 'output_1gb.png'

            set title 'Зависимость задержки от глубины очереди (IODEPTH)'

            set xlabel 'Глубина очереди (IODEPTH)'
            set ylabel 'Средняя задержка (Latency, мс)'

            set grid xtics ytics

            set key title "Тип операции"
            set key top left box

            set logscale x 2

            plot "randread.dat" using 1:($2/1000) with linespoints title "Чтение (randread)",                  "randwrite.dat" using 1:($2/1000) with linespoints title "Запись (randwrite)"
            