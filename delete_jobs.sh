#jenkins-jobs --conf /etc/jenkins_jobs/jenkins_jobs.ini delete main
jenkins-jobs --conf /etc/jenkins_jobs/jenkins_jobs.ini delete node-Manikanta
jenkins-jobs --conf /etc/jenkins_jobs/jenkins_jobs.ini delete node-Nandu
jenkins-jobs  delete --jobs-only node-Nikhil
jenkins-jobs  delete --jobs-only node-Ravichandra
rm -rf node-*
