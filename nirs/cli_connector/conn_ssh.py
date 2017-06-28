import paramiko
import time


class SshConn:

    problem_hosts = []

    def __init__(self, host, username, password, commands):
        self.host = host
        self.username = username
        self.password = password
        self.commands = commands
        self.client = paramiko.SSHClient()
        self.interactive_shell = None

    def single_host_conn(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname=self.host,
                                username=self.username,
                                password=self.password
                                )
        except OSError as err:
            print(err, '{0} is unreachable'.format(self.host), sep='/n')
            SshConn.problem_hosts.append(self.host)
        except paramiko.ssh_exception.AuthenticationException as err1:
            print(err1,
                  'Authentication failed with {0}'.format(self.host),
                  sep='/n'
                  )
            SshConn.problem_hosts.append(self.host)

        self.interactive_shell = self.client.invoke_shell()
        print("SSH подключение устанвлено к ", self.host)

    def send_commands_to_shell(self):
        shell = self.interactive_shell
        f = open(self.host + ".txt", "a")
        for command in self.commands:
            command += "\n"
            shell.send("\n")
            shell.send(command)
            time.sleep(2)
            output = shell.recv(10000)
            print(output.decode('utf-8'), "\n")
            f.write(output.decode('utf-8')+"\n")
        f.close()
        self.client.close()


def main():
    pass


if __name__ == '__main__':
    main()
