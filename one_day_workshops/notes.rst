Converting word doc with images to rst
--------------------------------------

::

  pandoc -f docx -t rst -o cloudformation_console.rst CloudFormation_Console.docx --extract-media=cloudformation
  
  rst2html cloudformation_console.rst > cloudformation_console.html
  
  
  
  agould@horus:~/git-repos/github/ucopacme/start-here/one_day_workshops> ll
  total 772
  -rw-rw-r--. 1 agould agould   4348 Dec 10 11:30 cloud9_and_awscli.rst
  -rw-rw-r--. 1 agould agould  10558 Dec 10 11:30 cloudformation_awscli.rst
  -rw-rw-r--. 1 agould agould 737276 Dec 10 11:30 CloudFormation_Console.docx
  -rw-rw-r--. 1 agould agould   4659 Dec 10 13:26 learning_git.rst
  -rw-rw-r--. 1 agould agould   4154 Dec 10 11:30 linux_workstation_setup.rst
  -rw-rw-r--. 1 agould agould    114 Dec 10 13:54 notes.txt
  -rw-rw-r--. 1 agould agould   5753 Dec  5 13:27 proposed_corriculum.rst
  -rw-rw-r--. 1 agould agould   2696 Dec 10 11:30 README.rst
  agould@horus:~/git-repos/github/ucopacme/start-here/one_day_workshops> pandoc -f docx -t rst -o cloudformation_console.rst CloudFormation_Console.docx --extract-media=cloudformation
  pandoc: extracting cloudformation/media/image1.png
  pandoc: extracting cloudformation/media/image10.png
  pandoc: extracting cloudformation/media/image11.png
  pandoc: extracting cloudformation/media/image12.png
  pandoc: extracting cloudformation/media/image13.png
  pandoc: extracting cloudformation/media/image14.png
  pandoc: extracting cloudformation/media/image2.png
  pandoc: extracting cloudformation/media/image3.png
  pandoc: extracting cloudformation/media/image4.png
  pandoc: extracting cloudformation/media/image5.png
  pandoc: extracting cloudformation/media/image6.png
  pandoc: extracting cloudformation/media/image7.png
  pandoc: extracting cloudformation/media/image8.png
  pandoc: extracting cloudformation/media/image9.png
  
  
  agould@horus:~/git-repos/github/ucopacme/start-here/one_day_workshops> find .
  .
  ./.README.rst.swp
  ./README.rst
  ./cloudformation_awscli.rst
  ./cloudformation
  ./cloudformation/media
  ./cloudformation/media/image6.png
  ./cloudformation/media/image11.png
  ./cloudformation/media/image10.png
  ./cloudformation/media/image3.png
  ./cloudformation/media/image12.png
  ./cloudformation/media/image5.png
  ./cloudformation/media/image7.png
  ./cloudformation/media/image9.png
  ./cloudformation/media/image1.png
  ./cloudformation/media/image8.png
  ./cloudformation/media/image4.png
  ./cloudformation/media/image14.png
  ./cloudformation/media/image2.png
  ./cloudformation/media/image13.png
  ./cloud9_and_awscli.rst
  ./cloudformation_console.rst
  ./.~lock.CloudFormation_Console.docx#
  ./notes.txt
  ./linux_workstation_setup.rst
  ./.notes.txt.swp
  ./learning_git.rst
  ./proposed_corriculum.rst
  ./CloudFormation_Console.docx
  
  
  agould@horus:~/git-repos/github/ucopacme/start-here/one_day_workshops> tail -50 cloudformation_console.rst 
  
  You are done with part 1 of CloudFormation.
  
  Part 2 will be using CloudFormation via AWS CLI
  
  In Part 2, we will do this via the AWS CLI, we will make a working web
  server.
  
  .. |image0| image:: cloudformation/media/image1.png
     :width: 6.50000in
     :height: 0.90972in
  .. |image1| image:: cloudformation/media/image2.png
     :width: 6.50000in
     :height: 0.72153in
  .. |image2| image:: cloudformation/media/image3.png
     :width: 6.50000in
     :height: 2.08056in
  .. |image3| image:: cloudformation/media/image4.png
     :width: 3.45749in
     :height: 5.47674in
  .. |image4| image:: cloudformation/media/image5.png
     :width: 6.19714in
     :height: 4.75982in
  .. |image5| image:: cloudformation/media/image6.png
     :width: 6.50000in
     :height: 1.46944in
  .. |image6| image:: cloudformation/media/image7.png
     :width: 6.50000in
     :height: 1.78958in
  .. |image7| image:: cloudformation/media/image8.png
     :width: 7.64287in
     :height: 2.52558in
  .. |image8| image:: cloudformation/media/image9.png
     :width: 6.50000in
     :height: 1.51458in
  .. |image9| image:: cloudformation/media/image10.png
     :width: 6.50000in
     :height: 1.48125in
  .. |image10| image:: cloudformation/media/image11.png
     :width: 6.50000in
     :height: 1.49236in
  .. |image11| image:: cloudformation/media/image12.png
     :width: 6.50000in
     :height: 1.58403in
  .. |image12| image:: cloudformation/media/image13.png
     :width: 6.50000in
     :height: 4.28611in
  .. |image13| image:: cloudformation/media/image14.png
     :width: 6.50000in
     :height: 3.69444in



