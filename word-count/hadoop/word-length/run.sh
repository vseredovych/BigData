#!/bin/bash
# This script should be executed from the directory where it is located.

################ Start ################
set -e
debug=1

PWD=$(PWD)

HADOOP_PROJECT_PATH="words-operations"
PROJECT_NAME="word-length"
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
 -mapper "python3 $PWD/mapper.py"  \
 -reducer "python3 $PWD/reducer.py"  \
 -input "$ROUND1_INPUT_DIR/text.txt" \
 -output "$ROUND1_OUTPUT_DIR" \

[[ $debug -ne 0 ]] && hdfs dfs -cat ./$ROUND1_OUTPUT_DIR/part-00000

echo "Round 1 has finished."

#######################################

# Copying output
[ ! -d $LOCAL_OUTPUT_DIR ] && mkdir -p $LOCAL_OUTPUT_DIR

hdfs dfs -get -f ./$ROUND1_OUTPUT_DIR/part-00000 \
  $LOCAL_OUTPUT_DIR/hadoop-${PROJECT_NAME}.txt


