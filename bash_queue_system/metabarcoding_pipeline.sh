# This script will process your metabarcoding files using a queue system.
# It has to be called as below:
# /workspaces/st-codespaces/bash_queue_system/metabarcoding_pipeline.sh your_file_address

# Here is the step-by-step
# Check if the queue_manager folder exists, if not, create one.
# The "-p" parameter will check if the folder already exists. If so it won't create a new one and won't through an error.
mkdir -p ~/queue_manager

# For making sure there is a queue, run this command:
touch ~/queue_manager/metabarcoding_analyses_queue.txt

# Check if there is any metabarcoding dataset currently running
if [ -f ~/queue_manager/running_file.txt ];
then
  echo -e "# $1 will be added to the queue \n"
  N_OF_FILES_TO_RUN=`wc -l ~/queue_manager/metabarcoding_analyses_queue.txt | cut -f 1 -d " "`
  echo -e "There are ${N_OF_FILES_TO_RUN} files in the queue\n"
  echo "/workspaces/st-codespaces/bash_queue_system/metabarcoding_pipeline.sh /new_user_00/his_file.tar.gz" >> ~/queue_manager/metabarcoding_analyses_queue.txt
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