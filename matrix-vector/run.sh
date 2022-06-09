PWD=$(PWD)
NAME="matrix-vector"

hdfs dfs -rm ./matrix.txt && hdfs dfs -put matrix.txt matrix.txt
hdfs dfs -rm -r ./$NAME; mapred streaming  -mapper "python3 $PWD/mapper.py"  -reducer "python3 $PWD/reducer.py"  -input "./matrix.txt"  -output "$NAME/output" && hdfs dfs -cat  ./$NAME/output/part-00000