FROM totem/python-base:2.7

ADD . /opt/spec-python

EXPOSE 8080

ENTRYPOINT ["python", "/opt/spec-python/simple.py"]
CMD ["-d", "/opt/spec-python"]
