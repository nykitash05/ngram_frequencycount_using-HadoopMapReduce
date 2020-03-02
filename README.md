# ngram_frequencycount_using-HadoopMapReduce
To calculate frequency of ngrams - 2grams,3 grams from couple of documents using Hadoop MapReduce with Python

# Program Execution
Run below command:
(Change your hadoop cluster name/config)
hadoop jar /usr/hdp/3.0.0.0-1634/hadoop-mapreduce/hadoop-streaming.jar -file /home/sharman6/mapper1.py -mapper /home/sharman6/mapper1.py -file /home/sharman6/reducer1.py -reducer /home/sharman6/reducer1.py -input /user/kumarlt/books/input/* -output /user/sharman6/outputsol6

- To get first 50 words from the output file use:
hadoop fs -cat /user/sharman6/outputsol10/part-00000|head -n 50

- To get last 50 words from the output file use:
hadoop fs -cat /user/sharman6/outputsol10/part-00000|tail -n 50
