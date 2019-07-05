


# import paramiko
#
#
# def qytang_ssh(ip,user,passwd,port=22,cmd='ls'):
#     ssh = paramiko.SSHClient()
#     ssh.load_system_host_keys()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     ssh.connect(hostname=ip,username=user,password=passwd,timeout=5,compress=True)
#     stdin,stdout,stderr = ssh.exec_command(cmd)
#     x = stdout.read().decode()
#     return x
#
#
# if __name__ == '__main__':
#     print(qytang_ssh('10.1.1.12','root','P@ssw0rd'))
#     print(qytang_ssh('10.1.1.12','root','P@ssw0rd',cmd='pwd'))

import paramiko


def qytang_ssh(ip, username, password, port=22, cmd='sh ip int b'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('192.168.2.11', 'cisco', 'cisco', ))
