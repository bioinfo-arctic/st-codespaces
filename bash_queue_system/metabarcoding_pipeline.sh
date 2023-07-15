# first step, check if there is any metabarcoding dataset currently running
if [ -f ~/queue_manager/running_file.txt ];
then
  echo -e "# $1 will be next \n$1"
else
  touch ~/queue_manager/running_file.txt
  echo -e "running $1\n" > ~/queue_manager/running_file.txt
  echo -e "start demultiplexing\n"
  sleep 3s
  echo -e "demultiplexing done\n"
  echo -e "start filtering and seq clean-up\n"
  sleep 2s
  echo -e "start clustering\n"
  sleep 10s
  echo -e "assign taxonomy\n"
  sleep 2s
  echo "all done.\nStarting next job\n"
  rm ~/queue_manager/running_file.txt
  echo -e "Finished $1\n" >> ~/queue_manager/finished_files.txt
fi
