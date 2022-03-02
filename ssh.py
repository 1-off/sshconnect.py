import paramiko

class ssh:
    def __init__(self,host,port,username,password,command):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.host = host
        self.port = port
        self.username= username
        self.password = password
        self.command = command
        self.ssh.connect(self.host, self.port, self.username, self.password)

    def execute(self,command:str):
        self.ssh.exec_command(command)
