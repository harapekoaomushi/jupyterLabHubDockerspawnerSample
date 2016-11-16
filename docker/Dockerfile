FROM jupyterhub/singleuser:latest
RUN conda install -c conda-forge jupyterlab --yes && \
    jupyter serverextension enable --py jupyterlab --sys-prefix
CMD ["sh", "/srv/singleuser/singleuser.sh", "--SingleUserNotebookApp.default_url=/lab", "--SingleUserNotebookApp.disable_user_config=True"]
