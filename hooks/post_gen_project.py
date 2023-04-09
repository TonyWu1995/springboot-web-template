import os
import platform

directory = '{{ cookiecutter.__package.replace('.','/') }}'
srcDir = 'src/main/java/' + directory
resouceDir='src/main/resources'
testDir = 'src/test/java/' + directory

os.makedirs(srcDir, exist_ok=True)
os.makedirs(resouceDir, exist_ok=True)
os.makedirs(testDir, exist_ok=True)


name ='{{ cookiecutter.applicationName }}'

os.rename("Application.java", srcDir + '/'+name+'.java')
os.rename("Tests.java", testDir + '/'+name+'Tests.java')
os.rename("application.yml", resouceDir + '/'+'application.yml')

os.system('mvn wrapper:wrapper')

if platform.system() =='Windows':
    os.system('mvnw.cmd verify')
else:
    os.system('mvnw verify')