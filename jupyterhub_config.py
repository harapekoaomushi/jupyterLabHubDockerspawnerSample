c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = '192.168.XXX.XXX' #hub private ip
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.hub_ip_connect = '192.168.XXX.XXX' #hub_private_ip
c.DockerSpawner.container_image = "XXXXXXXXXXXX"
c.JupyterHub.confirm_no_ssl =True
