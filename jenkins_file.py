import sys
import requests



def CALLJENKINS ( Project, Parameter ):
	requests.get ( "http://localhost:8080/job/{0}/buildWithParameters?token=srivalli_project&Item={1}".format ( Project, Parameter ) )

print "\n\n\n\n", sys.argv, "\n\n\n\n"

if len ( sys.argv ) == 3:
	print  sys.argv[1], sys.argv[2]
else:
	print "please provide atleast one argument"
	exit ( 1 )


Device = sys.argv[1]
Slaves = sys.argv[2].split ( "," )

if Device == 'Samsung':
	for Item in Slaves:
		if  Item == 'nandu':
			CALLJENKINS ( 'node-NANDU', Item )
		if Item == 'nikhil':
			CALLJENKINS ( 'project_NIKHIL', Item )
		if Item == 'manikanta':
                        CALLJENKINS ( 'project_MANIKANTA', Item )
                if Item == 'windows-slave':
                        CALLJENKINS ( 'project_Ravichandra', Item )

elif Device == 'Oppo':
        for Item in Slaves:
                if  Item == 'nandu':
                        CALLJENKINS ( 'node-NANDU', Item )
                if Item == 'nikhil':
                        CALLJENKINS ( 'project_NIKHIL', Item )
                if Item == 'manikanta':
                        CALLJENKINS ( 'project_MANIKANTA', Item )
                if Item == 'windows-slave':
                        CALLJENKINS ( 'project_Ravichandra', Item )

elif Device == 'HTC':
        for Item in Slaves:
                if  Item == 'nandu':
                        CALLJENKINS ( 'node-NANDU', Item )
                if Item == 'nikhil':
                        CALLJENKINS ( 'project_NIKHIL', Item )
                if Item == 'manikanta':
                        CALLJENKINS ( 'project_MANIKANTA', Item )
                if Item == 'windows-slave':
                        CALLJENKINS ( 'project_Ravichandra', Item )
else:
	print "NOTHING"

