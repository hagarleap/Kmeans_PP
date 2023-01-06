1. k=3, max_iter = 333,  eps=0, input_1_db_1, input_1_db_2
2. k=7, max_iter = not provided, eps=0, input_2_db_1, input_2_db_2
3. k=15, max_iter = 750, eps=0, input_3_db_1, input_3_db_2

test line : python3 kmeans_pp.py 3 333 0 input_1_db_1.txt input_1_db_2.txt

python3 kmeans_pp.py 7 0 input_2_db_1.txt input_2_db_2.txt

python3 kmeans_pp.py 15 750 0 input_3_db_1.txt input_3_db_2.txt


python3 setup.py build_ext --inplace


python3 kmeans_pp.py 0 <input/input_1.txt"
python3 kmeans_pp.py 100000 <input/input_1.txt"
python3 kmeans_pp.py 100000 100000 <input/input_1.txt"
python3 kmeans_pp.py 100000 100 <input/input_1.txt"
python3 kmeans_pp.py 10 0 <input/input_1.txt"
python3 kmeans_pp.py 10 1000 <input/input_1.txt"
python3 kmeans_pp.py 10 1a0 <input/input_1.txt"
python3 kmeans_pp.py 1a0 10 <input/input_1.txt"
python3 kmeans_pp.py 0 <input/input_2.txt"
python3 kmeans_pp.py 100000 <input/input_2.txt"
python3 kmeans_pp.py 100000 100000 <input/input_2.txt"
python3 kmeans_pp.py 100000 100 <input/input_2.txt"
python3 kmeans_pp.py 10 0 <input/input_2.txt"
python3 kmeans_pp.py 10 1000 <input/input_2.txt"
python3 kmeans_pp.py 10 1a0 <input/input_2.txt"
python3 kmeans_pp.py 1a0 10 <input/input_2.txt"