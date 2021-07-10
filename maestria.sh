sudo docker run -m 8G --memory-reservation 2G --hostname=quickstart.cloudera --privileged=true -t -i -v $(pwd):/tbracamonte --publish-all=true -p 8888:8888 -p 8088:8088 -p 7180:7180 cloudera/quickstart /usr/bin/docker-quickstart

{
  "type": "record",
  "name": "StringPair",
  "doc": "A pair of strings.",
  "fields": [
    {"name": "left", "type": "string"},
    {"name": "right", "type": "string"}
  ]
}

.avsc

avro-tools random --count 100 --schema-file example_avro.avsc example_avro.avro


6  cat example_avro.avsc
7  avro-tools --help
8  avro-tools random
9  avro-tools random --count 1 --schema-file example_avro.avsc
10  avro-tools random --count 1 --schema-file example_avro.avsc -
11  avro-tools random --count 100 --schema-file example_avro.avsc example_avro.avro
12  ls
13  ls -l
14  cat example_avro.avro
15  avro-tools --help
16  avro-tools getschema
17  avro-tools getschema example_avro.avro
18  avro-tools getmeta example_avro.avro
19  avro-tools tojson
20  avro-tools tojson --pretty example_avro.avro
21  avro-tools tojson --pretty example_avro.avro > example_avro.json

40  ls -l
41  ls -lh
42  hadoop fs -ls /
43  hadoop fs -ls /user/cloudera
44  hadoop fs -mkdir /user/cloudera/2021_07_10
45  hadoop fs -put example_avro_500.avro /user/cloudera/2021_07_10/
46  hadoop fs -ls /user/cloudera
47  less example_avro_500.avro
48  hadoop fs -ls /user/cloudera/2021_07_10
49  hadoop fs -get /user/cloudera/2021_07_10/loan_1000.csv
50  ls -l
51  head -n3 loan_1000.csv

39  avro-tools random --count 500 --schema-file example_avro.avsc example_avro_500.avro
40  ls -l
41  ls -lh
42  hadoop fs -ls /
43  hadoop fs -ls /user/cloudera
44  hadoop fs -mkdir /user/cloudera/2021_07_10
45  hadoop fs -put example_avro_500.avro /user/cloudera/2021_07_10/
46  hadoop fs -ls /user/cloudera
47  less example_avro_500.avro
48  hadoop fs -ls /user/cloudera/2021_07_10
49  hadoop fs -get /user/cloudera/2021_07_10/loan_1000.csv
50  ls -l
51  head -n3 loan_1000.csv