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

