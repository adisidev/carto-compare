# remove all .csv except intersections.csv
for f in *.csv; do
  [[ $f == results_best_out_of_100.csv ]] && continue
  rm -f "$f"
done

rm -f *.tex

python3.10 combine.py

python3.10 latex.py

python3.10 summary/summary.py

python3.10 summary/latex.py
