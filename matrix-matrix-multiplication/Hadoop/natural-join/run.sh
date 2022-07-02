#!/bin/bash
# This script should be executed from the directory where it is located.

################ Start ################
set -e
debug=1

PWD=$(PWD)

HADOOP_PROJECT_PATH="matrix-matrix"
PROJECT_NAME="natural-join"
LOCAL_OUTPUT_DIR="../../output"

# Prepare project directory
! hdfs dfs -test -d $HADOOP_PROJECT_PATH/$PROJECT_NAME && hdfs dfs -mkdir -p $HADOOP_PROJECT_PATH/$PROJECT_NAME

############### Round 1 ###############
echo "Round 1 has started."

ROUND1_DIR="$HADOOP_PROJECT_PATH/$PROJECT_NAME/round1"
ROUND1_INPUT_DIR="${ROUND1_DIR}/input"
ROUND1_OUTPUT_DIR="${ROUND1_DIR}/output"

# Create dedicated directory for this round if it doesn't exist
! hdfs dfs -test -d $ROUND1_DIR && hdfs dfs -mkdir $ROUND1_DIR

# Delete the old output and input folders if exist
hdfs dfs -test -d $ROUND1_OUTPUT_DIR && hdfs dfs -rm -r $ROUND1_OUTPUT_DIR
hdfs dfs -test -d $ROUND1_INPUT_DIR && hdfs dfs -rm -r $ROUND1_INPUT_DIR

# Put input data folder
hdfs dfs -put ../../input $ROUND1_INPUT_DIR

mapred streaming \
 -mapper "python3 $PWD/mapper1.py"  \
 -reducer "python3 $PWD/reducer1.py"  \
 -input "$ROUND1_INPUT_DIR/matrix1.txt" \
 -input "$ROUND1_INPUT_DIR/matrix2.txt"  \
 -output "$ROUND1_OUTPUT_DIR" \

[[ $debug -ne 0 ]] && hdfs dfs -cat ./$ROUND1_OUTPUT_DIR/part-00000

echo "Round 1 has finished."

############### Round 2 ###############
echo "Round 2 has started."

ROUND2_DIR="$HADOOP_PROJECT_PATH/$PROJECT_NAME/round2"
ROUND2_OUTPUT_DIR="${ROUND2_DIR}/output"

# Create dedicated directory for this round if it doesn't exist
! hdfs dfs -test -d $ROUND2_DIR && hdfs dfs -mkdir $ROUND2_DIR

# Delete the old output folder if exists
hdfs dfs -test -d $ROUND2_OUTPUT_DIR && hdfs dfs -rm -r ./$ROUND2_OUTPUT_DIR

mapred streaming \
 -D stream.reduce.input.field.separator=':' \
 -D stream.map.output.field.separator=':' \
 -mapper "python3 $PWD/mapper2.py"  \
 -reducer "python3 $PWD/reducer2.py"  \
 -input "$ROUND1_OUTPUT_DIR/part-00000" \
 -output "$ROUND2_OUTPUT_DIR"

echo "Round 1 has finished."
#######################################

# Copying output
[ ! -d $LOCAL_OUTPUT_DIR ] && mkdir -p $LOCAL_OUTPUT_DIR

hdfs dfs -get -f ./$ROUND2_OUTPUT_DIR/part-00000 \
  $LOCAL_OUTPUT_DIR/hadoop-${PROJECT_NAME}.txt


