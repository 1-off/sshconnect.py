import paramiko

class ssh_y:
    def __init__(self,host,port,username,password):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.host = host
        self.port = port
        self.username= username
        self.password = password
        self.ssh.connect(self.host, self.port, self.username, self.password)

    def execute(self,command:str):
        output = ''
        stdin, stdout, sterr = self.ssh.exec_command(command)
        for x in stdout:
            output+=line.strip('\n')
        print(output)
        
 
        
