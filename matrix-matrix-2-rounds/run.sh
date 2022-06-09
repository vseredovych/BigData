#!/bin/bash
# This script should be executed from the directory where it is located.

################ Start ################
set -e

PWD=$(PWD)
PROJECT_NAME="matrix-matrix"

# Prepare project directory
! hdfs dfs -test -d $PROJECT_NAME && hdfs dfs -mkdir $PROJECT_NAME

############### Round 1 ###############
echo "Round 1 has started."

ROUND1_DIR="$PROJECT_NAME/round1"
ROUND1_INPUT_DIR="${ROUND1_DIR}/input"
ROUND1_OUTPUT_DIR="${ROUND1_DIR}/output"

# Create dedicated directory for this round if it doens't exist
! hdfs dfs -test -d $ROUND1_DIR && hdfs dfs -mkdir $ROUND1_DIR

# Delete the old output and input folders if exist
hdfs dfs -test -d $ROUND1_OUTPUT_DIR && hdfs dfs -rm -r $ROUND1_OUTPUT_DIR
hdfs dfs -test -d $ROUND1_INPUT_DIR && hdfs dfs -rm -r $ROUND1_INPUT_DIR

# Put input data folder
hdfs dfs -put ./input $ROUND1_INPUT_DIR

#  -D stream.map.input.field.separator=':' \
#  -D stream.num.map.input.key.fields=1 \
#  -D stream.reduce.input.field.separator=':' \ 
mapred streaming \
 -mapper "python3 $PWD/mapper1.py"  \
 -reducer "python3 $PWD/reducer1.py"  \
 -input "$ROUND1_INPUT_DIR/matrix1.txt" \
 -input "$ROUND1_INPUT_DIR/matrix2.txt"  \
 -output "$ROUND1_OUTPUT_DIR" \
 && hdfs dfs -cat ./$ROUND1_OUTPUT_DIR/part-00000

echo "Round 1 has finished."
############### Round 2 ###############
echo "Round 2 has started."

ROUND2_DIR="$PROJECT_NAME/round2"
ROUND2_OUTPUT_DIR="${ROUND2_DIR}/output"

# Create dedicated directory for this round if it doens't exist
! hdfs dfs -test -d $ROUND2_DIR && hdfs dfs -mkdir $ROUND2_DIR

# Delete the old output folder if exists
hdfs dfs -test -d $ROUND2_OUTPUT_DIR && hdfs dfs -rm -r ./$ROUND2_OUTPUT_DIR

mapred streaming \
 -D stream.reduce.input.field.separator=':' \
 -D stream.map.output.field.separator=':' \
 -mapper "python3 $PWD/mapper2.py"  \
 -reducer "python3 $PWD/reducer2.py"  \
 -input "$ROUND1_OUTPUT_DIR/part-00000" \
 -output "$ROUND2_OUTPUT_DIR" \
 && hdfs dfs -cat ./$ROUND2_OUTPUT_DIR/part-00000

echo "Round 1 has finished."
#######################################
