FROM python:3.8
RUN useradd -ms /bin/bash qhduan
USER qhduan
WORKDIR /home/qhduan
ENV PATH="/home/qhduan/.local/bin:${PATH}"
COPY --chown=qhduan:qhduan ./requirements.txt .
RUN pip install --upgrade --user pip -i https://mirrors.aliyun.com/pypi/simple
RUN pip uninstall opencv-python -y
RUN pip install opencv-python-headless -i https://mirrors.aliyun.com/pypi/simple
RUN pip install --user -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
COPY --chown=qhduan:qhduan . .
EXPOSE 8000
HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1
ENTRYPOINT ["/home/qhduan/run.sh"]