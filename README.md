# Minimum Setting for Jupyterlab demonstration with Jupyterhub and dockerspawner
## Attention
This configuration is not safety. You should use SSL in some way (by `c.JupyterHub.ssl_cert` and `c.JupyterHub.ssl_key` option or by SSL offloader)

## Environment
* jupyterhub 0.6.1 (I don't use docker image of jupyterhub. This is installed on local environment)
* dockerspawner 0.5.0

## Instruction
1. `git clone https://github.com/harapekoaomushi/jupyterLabHubDockerspawnerSample`
1. `cd ./jupyterLabHubDockerspawnerSample/docker`
1. `docker build .`
1. `cd ..`
1. `vi jupyterhub_config.py` Put the image ID that you built now and your private ip on this config.
1. `sudo jupyterhub`
